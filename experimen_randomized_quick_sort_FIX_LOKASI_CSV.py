# Eksperimen Kinerja Randomized Quick Sort dan Merge Sort
# Studi kasus: pengurutan IPK mahasiswa dari tertinggi ke terendah
# Modul time hanya digunakan untuk mengukur waktu eksekusi.

import time
import csv
from pathlib import Path


def angka_acak(seed, batas):
    seed = (seed * 1103515245 + 12345) % (2 ** 31)
    return seed, seed % batas


def buat_data(jumlah, seed):
    data = []
    for i in range(jumlah):
        seed, nilai = angka_acak(seed, 401)
        # IPK disimpan sebagai bilangan bulat dalam skala 0.00-4.00
        ipk = nilai / 100.0
        data.append(ipk)
    return data


def randomized_quick_sort(data, seed):
    hasil = data[:]

    def quick_sort(kiri, kanan, seed_sekarang):
        if kiri >= kanan:
            return seed_sekarang

        seed_sekarang, angka = angka_acak(
            seed_sekarang, kanan - kiri + 1
        )
        indeks_pivot = kiri + angka
        hasil[indeks_pivot], hasil[kanan] = (
            hasil[kanan], hasil[indeks_pivot]
        )
        pivot = hasil[kanan]

        # Partisi tiga arah agar nilai IPK duplikat tidak membuat
        # pembagian menjadi sangat tidak seimbang.
        lebih = kiri
        sekarang = kiri
        kurang = kanan

        while sekarang <= kurang:
            if hasil[sekarang] > pivot:
                hasil[lebih], hasil[sekarang] = (
                    hasil[sekarang], hasil[lebih]
                )
                lebih += 1
                sekarang += 1
            elif hasil[sekarang] < pivot:
                hasil[sekarang], hasil[kurang] = (
                    hasil[kurang], hasil[sekarang]
                )
                kurang -= 1
            else:
                sekarang += 1

        seed_sekarang = quick_sort(kiri, lebih - 1, seed_sekarang)
        seed_sekarang = quick_sort(kurang + 1, kanan, seed_sekarang)
        return seed_sekarang

    quick_sort(0, len(hasil) - 1, seed)
    return hasil


def merge_sort_menurun(data):
    if len(data) <= 1:
        return data[:]

    tengah = len(data) // 2
    kiri = merge_sort_menurun(data[:tengah])
    kanan = merge_sort_menurun(data[tengah:])

    hasil = []
    i = 0
    j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] >= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1

    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1

    return hasil


def rata_rata(nilai):
    total = 0.0
    for x in nilai:
        total += x
    return total / len(nilai)


def simpangan_baku(nilai):
    # Simpangan baku sampel
    if len(nilai) < 2:
        return 0.0

    mean = rata_rata(nilai)
    total = 0.0
    for x in nilai:
        total += (x - mean) ** 2
    return (total / (len(nilai) - 1)) ** 0.5


def sudah_urut_menurun(data):
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            return False
    return True


def main():
    ukuran_data = [100, 500, 1000, 5000, 10000]
    jumlah_pengulangan =5
    hasil_eksperimen = []

    print("=" * 78)
    print("EKSPERIMEN RANDOMIZED QUICK SORT DAN MERGE SORT")
    print("Urutan IPK: tertinggi ke terendah")
    print("Setiap ukuran diuji sebanyak", jumlah_pengulangan, "kali")
    print("=" * 78)

    print(
        "{:>8} | {:>14} | {:>14} | {:>14} | {:>14}".format(
            "Jumlah", "Algoritma", "Rata-rata (s)", "SD (s)", "Status"
        )
    )
    print("-" * 78)

    for jumlah in ukuran_data:
        waktu_quick = []
        waktu_merge = []
        benar = True

        for percobaan in range(jumlah_pengulangan):
            # Seed data dibuat berbeda untuk setiap percobaan,
            # tetapi tetap dapat diulang jika program dijalankan ulang.
            seed_data = 20261011 + jumlah * 17 + percobaan
            data = buat_data(jumlah, seed_data)

            mulai = time.perf_counter()
            hasil_quick = randomized_quick_sort(
                data, seed_data + 99
            )
            selesai = time.perf_counter()
            waktu_quick.append(selesai - mulai)

            mulai = time.perf_counter()
            hasil_merge = merge_sort_menurun(data)
            selesai = time.perf_counter()
            waktu_merge.append(selesai - mulai)

            if not sudah_urut_menurun(hasil_quick):
                benar = False
            if not sudah_urut_menurun(hasil_merge):
                benar = False
            if hasil_quick != hasil_merge:
                benar = False

        status = "LULUS" if benar else "GAGAL"
        hasil_eksperimen.append({
            "Jumlah Data": jumlah,
            "Algoritma": "Randomized Quick Sort",
            "Rata-rata Waktu": rata_rata(waktu_quick),
            "Simpangan Baku": simpangan_baku(waktu_quick),
            "Status": status
        }) 
        hasil_eksperimen.append({
            "Jumlah Data": jumlah,
            "Algoritma": "Merge Sort",
            "Rata-rata Waktu": rata_rata(waktu_merge),
            "Simpangan Baku": simpangan_baku(waktu_merge),
            "Status": status
        })

        print(
            "{:>8} | {:>14} | {:>14.6f} | {:>14.6f} | {:>14}".format(
                jumlah, "Randomized QS", rata_rata(waktu_quick),
                simpangan_baku(waktu_quick), status
            )
        )
        print(
            "{:>8} | {:>14} | {:>14.6f} | {:>14.6f} | {:>14}".format(
                jumlah, "Merge Sort", rata_rata(waktu_merge),
                simpangan_baku(waktu_merge), status
            )
        )
        print("-" * 78)

    print("\nKeterangan:")
    print("- Rata-rata adalah rata-rata waktu dari 5 pengulangan.")
    print("- SD adalah simpangan baku sampel waktu eksekusi.")
    print("- LULUS berarti hasil kedua algoritma sama dan terurut menurun.")
    print("- Waktu dapat berbeda tergantung spesifikasi dan beban laptop.")

    # Simpan CSV di folder yang sama dengan file Python ini
    lokasi_csv = Path(__file__).resolve().parent / "hasil_eksperimen.csv"
    with open(lokasi_csv, "w", newline="", encoding="utf-8-sig") as file:
        kolom = [
            "Jumlah Data",
            "Algoritma",
            "Rata-rata Waktu",
            "Simpangan Baku",
            "Status",
        ]
        penulis = csv.DictWriter(file, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(hasil_eksperimen)

    print(f"\nHasil eksperimen berhasil disimpan di: {lokasi_csv}")


if __name__ == "__main__":
    main()
