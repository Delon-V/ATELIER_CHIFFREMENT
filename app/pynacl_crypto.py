import os
from nacl.secret import SecretBox
from nacl.utils import random

KEY_FILE = "key.bin"

def generate_key():
    key = random(SecretBox.KEY_SIZE)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("Clé générée")

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(input_file, output_file):
    key = load_key()
    box = SecretBox(key)

    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = box.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted)

    print("Fichier chiffré")

def decrypt_file(input_file, output_file):
    key = load_key()
    box = SecretBox(key)

    with open(input_file, "rb") as f:
        data = f.read()

    decrypted = box.decrypt(data)

    with open(output_file, "wb") as f:
        f.write(decrypted)

    print("Fichier déchiffré")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: generate/encrypt/decrypt ...")
        exit()

    mode = sys.argv[1]

    if mode == "generate":
        generate_key()
    elif mode == "encrypt":
        encrypt_file(sys.argv[2], sys.argv[3])
    elif mode == "decrypt":
        decrypt_file(sys.argv[2], sys.argv[3])