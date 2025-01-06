import docx
import tkinter as tk
from tkinter import filedialog, messagebox

def hitung_kata_dari_file(file_path):
    """
    Fungsi untuk menghitung jumlah kata dalam sebuah file Word (.docx).
    :param file_path: string, path ke file Word yang akan dihitung jumlah katanya
    :return: int, jumlah kata dalam file
    """
    try:
        doc = docx.Document(file_path)
        teks = " ".join(paragraph.text for paragraph in doc.paragraphs)
        kata = teks.split()
        return len(kata)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        return 0

def pilih_file():
    file_path = filedialog.askopenfilename(
        title="Pilih File Word",
        filetypes=[("File Word", "*.docx")]
    )
    if file_path:
        jumlah_kata = hitung_kata_dari_file(file_path)
        label_hasil.config(text=f"Jumlah kata dalam file adalah: {jumlah_kata}")

def buat_gui():
    root = tk.Tk()
    root.title("Penghitung Kata dalam File Word")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label_instruksi = tk.Label(frame, text="Klik tombol di bawah untuk memilih file Word (.docx):")
    label_instruksi.pack(pady=5)

    tombol_pilih = tk.Button(frame, text="Pilih File", command=pilih_file)
    tombol_pilih.pack(pady=5)

    global label_hasil
    label_hasil = tk.Label(frame, text="")
    label_hasil.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    buat_gui()
