import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from hybrid_cipher import clean, decrypt, encrypt, vigenere


def test_roundtrip():
    msg = clean("Meet at the north gate at dawn")
    for vk, sk in [("LEMON", ""), ("secret", "monarchy"), ("a", "zebra")]:
        assert decrypt(encrypt(msg, vk, sk), vk, sk) == msg


def test_vigenere_inverse():
    assert vigenere(vigenere("HELLOWORLD", "KEY"), "KEY", decrypt=True) == clean("HELLOWORLD")


def test_square_key_changes_output():
    assert encrypt("HELLO", "KEY", "") != encrypt("HELLO", "KEY", "MONARCHY")


def test_spaces_preserved():
    ct = encrypt("Meet at the north gate", "LEMON", "MONARCHY")
    assert "/" in ct
    assert decrypt(ct, "LEMON", "MONARCHY") == "MEET AT THE NORTH GATE"
