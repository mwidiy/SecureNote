# main.py (modifikasi dengan placeholder + validasi kunci string minimal 8 karakter)

import tkinter as tk
from tkinter import messagebox, filedialog
from cipher import caesar_encrypt, caesar_decrypt
from storage import save_encrypted_note, load_encrypted_note

class SecureNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureNote - Enkripsi Catatan Pribadi")
        self.root.geometry("600x500")

        # Label
        self.label_key = tk.Label(root, text="Kunci Caesar Cipher:")
        self.label_key.pack(pady=5)

        # Entry Key (dengan placeholder)
        self.entry_key = tk.Entry(root, fg='grey')
        self.entry_key.insert(0, "Masukkan kunci")
        self.entry_key.bind("<FocusIn>", self.clear_key_placeholder)
        self.entry_key.bind("<FocusOut>", self.restore_key_placeholder)
        self.entry_key.pack(pady=5)

        # Text Area (dengan placeholder)
        self.text_area = tk.Text(root, wrap=tk.WORD, fg='grey')
        self.text_area.insert("1.0", "Tuliskan catatan kamu...")
        self.text_area.bind("<FocusIn>", self.clear_text_placeholder)
        self.text_area.bind("<FocusOut>", self.restore_text_placeholder)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # Buttons
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.encrypt_btn = tk.Button(self.btn_frame, text="Enkripsi & Simpan", command=self.encrypt_and_save)
        self.encrypt_btn.grid(row=0, column=0, padx=10)

        self.load_btn = tk.Button(self.btn_frame, text="Muat & Dekripsi", command=self.load_and_decrypt)
        self.load_btn.grid(row=0, column=1, padx=10)

    # --- Placeholder Logic ---
    def clear_key_placeholder(self, event):
        if self.entry_key.get() == "Masukkan kunci":
            self.entry_key.delete(0, tk.END)
            self.entry_key.config(fg='black')

    def restore_key_placeholder(self, event):
        if not self.entry_key.get():
            self.entry_key.insert(0, "Masukkan kunci")
            self.entry_key.config(fg='grey')

    def clear_text_placeholder(self, event):
        current = self.text_area.get("1.0", tk.END).strip()
        if current == "Tuliskan catatan kamu...":
            self.text_area.delete("1.0", tk.END)
            self.text_area.config(fg='black')

    def restore_text_placeholder(self, event):
        if not self.text_area.get("1.0", tk.END).strip():
            self.text_area.insert("1.0", "Tuliskan catatan kamu...")
            self.text_area.config(fg='grey')

    # --- Encrypt & Save ---
    def encrypt_and_save(self):
        key_text = self.entry_key.get()
        note = self.text_area.get("1.0", tk.END).strip()

        if key_text == "Masukkan kunci" or not key_text:
            messagebox.showerror("Error", "Masukkan kunci terlebih dahulu!")
            return

        if len(key_text) < 8:
            messagebox.showerror("Error", "Kunci minimal harus 8 karakter!")
            return

        if note == "Tuliskan catatan kamu..." or not note:
            messagebox.showerror("Error", "Tuliskan catatan terlebih dahulu!")
            return

        try:
            key = sum(ord(c) for c in key_text) % 26
            encrypted_text = caesar_encrypt(note, key)
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt")])
            if file_path:
                save_encrypted_note(file_path, encrypted_text)
                messagebox.showinfo("Berhasil", "Catatan terenkripsi dan disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    # --- Load & Decrypt ---
    def load_and_decrypt(self):
        key_text = self.entry_key.get()

        if key_text == "Masukkan kunci" or not key_text:
            messagebox.showerror("Error", "Masukkan kunci terlebih dahulu!")
            return

        if len(key_text) < 8:
            messagebox.showerror("Error", "Kunci minimal harus 8 karakter!")
            return

        try:
            key = sum(ord(c) for c in key_text) % 26
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                encrypted_text = load_encrypted_note(file_path)
                decrypted_text = caesar_decrypt(encrypted_text, key)

                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, decrypted_text)
                self.text_area.config(fg='black')
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat atau dekripsi: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureNoteApp(root)
    root.mainloop()
