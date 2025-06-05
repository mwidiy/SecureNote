# storage.py

def save_encrypted_note(filepath, encrypted_text):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

def load_encrypted_note(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
