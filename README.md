# Hybrid Cipher Studio

A Vigenère + Polybius hybrid cipher with a Python library/CLI and a browser UI.

**How it works:** the message is normalised to a 25-letter alphabet (J merged into I), shifted with a Vigenère key, then each letter is replaced by its row/column pair in a Polybius square. The square can be keyed with a second keyword, so there are two secrets.

## Use it
- **Web UI:** open `web/index.html` in any browser (no install, works offline).
- **CLI:** `python hybrid_cipher.py encrypt "Meet at dawn" --key LEMON --square MONARCHY`
- **Tests:** `pip install pytest && pytest`

## Limits
Spaces are kept as `/` between words in the ciphertext (this reveals word lengths); digits and punctuation are dropped on encrypt. This is a learning tool: classical ciphers can be broken, so use AES-GCM or ChaCha20 for anything real.

## Credit
Inspired by "Design and Analysis of Cryptographic Technique for Communication System" by Shivam Vatshayan. This is an independent implementation of the Vigenère + Polybius idea; no code from that repository is used.

# app link
https://frolicking-douhua-eb12b5.netlify.app/
