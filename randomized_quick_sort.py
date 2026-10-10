# ==========================================
# RANDOMIZED QUICK SORT - IPK MAHASISWA
# Pengurutan: IPK tertinggi ke terendah
# ==========================================

# Data mahasiswa
mahasiswa = [
    ["Mahasiswa A", 3.25],
    ["Mahasiswa B", 2.85],
    ["Mahasiswa C", 3.75],
    ["Mahasiswa D", 3.10],
    ["Mahasiswa E", 3.90],
    ["Mahasiswa F", 2.70],
    ["Mahasiswa G", 3.50],
    ["Mahasiswa H", 3.00]
]

# Seed awal untuk generator pseudo-random
seed = 12345


# ==========================================
# GENERATOR PSEUDO-RANDOM
# ==========================================

def random_number():
    global seed

    # Linear Congruential Generator (LCG)
    seed = (1103515245 * seed + 12345) % (2 ** 31)

    return seed


# ==========================================
# RANDOMIZED QUICK SORT
# ==========================================

def randomized_quick_sort(data, low, high, level=0):

    # Kondisi berhenti rekursi
    if low >= high:
        return

    # Menghasilkan angka pseudo-random
    angka_random = random_number()

    # Menentukan posisi pivot secara acak
    pivot_index = low + (angka_random % (high - low + 1))

    # Menyimpan informasi pivot
    pivot_value = data[pivot_index][1]

    print("\n" + "=" * 60)
    print("LEVEL REKURSI :", level)
    print("SEED          :", seed)
    print("ANGKA RANDOM  :", angka_random)
    print("POSISI PIVOT  :", pivot_index)
    print("NILAI PIVOT   :", pivot_value)

    # Memindahkan pivot ke posisi paling kanan
    data[pivot_index], data[high] = data[high], data[pivot_index]

    # Proses partisi
    i = low

    for j in range(low, high):

        # Karena ingin urutan menurun:
        # IPK lebih besar ditempatkan di sebelah kiri pivot
        if data[j][1] > pivot_value:

            data[i], data[j] = data[j], data[i]
            i += 1

    # Menempatkan pivot pada posisi akhirnya
    data[i], data[high] = data[high], data[i]

    # Menampilkan hasil pembagian
    print("\nPembagian data:")

    print("Bagian KIRI  :", end=" ")
    if low <= i - 1:
        for k in range(low, i):
            print(data[k][1], end=" ")
    else:
        print("kosong", end="")

    print()

    print("PIVOT        :", data[i][0], "-", data[i][1])

    print("Bagian KANAN :", end=" ")
    if i + 1 <= high:
        for k in range(i + 1, high + 1):
            print(data[k][1], end=" ")
    else:
        print("kosong", end="")

    print()

    # Rekursi bagian kiri
    randomized_quick_sort(data, low, i - 1, level + 1)

    # Rekursi bagian kanan
    randomized_quick_sort(data, i + 1, high, level + 1)


# ==========================================
# PROGRAM UTAMA
# ==========================================

print("=" * 60)
print("DATA IPK SEBELUM DIURUTKAN")
print("=" * 60)

for mahasiswa_data in mahasiswa:
    print(mahasiswa_data[0], ":", mahasiswa_data[1])


# Menjalankan Randomized Quick Sort
randomized_quick_sort(mahasiswa, 0, len(mahasiswa) - 1)


# ==========================================
# HASIL AKHIR
# ==========================================

print("\n" + "=" * 60)
print("HASIL AKHIR PENGURUTAN IPK")
print("DARI TERTINGGI KE TERENDAH")
print("=" * 60)

for mahasiswa_data in mahasiswa:
    print(mahasiswa_data[0], ":", mahasiswa_data[1])