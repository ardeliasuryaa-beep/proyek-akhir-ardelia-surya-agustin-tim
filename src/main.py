import os
from analisis import hitung_ketuntasan, hitung_statistik
from data_io import baca_data, simpan_laporan
from utilitas import cetak_header, tampilkan_ringkasan


def main():
    cetak_header("PROGRAM REKAP DAN ANALISIS NILAI")

    # Path file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_input = os.path.join(base_dir, "data", "nilai_contoh.txt")
    file_output = os.path.join(base_dir, "output", "laporan.txt")

    print(f"Membaca data dari: {file_input} ...")

    try:
        # 1. Baca & Validasi Data
        data_siswa = baca_data(file_input)

        if not data_siswa:
            print(
                "\n[Peringatan] Tidak ada data nilai valid yang dapat diproses."
            )
            return

        # 2. Hitung Statistik & Ketuntasan (KKM standar = 75)
        kkm = 75
        statistik = hitung_statistik(data_siswa)
        ketuntasan = hitung_ketuntasan(data_siswa, kkm=kkm)

        # 3. Tampilkan Hasil di Console
        tampilkan_ringkasan(statistik, ketuntasan)

        # 4. Simpan Hasil ke File Laporan
        simpan_laporan(file_output, statistik, ketuntasan)

    except FileNotFoundError as err:
        print(f"\n[Error] {err}")
    except Exception as err:
        print(f"\n[Error Tidak Terduga] {err}")


if __name__ == "__main__":
    main()