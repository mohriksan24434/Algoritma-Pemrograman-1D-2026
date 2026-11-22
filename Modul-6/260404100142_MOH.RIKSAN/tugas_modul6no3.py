def cek_layak(status, ram):
    
    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("=== Inventaris PC ===")
jumlah = int(input("Jumlah PC: "))

data_pc = []

for i in range(jumlah):
    print("\nPC ke-", i+1)
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("RAM (GB): ")
    data_pc.append([nama, status, ram])

print("\n--- Hasil ---")
for pc in data_pc:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]

    try:
    
        hasil = cek_layak(status, ram)
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')