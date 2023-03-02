import random

def substitution_cipher(plaintext, key):
  
    mapping = {}
    for i, letter in enumerate(key):
        mapping[chr(ord('a') + i)] = letter

    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            letter = letter.lower()
            ciphertext += mapping.get(letter, letter)
        else:
            ciphertext += letter
    return ciphertext


plaintext = "hello world"
key = "qazwsxedcrfvtgbyhnujmikolp" #enter alphabet in random order
key = ""
ciphertext = substitution_cipher(plaintext, key)
print(ciphertext)  
