import os
from cryptography.fernet import Fernet

def get_key():
    key = os.getenv("FERNET_KEY")
    if not key:
        raise Exception("Clé FERNET_KEY introuvable !")
    return key.encode()

def encrypt_file(input_file, output_file):
    key = get_key()
    f = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted)

    print("Fichier chiffré")

def decrypt_file(input_file, output_file):
    key = get_key()
    f = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    with open(output_file, "wb") as file:
        file.write(decrypted)

    print("Fichier déchiffré")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: encrypt/decrypt input output")
        exit()

    mode = sys.argv[1]

    if mode == "encrypt":
        encrypt_file(sys.argv[2], sys.argv[3])
    elif mode == "decrypt":
        decrypt_file(sys.argv[2], sys.argv[3])