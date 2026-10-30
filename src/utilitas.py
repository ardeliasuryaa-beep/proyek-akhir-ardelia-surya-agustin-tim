def cetak_header(judul):
    """Mencetak header judul yang rapi di terminal."""
    print("=" * 50)
    print(f"{judul.center(50)}")
    print("=" * 50)


def tampilkan_ringkasan(statistik, ketuntasan):
    """Menampilkan hasil analisis statistik ke konsol."""
    print("\n--- RINGKASAN HASIL ANALISIS ---")
    print(f"Total Siswa Valid  : {statistik['jumlah_siswa']}")
    print(f"Rata-rata Nilai    : {statistik['rata_rata']:.2f}")
    print(f"Nilai Tertinggi    : {statistik['nilai_max']}")
    print(f"Nilai Terendah     : {statistik['nilai_min']}")
    print("-" * 35)
    print(f"Batas KKM          : {ketuntasan['kkm']}")
    print(f"Jumlah Tuntas      : {ketuntasan['jumlah_tuntas']}")
    print(f"Jumlah Belum Tuntas: {ketuntasan['jumlah_belum_tuntas']}")
    print(f"Persentase Ketuntasan: {ketuntasan['persentase_tuntas']:.2f}%")
    print("-" * 35)