import docx

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
        print(f"Terjadi kesalahan: {e}")
        return 0

def main():
    print("Program Penghitung Kata dari File Word")
    print("=====================================")
    file_path = input("Masukkan path file Word (.docx): ")
    jumlah_kata = hitung_kata_dari_file(file_path)
    print(f"Jumlah kata dalam file adalah: {jumlah_kata}")

if __name__ == "__main__":
    main()
