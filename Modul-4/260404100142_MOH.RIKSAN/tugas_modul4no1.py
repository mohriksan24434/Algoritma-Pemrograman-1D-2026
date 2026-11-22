
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for baris in range(1, jumlah_baris + 1):
    print("Baris ke-", baris)

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print("Lampu", lampu, ": Mengalami gangguan")
        else:
            print("Lampu", lampu, ": Berfungsi normal") 

print("Periksa sumber listrik utama taman.")
