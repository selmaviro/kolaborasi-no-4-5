# Fungsi Laporan
def cetak_laporan(data):
    print("=== LAPORAN PROYEK ===")
    for idx, item in enumerate(data, 1):
        print(f"{idx}. Nama: {item.get('nama')} | Nilai: {item.get('nilai')}")

if __name__ == "__main__":
    sample_data = [{"nama": "Ayu", "nilai": "90"}, {"nama": "Budi", "nilai": "85"}]
    cetak_laporan(sample_data)
