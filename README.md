# Randomized Quick Sort untuk Mengurutkan IPK Mahasiswa

## Tentang Program

Program ini dibuat untuk memenuhi tugas mata kuliah Analisis Algoritma Komputasi. Saya menggunakan algoritma Randomized Quick Sort untuk mengurutkan nilai IPK mahasiswa dari yang tertinggi sampai terendah menggunakan bahasa pemrograman Python.

Saya membuat program ini supaya bisa memahami cara kerja Randomized Quick Sort secara langsung, mulai dari pemilihan pivot, pembagian data, pertukaran posisi, sampai proses pengurutan selesai. Dalam program utama, saya tidak menggunakan fungsi bawaan Python seperti `sort()` atau `sorted()` untuk mengurutkan data.

## Tujuan

Tujuan dari program ini adalah untuk mempelajari cara kerja Randomized Quick Sort dan melihat bagaimana algoritma tersebut mengurutkan data IPK mahasiswa. Selain itu, saya juga melakukan pengujian untuk memastikan hasil pengurutan sudah benar.

## Pengujian Program

Pada program utama, saya menggunakan tiga jenis pengujian:

1. **Data acak**, yaitu data IPK yang belum tersusun dari nilai tertinggi ke terendah.
2. **Data yang sudah terurut**, yaitu data IPK yang sebelumnya sudah tersusun menurun.
3. **Data dengan IPK yang sama**, yaitu pengujian untuk melihat apakah program tetap bisa mengurutkan data yang memiliki nilai duplikat.

Selain pengujian tersebut, saya juga membuat program eksperimen untuk membandingkan waktu eksekusi Randomized Quick Sort dengan Merge Sort.

## Eksperimen

Pengujian kinerja dilakukan menggunakan data IPK sintetis dengan lima ukuran data, yaitu 100, 500, 1.000, 5.000, dan 10.000 data. Setiap ukuran diuji sebanyak lima kali.

Hasil pengujian digunakan untuk melihat waktu eksekusi kedua algoritma dan memeriksa apakah hasil pengurutannya sama serta sudah tersusun dari nilai tertinggi ke terendah.

## File dalam Repository

- `randomized_quick_sort_fix.py` — program utama untuk mengurutkan IPK mahasiswa dan menjalankan tiga pengujian.
- `eksperimen_acak_pengurutan_cepat_FIX_LOKASI_CSV.py` — program eksperimen untuk membandingkan Randomized Quick Sort dengan Merge Sort.
- `hasil_eksperimen.csv` — file untuk menyimpan hasil pengujian kinerja algoritma.

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer. Setelah itu, buka folder program menggunakan Visual Studio Code dan jalankan file yang ingin diuji melalui terminal.

Untuk program utama:

```bash
python randomized_quick_sort_fix.py
```

Untuk program eksperimen:

```bash
python eksperimen_acak_pengurutan_cepat_FIX_LOKASI_CSV.py
```

Setelah program eksperimen dijalankan, hasil pengujian akan disimpan dalam file CSV sesuai pengaturan pada program.

## Penutup

Melalui tugas ini, saya mempelajari bagaimana Randomized Quick Sort bekerja dalam mengurutkan data IPK mahasiswa. Saya juga dapat melihat perbedaan waktu eksekusi antara Randomized Quick Sort dan Merge Sort melalui pengujian dengan beberapa ukuran data. Hasilnya menjadi bahan untuk memahami hubungan antara teori algoritma dan hasil pengujian secara langsung.
