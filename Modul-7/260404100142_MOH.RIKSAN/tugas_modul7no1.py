tugas = {}

def tampilkan_menu():
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai & Belum")
    print("6. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama tugas: ")
        if nama in tugas:
            print("Tugas sudah ada.")
        else:
            tugas[nama] = "belum selesai"
            print(f"Tugas '{nama}' ditambahkan.")

    elif pilihan == "2":
        if not tugas:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for nama, status in tugas.items():
                print(f"- {nama}: {status}")

    elif pilihan == "3":
        nama = input("Nama tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "selesai"
            print(f"Tugas '{nama}' ditandai selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Nama tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print(f"Tugas '{nama}' dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = sum(1 for s in tugas.values() if s == "selesai")
        belum = sum(1 for s in tugas.values() if s == "belum selesai")
        print(f"Tugas selesai: {selesai}")
        print(f"Tugas belum selesai: {belum}")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")