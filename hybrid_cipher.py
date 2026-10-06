"""Hybrid cipher: Vigenere (stage 1) followed by a keyed Polybius square (stage 2).

Educational only. Classical ciphers are NOT secure; use AES-GCM or ChaCha20 for real data.
Alphabet: 25 letters (J is merged into I). Word spaces are kept as '/' in the ciphertext.
"""
import argparse

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def clean(text: str) -> str:
    """Uppercase, merge J into I, keep only A-Z letters."""
    return "".join(c for c in text.upper().replace("J", "I") if c in ALPHABET)


def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    key = clean(key)
    if not key:
        raise ValueError("Vigenere key needs at least one letter")
    sign = -1 if decrypt else 1
    return "".join(
        ALPHABET[(ALPHABET.index(c) + sign * ALPHABET.index(key[i % len(key)])) % 25]
        for i, c in enumerate(clean(text))
    )


def polybius_square(keyword: str = "") -> str:
    """25-letter square: keyword letters first (deduplicated), then the rest."""
    return "".join(dict.fromkeys(clean(keyword) + ALPHABET))


def polybius_encrypt(text: str, keyword: str = "") -> str:
    sq = polybius_square(keyword)
    return " ".join(f"{sq.index(c) // 5 + 1}{sq.index(c) % 5 + 1}" for c in clean(text))


def polybius_decrypt(digits: str, keyword: str = "") -> str:
    sq, d = polybius_square(keyword), [c for c in digits if c in "12345"]
    return "".join(sq[(int(d[i]) - 1) * 5 + int(d[i + 1]) - 1] for i in range(0, len(d) - 1, 2))


def _split(text: str, words: list) -> list:
    out, i = [], 0
    for w in words:
        out.append(text[i:i + len(w)])
        i += len(w)
    return out


def encrypt(plaintext: str, vigenere_key: str, square_key: str = "") -> str:
    """Spaces become ' / ' between words; the Vigenere key runs across the whole message."""
    words = [w for w in (clean(w) for w in plaintext.split()) if w]
    shifted = _split(vigenere("".join(words), vigenere_key), words)
    return " / ".join(polybius_encrypt(w, square_key) for w in shifted)


def decrypt(ciphertext: str, vigenere_key: str, square_key: str = "") -> str:
    parts = [p for p in (polybius_decrypt(p, square_key) for p in ciphertext.split("/")) if p]
    plain = vigenere("".join(parts), vigenere_key, decrypt=True)
    return " ".join(_split(plain, parts))


def main() -> None:
    ap = argparse.ArgumentParser(description="Vigenere + Polybius hybrid cipher")
    ap.add_argument("mode", choices=["encrypt", "decrypt"])
    ap.add_argument("text")
    ap.add_argument("--key", required=True, help="Vigenere key")
    ap.add_argument("--square", default="", help="Polybius square keyword")
    a = ap.parse_args()
    print((encrypt if a.mode == "encrypt" else decrypt)(a.text, a.key, a.square))


if __name__ == "__main__":
    main()
