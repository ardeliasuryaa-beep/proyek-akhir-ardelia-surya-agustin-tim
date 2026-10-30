import os


def baca_data(file_path):
    """Membaca file data nilai teks dan mengembalikannya sebagai list of dictionary.

    Format file yang diharapkan per baris: nama,nilai
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' tidak ditemukan.")

    data_siswa = []
    with open(file_path, "r", encoding="utf-8") as file:
        for baris_ke, baris in enumerate(file, 1):
            baris = baris.strip()
            if not baris:
                continue  # Abaikan baris kosong

            bagian = baris.split(",")
            if len(bagian) != 2:
                print(
                    f"[Peringatan] Baris {baris_ke} diabaikan (format tidak valid): {baris}"
                )
                continue

            nama, str_nilai = bagian[0].strip(), bagian[1].strip()

            try:
                nilai = float(str_nilai)
                if validasi_nilai(nilai):
                    data_siswa.append({"nama": nama, "nilai": nilai})
                else:
                    print(
                        f"[Peringatan] Baris {baris_ke} diabaikan (nilai di luar rentang 0-100): {nilai}"
                    )
            except ValueError:
                print(
                    f"[Peringatan] Baris {baris_ke} diabaikan (nilai bukan angka): {str_nilai}"
                )

    return data_siswa


def validasi_nilai(nilai):
    """Memvalidasi apakah nilai berada pada rentang valid (0 - 100)."""
    return 0 <= nilai <= 100


def simpan_laporan(file_path, hasil_statistik, hasil_ketuntasan):
    """Menyimpan hasil rekapitulasi analisis ke file teks laporan."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("=========================================\n")
        file.write("      LAPORAN REKAPITULASI NILAI         \n")
        file.write("=========================================\n\n")

        file.write("1. STATISTIK KELAS\n")
        file.write(
            f"   - Total Siswa Valid  : {hasil_statistik['jumlah_siswa']} orang\n"
        )
        file.write(
            f"   - Rata-rata Nilai    : {hasil_statistik['rata_rata']:.2f}\n"
        )
        file.write(
            f"   - Nilai Tertinggi    : {hasil_statistik['nilai_max']}\n"
        )
        file.write(
            f"   - Nilai Terendah     : {hasil_statistik['nilai_min']}\n\n"
        )

        file.write("2. ANALISIS KETUNTASAN (KKM)\n")
        file.write(f"   - Batas KKM          : {hasil_ketuntasan['kkm']}\n")
        file.write(
            f"   - Jumlah Tuntas      : {hasil_ketuntasan['jumlah_tuntas']} orang\n"
        )
        file.write(
            f"   - Jumlah Belum Tuntas: {hasil_ketuntasan['jumlah_belum_tuntas']} orang\n"
        )
        file.write(
            f"   - Persentase Tuntas  : {hasil_ketuntasan['persentase_tuntas']:.2f}%\n"
        )

    print(f"\n[Sukses] Laporan berhasil disimpan ke '{file_path}'")