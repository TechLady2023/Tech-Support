# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:07:34 2023

@author: LRJ
"""

def create_decryption_cipher(substitution):
    substitution = substitution.upper()
    decryption_cipher = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!,. "
    for i, char in enumerate(substitution):
        decryption_cipher[char] = alphabet[i % len(alphabet)]
    return decryption_cipher

def decrypt_message(message, cipher):
    decryption_cipher = create_decryption_cipher(cipher)
    decrypted_message = ''.join(decryption_cipher.get(char, char) for char in message)
    return decrypted_message

def main():
    provided_substitution = "0123456789!@#$%^&*:;?,.<>+-_`~ "  # Replace this with the same substitution used in encryption.py
    encrypted_message = input("Enter the encrypted message: ")
    decrypted_message = decrypt_message(encrypted_message, provided_substitution)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()


