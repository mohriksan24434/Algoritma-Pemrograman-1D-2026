
total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    jam_lembur = int(input("Masukkan jam lembur: "))

    while jam_lembur < 0 or jam_lembur > 8:
        print("Jam lembur tidak valid, maksimal 8 jam")
        jam_lembur = int(input("Masukkan ulang jam lembur: "))

    if jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Apakah shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_harian = 100000 + upah_lembur + tambahan
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)
     
