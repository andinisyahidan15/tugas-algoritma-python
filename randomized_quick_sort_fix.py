# Randomized Quick Sort untuk Mengurutkan IPK Mahasiswa
# Urutan: IPK tertinggi ke terendah
# Tanpa library tambahan dan tanpa sort()/sorted()

# Generator angka pseudo-acak sederhana agar hasil dapat diulang.
# Seed yang sama akan menghasilkan urutan angka yang sama.
def angka_acak(seed, batas):
    seed = (seed * 1103515245 + 12345) % (2 ** 31)
    indeks = seed % batas
    return seed, indeks


def salin_data(data):
    hasil = []
    for mahasiswa in data:
        hasil.append(mahasiswa)
    return hasil


def tampilkan_data(data):
    for nama, ipk in data:
        print("  {:<15} IPK: {:.2f}".format(nama, ipk))


def randomized_quick_sort(data, seed, tampilkan_langkah=True):
    # Salin data agar data asli tidak berubah
    hasil = salin_data(data)

    def quick_sort(kiri, kanan, seed_sekarang):
        if kiri >= kanan:
            return seed_sekarang

        # Memilih pivot secara pseudo-acak
        seed_sekarang, angka = angka_acak(
            seed_sekarang, kanan - kiri + 1
        )
        indeks_pivot = kiri + angka

        # Pindahkan pivot terpilih ke posisi paling kanan
        hasil[indeks_pivot], hasil[kanan] = (
            hasil[kanan], hasil[indeks_pivot]
        )
        nilai_pivot = hasil[kanan][1]

        if tampilkan_langkah:
            print("\nRentang indeks:", kiri, "sampai", kanan)
            print("Seed setelah pembaruan:", seed_sekarang)
            print("Angka pseudo-acak:", angka)
            print("Pivot terpilih:", hasil[kanan][0],
                  "dengan IPK", "{:.2f}".format(nilai_pivot))

        # Partisi: IPK yang lebih tinggi atau sama
        # ditempatkan di sebelah kiri pivot
        batas = kiri
        for indeks in range(kiri, kanan):
            if hasil[indeks][1] >= nilai_pivot:
                hasil[batas], hasil[indeks] = (
                    hasil[indeks], hasil[batas]
                )
                batas += 1

        # Letakkan pivot pada posisi akhirnya
        hasil[batas], hasil[kanan] = (
            hasil[kanan], hasil[batas]
        )

        if tampilkan_langkah:
            print("Posisi akhir pivot:", batas)
            print("Bagian kiri pivot:")
            tampilkan_data(hasil[kiri:batas])
            print("Bagian kanan pivot:")
            tampilkan_data(hasil[batas + 1:kanan + 1])

        # Urutkan bagian kiri dan kanan secara rekursif
        seed_sekarang = quick_sort(
            kiri, batas - 1, seed_sekarang
        )
        seed_sekarang = quick_sort(
            batas + 1, kanan, seed_sekarang
        )

        return seed_sekarang

    quick_sort(0, len(hasil) - 1, seed)
    return hasil


def jalankan_pengujian(judul, data, seed):
    print("\n" + "=" * 55)
    print(judul)
    print("=" * 55)

    print("\nData IPK sebelum diurutkan:")
    tampilkan_data(data)

    print("\nProses Randomized Quick Sort:")
    hasil = randomized_quick_sort(data, seed, True)

    print("\nHasil akhir (IPK tertinggi ke terendah):")
    tampilkan_data(hasil)

    # Pemeriksaan sederhana: IPK harus tidak menaik
    benar = True
    for i in range(len(hasil) - 1):
        if hasil[i][1] < hasil[i + 1][1]:
            benar = False
            break

    if benar:
        print("\nStatus pengujian: LULUS")
    else:
        print("\nStatus pengujian: GAGAL")

    return hasil


def main():
    # Pengujian 1: data IPK dengan urutan acak
    data_acak = [
        ("Andi", 3.25),
        ("Budi", 3.80),
        ("Citra", 3.45),
        ("Dina", 3.90),
        ("Eko", 3.10),
    ]

    # Pengujian 2: data IPK sudah terurut menurun
    data_terurut = [
        ("Dina", 3.90),
        ("Budi", 3.80),
        ("Citra", 3.45),
        ("Andi", 3.25),
        ("Eko", 3.10),
    ]

    # Pengujian 3: data memiliki IPK duplikat
    data_duplikat = [
        ("Andi", 3.50),
        ("Budi", 3.80),
        ("Citra", 3.50),
        ("Dina", 3.80),
        ("Eko", 3.20),
    ]

    jalankan_pengujian(
        "PENGUJIAN 1: DATA ACAK", data_acak, 42
    )
    jalankan_pengujian(
        "PENGUJIAN 2: DATA SUDAH TERURUT",
        data_terurut, 42
    )
    jalankan_pengujian(
        "PENGUJIAN 3: IPK DUPLIKAT",
        data_duplikat, 42
    )


if __name__ == "__main__":
    main()
