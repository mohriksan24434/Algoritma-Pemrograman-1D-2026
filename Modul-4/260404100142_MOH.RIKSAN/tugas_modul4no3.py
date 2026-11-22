n = int(input("Masukkan bilangan bulat positif n: "))
jarak = 4  # jumlah spasi pemisah antara dua pola

for i in range(1, n + 1):
    # spasi di kiri supaya pola kiri rata kanan
    for s in range(n - i):
        print(" ", end="")

    # pola kiri: 1 2 3 ... i
    for j in range(1, i + 1):
        print(j, end="")

    # spasi pemisah antara kedua pola
    for s in range(jarak):
        print(" ", end="")

    # pola kanan (cermin): i ... 3 2 1
    for j in range(i, 0, -1):
        print(j, end="")

    print()  # pindah baris 