print("=== Jadwal Shift Asisten Lab ===")

asisten_awal = []
while True:
    nama = input("Nama asisten awal (ketik 'cukup'): ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)
tambahan = input("Nama asisten tambahan: ")
asisten_final = list(asisten_awal) + [tambahan]
hari_list = []
while True:
    hari = input("Nama hari (ketik 'cukup'): ")
    if hari == "cukup":
        break
    hari_list.append(hari)
hari_list = tuple(hari_list)

exc_asisten = input("Asisten pengecualian: ")
exc_hari = input("Hari pengecualian: ")

print("\n--- Jadwal Shift ---")
for a in asisten_final:
    for h in hari_list:
        if a == exc_asisten and h == exc_hari:
            continue
        print(a, "->", h)