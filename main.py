# Program Utama Kelompok

def input_data():
    nama = input("Masukkan Nama: ")
    nilai = input("Masukkan Nilai: ")
    return {"nama": nama, "nilai": nilai}

if __name__ == "__main__":
    data = input_data()
    print("Data tersimpan:", data)
