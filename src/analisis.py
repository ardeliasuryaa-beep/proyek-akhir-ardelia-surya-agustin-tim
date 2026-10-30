def hitung_statistik(data_siswa):
    """Menhitung rata-rata, nilai minimum, dan nilai maksimum dari list siswa."""
    if not data_siswa:
        return {
            "jumlah_siswa": 0,
            "rata_rata": 0.0,
            "nilai_min": 0,
            "nilai_max": 0,
        }

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    jumlah_siswa = len(daftar_nilai)
    total_nilai = sum(daftar_nilai)
    rata_rata = total_nilai / jumlah_siswa
    nilai_min = min(daftar_nilai)
    nilai_max = max(daftar_nilai)

    return {
        "jumlah_siswa": jumlah_siswa,
        "rata_rata": rata_rata,
        "nilai_min": nilai_min,
        "nilai_max": nilai_max,
    }


def hitung_ketuntasan(data_siswa, kkm=75):
    """Menentukan status ketuntasan siswa berdasarkan nilai KKM."""
    if not data_siswa:
        return {
            "kkm": kkm,
            "jumlah_tuntas": 0,
            "jumlah_belum_tuntas": 0,
            "persentase_tuntas": 0.0,
        }

    jumlah_tuntas = sum(1 for siswa in data_siswa if siswa["nilai"] >= kkm)
    jumlah_total = len(data_siswa)
    jumlah_belum_tuntas = jumlah_total - jumlah_tuntas
    persentase_tuntas = (
        (jumlah_tuntas / jumlah_total) * 100 if jumlah_total > 0 else 0.0
    )

    return {
        "kkm": kkm,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas,
        "persentase_tuntas": persentase_tuntas,
    }