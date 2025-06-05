# cipher.py

def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            # Geser huruf besar
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            # Geser huruf kecil
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            # Karakter non-huruf tidak berubah
            result += char
    return result

def caesar_decrypt(text, key):
    # Dekripsi dengan menggeser ke arah sebaliknya
    return caesar_encrypt(text, -key)
