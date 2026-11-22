print("=== Pendaftaran Anggota Klub Robotika ===")

nama_list = []

while True:
    nama = input("Masukkan nama: ")
    if nama == "selesai":
        break
    nama_list.append(nama)

print("\n--- Hasil Pengecekan ---")
for nama in nama_list:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "-> nama tidak valid")
    else:
        print(nama, "-> nama valid")

print("\n--- Hapus Penyusup ---")
hapus = input("Masukkan nama yang mau dihapus: ")

if hapus in nama_list:
    nama_list.remove(hapus)
    print(hapus, "sudah dihapus")
else:
    print(hapus, "tidak ada di daftar, program lanjut")

print("\nDaftar akhir:", nama_list)