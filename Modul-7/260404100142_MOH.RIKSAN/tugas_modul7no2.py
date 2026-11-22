playlist = {}

def tampilkan_menu():
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama_playlist = input("Nama playlist: ")
        if nama_playlist in playlist:
            print("Playlist sudah ada.")
        else:
            playlist[nama_playlist] = {}
            print(f"Playlist '{nama_playlist}' dibuat.")

    elif pilihan == "2":
        nama_playlist = input("Nama playlist: ")
        if nama_playlist in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama_playlist][judul] = penyanyi
            print(f"Lagu '{judul}' ditambahkan ke '{nama_playlist}'.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "3":
        if not playlist:
            print("Belum ada playlist.")
        else:
            for nama_playlist, lagu in playlist.items():
                print(f"\nPlaylist: {nama_playlist}")
                if not lagu:
                    print("  (kosong)")
                else:
                    for judul, penyanyi in lagu.items():
                        print(f"  - {judul} oleh {penyanyi}")

    elif pilihan == "4":
        kata_kunci = input("Cari judul lagu: ").lower()
        ditemukan = False
        for nama_playlist, lagu in playlist.items():
            for judul, penyanyi in lagu.items():
                if kata_kunci in judul.lower():
                    print(f"Ditemukan: '{judul}' oleh {penyanyi} (Playlist: {nama_playlist})")
                    ditemukan = True
        if not ditemukan:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":
        nama_playlist = input("Nama playlist: ")
        if nama_playlist in playlist:
            judul = input("Judul lagu yang dihapus: ")
            if judul in playlist[nama_playlist]:
                del playlist[nama_playlist][judul]
                print(f"Lagu '{judul}' dihapus dari '{nama_playlist}'.")
            else:
                print("Lagu tidak ditemukan di playlist.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "6":
        nama_playlist = input("Nama playlist yang dihapus: ")
        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print(f"Playlist '{nama_playlist}' dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")