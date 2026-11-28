
daftar_kamera = {
    "CANON EOS M10": (130000, 100000, 50000),
    "SONY A7 III": (200000, 150000, 100000),
    "FUJIFILM X-A3": (150000, 120000, 70000),
    "FUJIFILM X-M5": (250000, 200000, 150000)
}

stok_kamera = {
    "CANON EOS M10": 3,
    "SONY A7 III": 2,
    "FUJIFILM X-A3": 2,
    "FUJIFILM X-M5": 1
}

daftar_fotografi = {
    "PAKET WISUDA": 300000,
    "PAKET PREWEDDING": 750000,
    "PAKET EVENT": 500000,
    "PAKET PRODUK": 250000
}

daftar_pesanan = []


def menu_awal():
    print("-------------------------------")
    print("SISTEM PENYEWAAN KAMERA")
    print("1. user")
    print("2. admin")
    print("3. keluar")
    try:
        return int(input("pilih akses: "))
    except ValueError:
        print("MASUKKAN ANGKA YANG ADA DI URUTAN!")
        return 0


def menu_user():
    print("-------------------------------")
    print("MENU USER")
    print("1. penyewaan kamera")
    print("2. jasa fotografi")
    print("3. cek status pesanan")
    print("4. batalkan pesanan")
    print("5. selesai")
    try:
        return int(input("pilih menu: "))
    except ValueError:
        print("MASUKKAN ANGKA!")
        return 0


def login_admin():
    pw_admin = "iniPunyaAdmin1927"
    while True:
        pw = input("masukkan password admin: ")
        if pw == pw_admin:
            print("LOGIN BERHASIL!")
            return True
        print("PASSWORD SALAH!")
        ulang = input("coba lagi? (ya/tidak): ").lower().strip()
        if ulang != "ya":
            return False

# KELOLA KAMERA
def lihat_kamera():
    print("DAFTAR KAMERA")
    if not daftar_kamera:
        print("BELUM ADA KAMERA!")
        return
    for nama, harga in daftar_kamera.items():
        print("-------------------------------")
        print("Nama kamera:", nama)
        print("Harga per hari: Rp", harga[0])
        print("Harga 12 jam: Rp", harga[1])
        print("Harga 6 jam: Rp", harga[2])
        print("Stok:", stok_kamera.get(nama, 0))
        print("-------------------------------")


def tambah_kamera():
    print("MENU TAMBAH KAMERA")
    nama = input("masukkan nama kamera: ").strip().upper()
    if not nama:
        print("NAMA KAMERA TIDAK BOLEH KOSONG!")
        return
    if nama in daftar_kamera:
        print("KAMERA SUDAH TERDAFTAR!")
        return
    try:
        harian = int(input("harga sewa per hari: "))
        dua_belas = int(input("harga sewa 12 jam: "))
        enam = int(input("harga sewa 6 jam: "))
        stok = int(input("jumlah stok kamera: "))
    except ValueError:
        print("HARGA DAN STOK HARUS BERUPA ANGKA!")
        return
    if min(harian, dua_belas, enam, stok) <= 0:
        print("HARGA DAN STOK HARUS LEBIH DARI 0!")
        return
    if input("yakin menambahkan kamera? (ya/tidak): ").lower().strip() == "ya":
        daftar_kamera[nama] = (harian, dua_belas, enam)
        stok_kamera[nama] = stok
        print("KAMERA BERHASIL DITAMBAHKAN!")
    else:
        print("PENAMBAHAN DIBATALKAN!")


def ubah_harga_kamera():
    lihat_kamera()
    nama = input("nama kamera yang ingin diubah: ").strip().upper()
    if nama not in daftar_kamera:
        print("KAMERA TIDAK DITEMUKAN!")
        return
    try:
        harian = int(input("harga sewa per hari yang baru: "))
        dua_belas = int(input("harga sewa 12 jam yang baru: "))
        enam = int(input("harga sewa 6 jam yang baru: "))
    except ValueError:
        print("HARGA HARUS BERUPA ANGKA!")
        return
    if min(harian, dua_belas, enam) <= 0:
        print("HARGA HARUS LEBIH DARI 0!")
        return
    daftar_kamera[nama] = (harian, dua_belas, enam)
    print("HARGA KAMERA BERHASIL DIUBAH!")


def hapus_kamera():
    lihat_kamera()
    nama = input("nama kamera yang ingin dihapus: ").strip().upper()
    if nama not in daftar_kamera:
        print("KAMERA TIDAK DITEMUKAN!")
        return
    for data in daftar_pesanan:
        if (data["jenis"] == "sewa kamera" and data["kamera"] == nama
                and data.get("status_pengembalian") == "belum dikembalikan"):
            print("KAMERA MASIH DIGUNAKAN DALAM PESANAN!")
            return
    if input("yakin menghapus kamera ini? (ya/tidak): ").lower().strip() == "ya":
        del daftar_kamera[nama]
        del stok_kamera[nama]
        print("KAMERA BERHASIL DIHAPUS!")
        lihat_kamera()
    else:
        print("PENGHAPUSAN DIBATALKAN!")


def menu_kelola_kamera():
    while True:
        print("-------------------------------")
        print("MENU KELOLA SEWA KAMERA")
        print("1. lihat daftar kamera")
        print("2. tambah kamera")
        print("3. ubah harga kamera")
        print("4. hapus kamera")
        print("5. kembali")
        try:
            pilihan = int(input("pilih menu: "))
        except ValueError:
            print("MASUKKAN ANGKA!")
            continue
        if pilihan == 1:
            lihat_kamera()
        elif pilihan == 2:
            tambah_kamera()
        elif pilihan == 3:
            ubah_harga_kamera()
        elif pilihan == 4:
            hapus_kamera()
        elif pilihan == 5:
            break
        else:
            print("PILIHAN MENU TIDAK TERSEDIA!")

# KELOLA JASA FOTOGRAFI
def lihat_fotografi():
    print("DAFTAR PAKET FOTOGRAFI")
    if not daftar_fotografi:
        print("BELUM ADA PAKET FOTOGRAFI!")
        return
    for nama, harga in daftar_fotografi.items():
        print("-------------------------------")
        print("nama paket:", nama)
        print("harga paket: Rp", harga)
        print("-------------------------------")


def tambah_fotografi():
    nama = input("masukkan nama paket fotografi: ").strip().upper()
    if not nama:
        print("NAMA PAKET TIDAK BOLEH KOSONG!")
        return
    if nama in daftar_fotografi:
        print("PAKET SUDAH TERDAFTAR!")
        return
    try:
        harga = int(input("masukkan harga paket: "))
    except ValueError:
        print("HARGA HARUS BERUPA ANGKA!")
        return
    if harga <= 0:
        print("HARGA HARUS LEBIH DARI 0!")
        return
    if input("yakin menambahkan paket? (ya/tidak): ").lower().strip() == "ya":
        daftar_fotografi[nama] = harga
        print("PAKET BERHASIL DITAMBAHKAN!")
    else:
        print("PENAMBAHAN DIBATALKAN!")


def ubah_harga_fotografi():
    lihat_fotografi()
    nama = input("nama paket yang ingin diubah: ").strip().upper()
    if nama not in daftar_fotografi:
        print("PAKET TIDAK DITEMUKAN!")
        return
    try:
        harga = int(input("masukkan harga baru: "))
    except ValueError:
        print("HARGA HARUS BERUPA ANGKA!")
        return
    if harga <= 0:
        print("HARGA HARUS LEBIH DARI 0!")
        return
    daftar_fotografi[nama] = harga
    print("HARGA PAKET BERHASIL DIUBAH!")


def hapus_fotografi():
    lihat_fotografi()
    nama = input("nama paket yang ingin dihapus: ").strip().upper()
    if nama not in daftar_fotografi:
        print("PAKET TIDAK DITEMUKAN!")
        return
    if input("yakin menghapus paket ini? (ya/tidak): ").lower().strip() == "ya":
        del daftar_fotografi[nama]
        print("PAKET BERHASIL DIHAPUS!")
        lihat_fotografi()
    else:
        print("PENGHAPUSAN DIBATALKAN!")


def menu_kelola_fotografi():
    while True:
        print("-------------------------------")
        print("MENU KELOLA JASA FOTOGRAFI")
        print("1. lihat paket fotografi")
        print("2. tambah paket fotografi")
        print("3. bah harga paket")
        print("4. hapus paket fotografi")
        print("5. kembali")
        print("-------------------------------")
        try:
            pilihan = int(input("pilih menu: "))
        except ValueError:
            print("MASUKKAN ANGKA!")
            continue
        if pilihan == 1:
            lihat_fotografi()
        elif pilihan == 2:
            tambah_fotografi()
        elif pilihan == 3:
            ubah_harga_fotografi()
        elif pilihan == 4:
            hapus_fotografi()
        elif pilihan == 5:
            break
        else:
            print("PILIHAN MENU TIDAK TERSEDIA!")


# ID PELANGGAN
def cari_atau_buat_id_pelanggan(telpon):
    for data in daftar_pesanan:
        if data.get("telpon") == telpon and data.get("id_pelanggan"):
            return data["id_pelanggan"]

    nomor_terbesar = 0
    for data in daftar_pesanan:
        id_lama = data.get("id_pelanggan", "")
        if id_lama.startswith("PLG") and id_lama[3:].isdigit():
            nomor_terbesar = max(nomor_terbesar, int(id_lama[3:]))

    return "PLG" + str(nomor_terbesar + 1).zfill(3)


# BUKTI PESANAN DAN PESANAN USER
def bukti_penyewaan(data):
    print("-------------------------------")
    print("BUKTI PENYEWAAN KAMERA")
    print("ID pelanggan:", data["id_pelanggan"])
    print("nama penyewa:", data["nama"])
    print("No. telepon:", data["telpon"])
    print("tanggal penyewaan:", data["tanggal_sewa"])
    print("tanggal pengembalian:", data["tanggal_kembali"])
    print("jaminan:", data["jaminan"])
    print("DAFTAR KAMERA:")
    for item in data.get("rincian_kamera", []):
        print("-", item["nama"], "|", item["durasi"], "| Rp", item["harga"])
    print("Total pembayaran: Rp", data["total_harga"])
    print("Metode pembayaran:", data["pembayaran"])
    print("-------------------------------")


def kamera():
    from datetime import datetime, timedelta

    print("MENU PENYEWAAN KAMERA")
    if not daftar_kamera:
        print("BELUM ADA KAMERA!")
        return

    pilihan_kamera = []
    while True:
        kamera_tersedia = list(daftar_kamera.keys())
        print("DAFTAR KAMERA")
        for i, nama_kamera in enumerate(kamera_tersedia, 1):
            sisa_stok = stok_kamera.get(nama_kamera, 0) - pilihan_kamera.count(nama_kamera)
            print(i, nama_kamera, "- Stok tersedia:", max(0, sisa_stok))
        print("Ketik b untuk membatalkan pemesanan.")
        try:
            pilihan = input("pilih nomor kamera: ").strip()
            if pilihan.lower() == "b":
                print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
                return
            pilihan = int(pilihan)
        except ValueError:
            print("INPUT SALAH! SILAKAN PILIH NOMOR KAMERA YANG TERSEDIA.")
            continue

        if pilihan < 1 or pilihan > len(kamera_tersedia):
            print("INPUT SALAH! SILAKAN PILIH NOMOR KAMERA YANG TERSEDIA.")
            continue

        nama_pilihan = kamera_tersedia[pilihan - 1]
        if pilihan_kamera.count(nama_pilihan) >= stok_kamera.get(nama_pilihan, 0):
            print("STOK KAMERA TERSEBUT TIDAK MENCUKUPI!")
            continue

        print("-------------------------------")
        print("DETAIL HARGA DAN DURASI KAMERA")
        print("Nama kamera:", nama_pilihan)
        print("1. Per hari : Rp", daftar_kamera[nama_pilihan][0])
        print("2. 12 jam   : Rp", daftar_kamera[nama_pilihan][1])
        print("3. 6 jam    : Rp", daftar_kamera[nama_pilihan][2])
        print("-------------------------------")

        while True:
            lanjut_sewa = input("Tetap lanjut menyewa kamera ini? (ya/tidak): ").lower().strip()
            if lanjut_sewa == "ya":
                pilihan_kamera.append(nama_pilihan)
                print(nama_pilihan, "BERHASIL DITAMBAHKAN!")
                break
            elif lanjut_sewa == "tidak":
                print("KAMERA TIDAK JADI DIPILIH. KEMBALI KE DAFTAR KAMERA.")
                break
            print("MASUKKAN YA ATAU TIDAK!")

        if lanjut_sewa == "tidak":
            continue

        while True:
            lagi = input("ingin menambah kamera lain? (ya/tidak): ").lower().strip()
            if lagi == "ya":
                break
            elif lagi == "tidak":
                break
            print("MASUKKAN YA ATAU TIDAK!")
        if lagi == "tidak":
            break

    while True:
        nama = input("masukkan nama penyewa (atau b untuk batal): ").strip()
        if nama.lower() == "b":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        if nama:
            break
        print("NAMA TIDAK BOLEH KOSONG!")

    while True:
        telpon = input("masukkan nomor telepon aktif (12 digit, atau b untuk batal): ").strip()
        if telpon.lower() == "b":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        if telpon.isdigit() and len(telpon) == 12:
            break
        print("NOMOR TELEPON HARUS TERDIRI DARI 12 DIGIT ANGKA!")

    while True:
        jaminan = input("masukkan jaminan (KK/KTP/KTM/SIM, atau b untuk batal): ").strip().upper()
        if jaminan == " ":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        if jaminan in ["KK", "KTP", "KTM", "SIM"]:
            break
        print("JAMINAN HARUS KK, KTP, KTM, ATAU SIM!")

    print("-------------------------------")
    print("PILIH DURASI UNTUK SEMUA KAMERA")
    print("1. per hari")
    print("2. 12 jam")
    print("3. 6 jam")
    print("-------------------------------")

    while True:
        try:
            durasi = int(input("pilih durasi (atau ketik b untuk batal): ").strip().lower()
                          .replace("b", "-999"))
        except ValueError:
            print("INPUT SALAH! PILIH DURASI 1, 2, ATAU 3.")
            continue
        if durasi == -999:
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        if durasi in [1, 2, 3]:
            break
        print("INPUT SALAH! PILIH DURASI 1, 2, ATAU 3.")

    jumlah_hari = 1
    if durasi == 1:
        while True:
            masukan_hari = input("mau menyewa berapa hari? (atau b untuk batal): ").strip()
            if masukan_hari.lower() == "b":
                print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
                return
            try:
                jumlah_hari = int(masukan_hari)
                if jumlah_hari > 0:
                    break
                print("JUMLAH HARI HARUS LEBIH DARI 0!")
            except ValueError:
                print("JUMLAH HARI HARUS BERUPA ANGKA!")
        keterangan_durasi = str(jumlah_hari) + " hari"
        lama_sewa = timedelta(days=jumlah_hari)
        indeks_harga = 0
    elif durasi == 2:
        keterangan_durasi, lama_sewa, indeks_harga = "12 jam", timedelta(hours=12), 1
    else:
        keterangan_durasi, lama_sewa, indeks_harga = "6 jam", timedelta(hours=6), 2

    rincian_kamera = []
    for nama_kamera in pilihan_kamera:
        rincian_kamera.append({
            "nama": nama_kamera,
            "durasi": keterangan_durasi,
            "harga": daftar_kamera[nama_kamera][indeks_harga] * (jumlah_hari if durasi == 1 else 1)
        })
    total_harga = sum(item["harga"] for item in rincian_kamera)

    while True:
        masukan_tanggal = input("tanggal penyewaan (DD-MM-YYYY, atau b untuk batal): ").strip()
        if masukan_tanggal.lower() == "b":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        try:
            tanggal_mulai = datetime.strptime(masukan_tanggal, "%d-%m-%Y")
            break
        except ValueError:
            print("TANGGAL TIDAK VALID! GUNAKAN FORMAT DD-MM-YYYY!")

    while True:
        masukan_waktu = input("waktu penyewaan (JJ:MM, atau b untuk batal): ").strip()
        if masukan_waktu.lower() == "b":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        try:
            waktu_mulai = datetime.strptime(masukan_waktu, "%H:%M").time()
            break
        except ValueError:
            print("WAKTU TIDAK VALID! GUNAKAN FORMAT JJ:MM!")

    mulai = datetime.combine(tanggal_mulai.date(), waktu_mulai)
    selesai = mulai + lama_sewa
    tanggal_sewa = mulai.strftime("%d-%m-%Y %H:%M")
    tanggal_kembali = selesai.strftime("%d-%m-%Y %H:%M")

    print("-------------------------------")    
    print("METODE PEMBAYARAN")
    print("1. transfer")
    print("2. tunai")
    print("-------------------------------")
    while True:
        masukan_bayar = input("pilih metode pembayaran (atau b untuk batal): ").strip().lower()
        if masukan_bayar == "b":
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            return
        if masukan_bayar == "1":
            metode = "transfer"
            break
        elif masukan_bayar == "2":
            metode = "tunai"
            break
        print("INPUT SALAH! PILIH 1 UNTUK TRANSFER ATAU 2 UNTUK TUNAI.")

    id_pelanggan = cari_atau_buat_id_pelanggan(telpon)
    data_pesanan = {
        "id_pelanggan": id_pelanggan,
        "jenis": "sewa kamera", "nama": nama, "telpon": telpon,
        "jaminan": jaminan, "tanggal_sewa": tanggal_sewa,
        "tanggal_kembali": tanggal_kembali, "kamera": pilihan_kamera,
        "rincian_kamera": rincian_kamera, "durasi": keterangan_durasi,
        "total_harga": total_harga, "pembayaran": metode,
        "status": "menunggu validasi", "status_pengembalian": "belum dikembalikan",
        "tanggal_pengembalian_aktual": "-", "denda": 0,
        "denda_dibayar": 0, "kondisi_kamera": "belum diperiksa"
    }

    while True:
        print("-------------------------------")
        bukti_penyewaan(data_pesanan)
        print("APAKAH DATA SUDAH BENAR?")
        print("1. ya, lanjutkan pemesanan")
        print("2. tidak, perbaiki data")
        print("3. batalkan pesanan dan kembali ke Menu User")
        print("-------------------------------")
        try:
            konfirmasi = int(input("Pilih menu: "))
        except ValueError:
            print("INPUT SALAH! MASUKKAN ANGKA 1, 2, ATAU 3.")
            continue

        if konfirmasi == 1:
            daftar_pesanan.append(data_pesanan)
            print("PESANAN BERHASIL DISIMPAN! STATUS: MENUNGGU VALIDASI ADMIN.")
            break
        elif konfirmasi == 3:
            print("PEMESANAN DIBATALKAN! KEMBALI KE MENU USER.")
            break
        elif konfirmasi == 2:
            while True:
                print("-------------------------------")
                print("DATA YANG INGIN DIPERBAIKI")
                print("1. nama penyewa")
                print("2. nomor telepon")
                print("3. jaminan")
                print("4. daftar kamera")
                print("5. durasi penyewaan")
                print("6. danggal dan waktu penyewaan")
                print("7. metode pembayaran")
                print("8. kembali ke konfirmasi")
                print("-------------------------------")
                try:
                    ubah = int(input("pilih data yang ingin diperbaiki: "))
                except ValueError:
                    print("INPUT SALAH! MASUKKAN ANGKA 1 SAMPAI 8.")
                    continue

                if ubah == 1:
                    while True:
                        nama_baru = input("masukkan nama penyewa yang benar: ").strip()
                        if nama_baru:
                            data_pesanan["nama"] = nama_baru
                            break
                        print("NAMA TIDAK BOLEH KOSONG!")
                elif ubah == 2:
                    while True:
                        telpon_baru = input("masukkan nomor telepon yang benar (12 digit): ").strip()
                        if telpon_baru.isdigit() and len(telpon_baru) == 12:
                            data_pesanan["telpon"] = telpon_baru
                            break
                        print("NOMOR TELEPON HARUS TERDIRI DARI 12 DIGIT ANGKA!")
                elif ubah == 3:
                    while True:
                        jaminan_baru = input("masukkan jaminan (KK/KTP/KTM/SIM): ").strip().upper()
                        if jaminan_baru in ["KK", "KTP", "KTM", "SIM"]:
                            data_pesanan["jaminan"] = jaminan_baru
                            break
                        print("JAMINAN HARUS KK, KTP, KTM, ATAU SIM!")
                elif ubah == 4:
                    pilihan_baru = []
                    while True:
                        kamera_tersedia = list(daftar_kamera.keys())
                        print("DAFTAR KAMERA")
                        for nomor, nama_kamera in enumerate(kamera_tersedia, 1):
                            sisa = stok_kamera.get(nama_kamera, 0) - pilihan_baru.count(nama_kamera)
                            print(nomor, nama_kamera, "- stok tersedia:", max(0, sisa))
                        print("Ketik b untuk membatalkan perubahan daftar kamera.")
                        masukan = input("pilih nomor kamera: ").strip()
                        if masukan.lower() == "b":
                            print("PERUBAHAN DAFTAR KAMERA DIBATALKAN.")
                            pilihan_baru = None
                            break
                        try:
                            nomor = int(masukan)
                        except ValueError:
                            print("INPUT SALAH! PILIH NOMOR KAMERA YANG TERSEDIA.")
                            continue
                        if nomor < 1 or nomor > len(kamera_tersedia):
                            print("INPUT SALAH! PILIH NOMOR KAMERA YANG TERSEDIA.")
                            continue
                        nama_pilihan = kamera_tersedia[nomor - 1]
                        if pilihan_baru.count(nama_pilihan) >= stok_kamera.get(nama_pilihan, 0):
                            print("STOK KAMERA TIDAK MENCUKUPI!")
                            continue
                        pilihan_baru.append(nama_pilihan)
                        print(nama_pilihan, "BERHASIL DIPILIH!")
                        while True:
                            lagi = input("ingin menambah kamera lain? (ya/tidak): ").lower().strip()
                            if lagi in ["ya", "tidak"]:
                                break
                            print("MASUKKAN YA ATAU TIDAK!")
                        if lagi == "tidak":
                            break
                    if pilihan_baru:
                        pilihan_kamera = pilihan_baru
                        data_pesanan["kamera"] = pilihan_kamera
                        rincian_kamera = []
                        for nama_kamera in pilihan_kamera:
                            faktor_hari = jumlah_hari if durasi == 1 else 1
                            rincian_kamera.append({
                                "nama": nama_kamera,
                                "durasi": keterangan_durasi,
                                "harga": daftar_kamera[nama_kamera][indeks_harga] * faktor_hari
                            })
                        data_pesanan["rincian_kamera"] = rincian_kamera
                        data_pesanan["total_harga"] = sum(item["harga"] for item in rincian_kamera)
                elif ubah == 5:
                    print("-------------------------------")
                    print("1. per hari")
                    print("2. 12 jam")
                    print("3. 6 jam")
                    print("-------------------------------")
                    while True:
                        masukan_durasi = input("pilih durasi baru: ").strip()
                        if masukan_durasi in ["1", "2", "3"]:
                            durasi = int(masukan_durasi)
                            break
                        print("INPUT SALAH! PILIH DURASI 1, 2, ATAU 3.")
                    if durasi == 1:
                        while True:
                            try:
                                jumlah_hari = int(input("mau menyewa berapa hari? "))
                                if jumlah_hari > 0:
                                    break
                                print("JUMLAH HARI HARUS LEBIH DARI 0!")
                            except ValueError:
                                print("JUMLAH HARI HARUS BERUPA ANGKA!")
                        keterangan_durasi = str(jumlah_hari) + " hari"
                        lama_sewa = timedelta(days=jumlah_hari)
                        indeks_harga = 0
                    elif durasi == 2:
                        keterangan_durasi, lama_sewa, indeks_harga = "12 jam", timedelta(hours=12), 1
                    else:
                        keterangan_durasi, lama_sewa, indeks_harga = "6 jam", timedelta(hours=6), 2
                    rincian_kamera = []
                    for nama_kamera in data_pesanan["kamera"]:
                        faktor_hari = jumlah_hari if durasi == 1 else 1
                        rincian_kamera.append({
                            "nama": nama_kamera,
                            "durasi": keterangan_durasi,
                            "harga": daftar_kamera[nama_kamera][indeks_harga] * faktor_hari
                        })
                    data_pesanan["durasi"] = keterangan_durasi
                    data_pesanan["rincian_kamera"] = rincian_kamera
                    data_pesanan["total_harga"] = sum(item["harga"] for item in rincian_kamera)
                    mulai_lama = datetime.strptime(data_pesanan["tanggal_sewa"], "%d-%m-%Y %H:%M")
                    data_pesanan["tanggal_kembali"] = (mulai_lama + lama_sewa).strftime("%d-%m-%Y %H:%M")
                elif ubah == 6:
                    while True:
                        try:
                            tanggal_baru = datetime.strptime(
                                input("tanggal penyewaan yang benar (DD-MM-YYYY): ").strip(), "%d-%m-%Y"
                            )
                            waktu_baru = datetime.strptime(
                                input("waktu penyewaan yang benar (JJ:MM): ").strip(), "%H:%M"
                            ).time()
                            mulai_baru = datetime.combine(tanggal_baru.date(), waktu_baru)
                            selesai_baru = mulai_baru + lama_sewa
                            data_pesanan["tanggal_sewa"] = mulai_baru.strftime("%d-%m-%Y %H:%M")
                            data_pesanan["tanggal_kembali"] = selesai_baru.strftime("%d-%m-%Y %H:%M")
                            break
                        except ValueError:
                            print("TANGGAL ATAU WAKTU TIDAK VALID! COBA LAGI.")
                elif ubah == 7:
                    while True:
                        print("-------------------------------")
                        print("1. transfer")
                        print("2. tunai")
                        print("-------------------------------")
                        metode_baru = input("pilih metode pembayaran: ").strip()
                        if metode_baru == "1":
                            data_pesanan["pembayaran"] = "transfer"
                            break
                        elif metode_baru == "2":
                            data_pesanan["pembayaran"] = "tunai"
                            break
                        print("INPUT SALAH! PILIH 1 ATAU 2.")
                elif ubah == 8:
                    break
                else:
                    print("PILIHAN TIDAK TERSEDIA!")
        else:
            print("INPUT SALAH! PILIH 1, 2, ATAU 3.")

def bukti_fotografi(data):
    print("=========================================")
    print("BUKTI PEMESANAN JASA FOTOGRAFI")
    print("ID pelanggan:", data["id_pelanggan"])
    print("Nama pemesan:", data["nama"])
    print("No. telepon:", data["telpon"])
    print("Paket:", data["paket"])
    print("Tanggal pemotretan:", data["tanggal"])
    print("Lokasi:", data["lokasi"])
    print("Total pembayaran: Rp", data["total_harga"])
    print("Metode pembayaran:", data["pembayaran"])
    print("Status: MENUNGGU VALIDASI ADMIN")
    print("=========================================")


def jasa_fotografi():
    from datetime import datetime
    while True:
        paket_tersedia = list(daftar_fotografi.keys())
        if not paket_tersedia:
            print("BELUM ADA PAKET FOTOGRAFI!")
            return

        print("DAFTAR PAKET FOTOGRAFI")
        for nomor, nama_paket in enumerate(paket_tersedia, 1):
            print(nomor, ".", nama_paket, "- Harga: Rp", daftar_fotografi[nama_paket])

        try:
            pilihan = int(input("Pilih paket sesuai nomor: "))
        except ValueError:
            print("INPUT SALAH! MASUKKAN NOMOR PAKET YANG TERSEDIA.")
            continue
        if pilihan < 1 or pilihan > len(paket_tersedia):
            print("INPUT SALAH! NOMOR PAKET TIDAK TERSEDIA.")
            continue
        nama_paket = paket_tersedia[pilihan - 1]
        harga = daftar_fotografi[nama_paket]
        break

    while True:
        nama = input("masukkan nama pemesan: ").strip()
        if nama:
            break
        print("NAMA TIDAK BOLEH KOSONG!")
    while True:
        telpon = input("masukkan nomor telepon aktif (12 digit): ").strip()
        if telpon.isdigit() and len(telpon) == 12:
            break
        print("NOMOR TELEPON HARUS TERDIRI DARI 12 DIGIT ANGKA!")
    while True:
        try:
            tanggal = datetime.strptime(
                input("tanggal pemotretan (DD-MM-YYYY): ").strip(), "%d-%m-%Y"
            ).strftime("%d-%m-%Y")
            break
        except ValueError:
            print("TANGGAL TIDAK VALID! GUNAKAN FORMAT DD-MM-YYYY!")
    while True:
        lokasi = input("masukkan lokasi pemotretan: ").strip()
        if lokasi:
            break
        print("LOKASI TIDAK BOLEH KOSONG!")

    while True:
        print("-------------------------------")
        print("1. transfer")
        print("2. tunai")
        print("-------------------------------")
        try:
            bayar = int(input("pilih metode pembayaran: "))
        except ValueError:
            print("MASUKKAN ANGKA!")
            continue
        if bayar == 1:
            metode = "transfer"
            break
        if bayar == 2:
            metode = "tunai"
            break
        print("METODE PEMBAYARAN TIDAK TERSEDIA!")

    id_pelanggan = cari_atau_buat_id_pelanggan(telpon)
    data_pesanan = {
        "id_pelanggan": id_pelanggan,
        "jenis": "jasa fotografi", "nama": nama, "telpon": telpon,
        "tanggal": tanggal, "lokasi": lokasi, "paket": nama_paket,
        "total_harga": harga, "pembayaran": metode,
        "status": "menunggu validasi"
    }
    while True:
        bukti_fotografi(data_pesanan)
        print("APAKAH INGIN MELANJUTKAN PEMESANAN?")
        print("1. ya, lanjutkan pemesanan")
        print("2. tidak, perbaiki data")
        print("3. tidak jadi memesan, batalkan pesanan")
        try:
            konfirmasi = int(input("pilih menu: "))
        except ValueError:
            print("MASUKKAN ANGKA 1, 2, ATAU 3!")
            continue

        if konfirmasi == 1:
            daftar_pesanan.append(data_pesanan)
            print("PESANAN JASA FOTOGRAFI BERHASIL DISIMPAN! STATUS: MENUNGGU VALIDASI ADMIN.")
            break
        elif konfirmasi == 3:
            print("PESANAN DIBATALKAN!")
            break
        elif konfirmasi == 2:
            print("-------------------------------")
            print("DATA YANG INGIN DIPERBAIKI")
            print("1. nama pemesan")
            print("2. omor telepon")
            print("3. tanggal pemotretan")
            print("4. lokasi pemotretan")
            print("5. paket fotografi")
            print("6. metode pembayaran")
            print("7. kembali ke konfirmasi")
            print("-------------------------------")
            try:
                ubah = int(input("pilih data yang ingin diperbaiki: "))
            except ValueError:
                print("MASUKKAN ANGKA!")
                continue

            if ubah == 1:
                while True:
                    nama_baru = input("masukkan nama pemesan yang benar: ").strip()
                    if nama_baru:
                        data_pesanan["nama"] = nama_baru
                        break
                    print("NAMA TIDAK BOLEH KOSONG!")
            elif ubah == 2:
                while True:
                    telpon_baru = input("masukkan nomor telepon yang benar (12 digit): ").strip()
                    if telpon_baru.isdigit() and len(telpon_baru) == 12:
                        data_pesanan["telpon"] = telpon_baru
                        break
                    print("NOMOR TELEPON HARUS TERDIRI DARI 12 DIGIT ANGKA!")
            elif ubah == 3:
                while True:
                    try:
                        tanggal_baru = datetime.strptime(
                            input("tanggal pemotretan yang benar (DD-MM-YYYY): ").strip(), "%d-%m-%Y"
                        ).strftime("%d-%m-%Y")
                        data_pesanan["tanggal"] = tanggal_baru
                        break
                    except ValueError:
                        print("TANGGAL TIDAK VALID! GUNAKAN FORMAT DD-MM-YYYY!")
            elif ubah == 4:
                while True:
                    lokasi_baru = input("masukkan lokasi pemotretan yang benar: ").strip()
                    if lokasi_baru:
                        data_pesanan["lokasi"] = lokasi_baru
                        break
                    print("LOKASI TIDAK BOLEH KOSONG!")
            elif ubah == 5:
                lihat_fotografi()
                paket_tersedia = list(daftar_fotografi.keys())
                if paket_tersedia:
                    try:
                        nomor_paket = int(input("Pilih paket fotografi yang benar: "))
                        if 1 <= nomor_paket <= len(paket_tersedia):
                            paket_baru = paket_tersedia[nomor_paket - 1]
                            data_pesanan["paket"] = paket_baru
                            data_pesanan["total_harga"] = daftar_fotografi[paket_baru]
                        else:
                            print("NOMOR PAKET TIDAK TERSEDIA!")
                    except ValueError:
                        print("MASUKKAN ANGKA!")
            elif ubah == 6:
                while True:
                    print("1. transfer")
                    print("2. tunai")
                    metode_baru = input("pilih metode pembayaran: ").strip()
                    if metode_baru == "1":
                        data_pesanan["pembayaran"] = "transfer"
                        break
                    elif metode_baru == "2":
                        data_pesanan["pembayaran"] = "tunai"
                        break
                    print("PILIHAN PEMBAYARAN TIDAK TERSEDIA!")
            elif ubah == 7:
                continue
            else:
                print("PILIHAN TIDAK TERSEDIA!")
        else:
            print("PILIHAN TIDAK TERSEDIA!")

# CEK STATUS PESANAN USER
def batalkan_pesanan():
    print("-------------------------------")
    print("MENU PEMBATALAN PESANAN")
    id_pelanggan = input("masukkan ID pelanggan: ").strip().upper()
    daftar_milik = [
        i for i, data in enumerate(daftar_pesanan)
        if data.get("id_pelanggan", "").upper() == id_pelanggan
    ]
    if not daftar_milik:
        print("ID PELANGGAN TIDAK DITEMUKAN ATAU BELUM MEMILIKI PESANAN!")
        return

    print("DAFTAR PESANAN")
    for nomor, indeks in enumerate(daftar_milik, 1):
        data = daftar_pesanan[indeks]
        rincian = ", ".join(data["kamera"]) if data["jenis"] == "sewa kamera" and isinstance(data["kamera"], list) else data.get("kamera", data.get("paket", "-"))
        tanggal = data.get("tanggal_sewa", data.get("tanggal", "-"))
        print(nomor, "|", data["jenis"], "|", rincian, "|", tanggal, "|", data["status"])

    try:
        pilihan = int(input("pilih nomor pesanan yang ingin dibatalkan: "))
    except ValueError:
        print("PILIHAN HARUS BERUPA ANGKA!")
        return
    if pilihan < 1 or pilihan > len(daftar_milik):
        print("NOMOR PESANAN TIDAK VALID!")
        return

    indeks = daftar_milik[pilihan - 1]
    data = daftar_pesanan[indeks]
    if data["status"] != "menunggu validasi":
        print("PESANAN YANG SUDAH DIPROSES ADMIN TIDAK DAPAT DIBATALKAN MELALUI MENU USER.")
        return
    konfirmasi = input("yakin ingin membatalkan pesanan ini? (ya/tidak): ").lower().strip()
    if konfirmasi == "ya":
        daftar_pesanan.pop(indeks)
        print("PESANAN BERHASIL DIBATALKAN!")
    else:
        print("PEMBATALAN PESANAN DIBATALKAN.")


def cek_status_pesanan():
    print("MENU CEK STATUS PESANAN")
    id_pelanggan = input("masukkan ID pelanggan: ").strip().upper()
    ditemukan = False
    nomor_pesanan = 0
    for data in daftar_pesanan:
        if data.get("id_pelanggan", "").upper() == id_pelanggan:
            ditemukan = True
            nomor_pesanan += 1
            print("-------------------------------")
            print("PESANAN KE", nomor_pesanan)
            print("ID pelanggan:", data["id_pelanggan"])
            print("Nama:", data["nama"])
            print("No. telepon:", data["telpon"])
            print("Jenis pesanan:", data["jenis"])
            print("-------------------------------")
            if data["jenis"] == "sewa kamera":
                daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
                print("-------------------------------")
                print("daftar kamera:", ", ".join(daftar_nama))
                print("tanggal penyewaan:", data["tanggal_sewa"])
                print("tanggal pengembalian:", data["tanggal_kembali"])
                print("durasi:", data["durasi"])
                print("jaminan:", data["jaminan"])
                print("status pengembalian:", data.get("status_pengembalian", "belum dikembalikan"))
                if data.get("status_pengembalian") == "sudah dikembalikan":
                    print("Denda: Rp", data.get("denda", 0))
                print("-------------------------------")
            else:
                print("-------------------------------")
                print("paket:", data["paket"])
                print("tanggal pemotretan:", data["tanggal"])
                print("lokasi:", data["lokasi"])
            print("total pembayaran: Rp", data["total_harga"])
            print("metode pembayaran:", data["pembayaran"])
            print("status pesanan:", data["status"])
            print("-------------------------------")
    if not ditemukan:
        print("ID PELANGGAN TIDAK DITEMUKAN ATAU BELUM MEMILIKI PESANAN!")



# VALIDASI PESANAN OLEH ADMIN
def validasi_pesanan():
    print("MENU VALIDASI PESANAN")

    while True:
        pesanan_menunggu = [i for i, data in enumerate(daftar_pesanan)
                            if data["status"] == "menunggu validasi"]
        if not pesanan_menunggu:
            print("BELUM ADA PESANAN YANG PERLU DIVALIDASI!")
            return
        print("-------------------------------")
        print("DAFTAR PESANAN MENUNGGU VALIDASI")
        for nomor, indeks in enumerate(pesanan_menunggu, 1):
            data = daftar_pesanan[indeks]
            print("-------------------------------")
            print("nomor pesanan:", nomor)
            print("ID pelanggan:", data.get("id_pelanggan", "-"))
            print("nama:", data["nama"])
            print("jenis:", data["jenis"])
            if data["jenis"] == "sewa kamera":
                daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
                print("-------------------------------")
                print("kamera:", ", ".join(daftar_nama))
                print("tanggal sewa:", data["tanggal_sewa"])
                print("tanggal kembali:", data["tanggal_kembali"])
            else:
                print("-------------------------------")
                print("paket:", data["paket"])
                print("tanggal pemotretan:", data["tanggal"])
            print("total: Rp", data["total_harga"])


        print("-------------------------------")
        nomor_input = input("pilih nomor pesanan (b untuk kembali): ").strip().lower()
        if nomor_input == "b":
            return
        try:
            nomor = int(nomor_input)
        except ValueError:
            print("INPUT SALAH! MASUKKAN NOMOR PESANAN YANG TERSEDIA.")
            continue
        if nomor < 1 or nomor > len(pesanan_menunggu):
            print("INPUT SALAH! NOMOR PESANAN TIDAK TERSEDIA.")
            continue

        data = daftar_pesanan[pesanan_menunggu[nomor - 1]]
        print("-------------------------------")
        print("DETAIL PESANAN")
        print("ID pelanggan:", data.get("id_pelanggan", "-"))
        print("nama:", data["nama"])
        print("telepon:", data["telpon"])
        print("jenis:", data["jenis"])
        if data["jenis"] == "sewa kamera":
            daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
            print("-------------------------------")
            print("kamera:", ", ".join(daftar_nama))
            print("durasi:", data["durasi"])
            print("tanggal sewa:", data["tanggal_sewa"])
            print("tanggal kembali:", data["tanggal_kembali"])
            print("jaminan:", data["jaminan"])
        else:
            print("-------------------------------")
            print("paket:", data["paket"])
            print("tanggal pemotretan:", data["tanggal"])
            print("lokasi:", data["lokasi"])
        print("total: Rp", data["total_harga"])
        print("pembayaran:", data["pembayaran"])

        while True:
            print("-------------------------------")
            print("PILIH TINDAKAN ADMIN")
            print("1. terima pesanan")
            print("2. tolak pesanan")
            print("3. kembali ke daftar pesanan")
            print("-------------------------------")
            try:
                pilihan = int(input("pilih tindakan: "))
            except ValueError:
                print("INPUT SALAH! MASUKKAN ANGKA 1, 2, ATAU 3.")
                continue

            if pilihan == 1:
                konfirmasi = input("yakin menerima pesanan? (ya/tidak): ").strip().lower()
                if konfirmasi != "ya":
                    print("PENERIMAAN DIBATALKAN. PESANAN BELUM BERUBAH.")
                    continue

                if data["jenis"] == "sewa kamera":
                    rincian = data.get("rincian_kamera")
                    if not rincian:
                        daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
                        rincian = [{"nama": nama_kamera} for nama_kamera in daftar_nama]

                    jumlah_per_kamera = {}
                    for item in rincian:
                        nama_kamera = item["nama"]
                        jumlah_per_kamera[nama_kamera] = jumlah_per_kamera.get(nama_kamera, 0) + 1

                    stok_cukup = True
                    for nama_kamera, jumlah in jumlah_per_kamera.items():
                        if stok_kamera.get(nama_kamera, 0) < jumlah:
                            print("STOK", nama_kamera, "TIDAK MENCUKUPI. PESANAN BELUM DITERIMA!")
                            stok_cukup = False
                    if not stok_cukup:
                        break

                    for nama_kamera, jumlah in jumlah_per_kamera.items():
                        stok_kamera[nama_kamera] -= jumlah
                    data["rincian_kamera"] = rincian

                data["status"] = "diterima Admin"
                print("PESANAN BERHASIL DITERIMA!")
                break

            elif pilihan == 2:
                konfirmasi = input("yakin menolak pesanan? (ya/tidak): ").strip().lower()
                if konfirmasi == "ya":
                    data["status"] = "ditolak Admin"
                    print("PESANAN BERHASIL DITOLAK!")
                    break
                print("PENOLAKAN DIBATALKAN. PESANAN BELUM BERUBAH.")

            elif pilihan == 3:
                break
            else:
                print("INPUT SALAH! PILIH 1, 2, ATAU 3.")

def pengembalian_kamera():
    from datetime import datetime
    print("MENU PENGEMBALIAN KAMERA")
    pesanan_aktif = [
        i for i, data in enumerate(daftar_pesanan)
        if data["jenis"] == "sewa kamera"
        and data["status"] == "diterima Admin"
        and data.get("status_pengembalian") == "belum dikembalikan"
    ]
    if not pesanan_aktif:
        print("BELUM ADA KAMERA YANG PERLU DIKEMBALIKAN!")
        return

    for nomor, indeks in enumerate(pesanan_aktif, 1):
        data = daftar_pesanan[indeks]
        daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
        print(nomor, data["nama"], "-", ", ".join(daftar_nama), "-", data["tanggal_kembali"])
    try:
        nomor = int(input("pilih nomor pesanan yang dikembalikan: "))
    except ValueError:
        print("PILIHAN HARUS BERUPA ANGKA!")
        return
    if nomor < 1 or nomor > len(pesanan_aktif):
        print("NOMOR PESANAN TIDAK VALID!")
        return
    data = daftar_pesanan[pesanan_aktif[nomor - 1]]
    print("-------------------------------")
    print("nama penyewa:", data["nama"])
    print("kamera:", ", ".join(data["kamera"]) if isinstance(data["kamera"], list) else data["kamera"])
    print("tanggal seharusnya kembali:", data["tanggal_kembali"])
    print("-------------------------------")

    while True:
        try:
            tanggal_aktual = datetime.strptime(
                input("tanggal pengembalian aktual (DD-MM-YYYY): ").strip(), "%d-%m-%Y"
            )
            break
        except ValueError:
            print("TANGGAL TIDAK VALID!")
    while True:
        try:
            waktu_aktual = datetime.strptime(
                input("jam pengembalian aktual (JJ:MM): ").strip(), "%H:%M"
            ).time()
            break
        except ValueError:
            print("WAKTU TIDAK VALID!")

    aktual = datetime.combine(tanggal_aktual.date(), waktu_aktual)
    harus_kembali = datetime.strptime(data["tanggal_kembali"], "%d-%m-%Y %H:%M")
    terlambat_detik = (aktual - harus_kembali).total_seconds()
    hari_terlambat = int((terlambat_detik + 86399) // 86400) if terlambat_detik > 0 else 0
    jumlah_kamera = len(data["kamera"]) if isinstance(data["kamera"], list) else 1
    denda_waktu = hari_terlambat * 50000 * jumlah_kamera

    print("-------------------------------")
    print("PEMERIKSAAN KAMERA DAN PERLENGKAPAN")
    print("1. lengkap dan kondisi baik")
    print("2. ada kerusakan")
    print("3. ada perlengkapan yang kurang")
    print("-------------------------------")
    while True:
        try:
            kondisi = int(input("pilih kondisi pengembalian: "))
        except ValueError:
            print("MASUKKAN ANGKA!")
            continue
        if kondisi in [1, 2, 3]:
            break
        print("PILIHAN TIDAK TERSEDIA!")

    if kondisi == 1:
        keterangan_kondisi, denda_kondisi = "lengkap dan baik", 0
    elif kondisi == 2:
        keterangan_kondisi, denda_kondisi = "ada kerusakan", 100000 * jumlah_kamera
    else:
        keterangan_kondisi, denda_kondisi = "ada perlengkapan yang kurang", 50000 * jumlah_kamera

    total_denda = denda_waktu + denda_kondisi

    print("-------------------------------")
    print("Denda keterlambatan: Rp", denda_waktu)
    print("Denda kondisi/perlengkapan: Rp", denda_kondisi)
    print("TOTAL DENDA: Rp", total_denda)
    print("-------------------------------")
    while True:
        try:
            bayar_denda = int(input("Masukkan jumlah denda yang dibayar: "))
            if bayar_denda < total_denda:
                print("PEMBAYARAN DENDA KURANG!")
                continue
            break
        except ValueError:
            print("MASUKKAN JUMLAH PEMBAYARAN BERUPA ANGKA!")
    if bayar_denda > total_denda:
        print("kembalian: Rp", bayar_denda - total_denda)

    data["status_pengembalian"] = "sudah dikembalikan"
    data["tanggal_pengembalian_aktual"] = aktual.strftime("%d-%m-%Y %H:%M")
    data["denda"] = total_denda
    data["denda_dibayar"] = total_denda
    data["kondisi_kamera"] = keterangan_kondisi

    daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
    for nama_kamera in daftar_nama:
        stok_kamera[nama_kamera] = stok_kamera.get(nama_kamera, 0) + 1

    print("-------------------------------")
    print("BUKTI PENGEMBALIAN KAMERA")
    print("Nama penyewa:", data["nama"])
    print("Kamera:", ", ".join(daftar_nama))
    print("Tanggal seharusnya kembali:", data["tanggal_kembali"])
    print("Tanggal aktual kembali:", data["tanggal_pengembalian_aktual"])
    print("Kondisi kamera:", data["kondisi_kamera"])
    print("Denda keterlambatan: Rp", denda_waktu)
    print("Denda kondisi/perlengkapan: Rp", denda_kondisi)
    print("Total denda dibayar: Rp", data["denda_dibayar"])
    print("Status:", data["status_pengembalian"])
    print("Stok kamera berhasil diperbarui.")
    print("-------------------------------")

# LAPORAN PEMASUKAN
def laporan_pemasukan():
    from datetime import datetime
    print("\nLAPORAN PEMASUKAN")
    tanggal_input = input("Masukkan tanggal laporan (DD-MM-YYYY), atau kosong untuk semua: ").strip()
    if tanggal_input:
        try:
            tanggal_filter = datetime.strptime(tanggal_input, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            print("FORMAT TANGGAL TIDAK VALID!")
            return
    else:
        tanggal_filter = None

    total_kamera = 0
    total_fotografi = 0
    total_denda = 0
    ada = False
    for data in daftar_pesanan:
        if data["status"] != "diterima Admin":
            continue
        if data["jenis"] == "sewa kamera":
            tanggal_pesanan = data["tanggal_sewa"].split()[0]
            if tanggal_filter and tanggal_pesanan != tanggal_filter:
                continue
            total_kamera += data["total_harga"]
            total_denda += data.get("denda_dibayar", 0)
            ada = True
        elif data["jenis"] == "jasa fotografi":
            if tanggal_filter and data["tanggal"] != tanggal_filter:
                continue
            total_fotografi += data["total_harga"]
            ada = True
    if not ada:
        print("BELUM ADA PEMASUKAN UNTUK TANGGAL TERSEBUT.")
        return

    print("-------------------------------")
    print("Pemasukan sewa kamera: Rp", total_kamera)
    print("Pemasukan jasa fotografi: Rp", total_fotografi)
    print("Pemasukan denda: Rp", total_denda)
    print("TOTAL PEMASUKAN: Rp", total_kamera + total_fotografi + total_denda)
    print("-------------------------------")


# DAFTAR PESANAN DAN MENU ADMIN
def tampilkan_pesanan():
    print("DAFTAR SEMUA PESANAN")
    if not daftar_pesanan:
        print("BELUM ADA PESANAN!")
        return
    for nomor, data in enumerate(daftar_pesanan, 1):
        print("-------------------------------")
        print("PESANAN KE", nomor)
        print("nama:", data["nama"])
        print("telepon:", data["telpon"])
        print("jenis:", data["jenis"])
        if data["jenis"] == "sewa kamera":
            daftar_nama = data["kamera"] if isinstance(data["kamera"], list) else [data["kamera"]]
            print("-------------------------------")
            print("kamera:", ", ".join(daftar_nama))
            print("tanggal sewa:", data["tanggal_sewa"])
            print("tanggal kembali:", data["tanggal_kembali"])
            print("status pengembalian:", data["status_pengembalian"])
            print("-------------------------------")
        else:
            print("-------------------------------")
            print("paket:", data["paket"])
            print("tanggal pemotretan:", data["tanggal"])
            print("lokasi:", data["lokasi"])
        print("total: Rp", data["total_harga"])
        print("status pesanan:", data["status"])


def menu_admin():
    while True:
        print("-------------------------------")
        print("MENU ADMIN")
        print("1. kelola sewa kamera")
        print("2. kelola jasa fotografi")
        print("3. validasi pesanan")
        print("4. pengembalian kamera")
        print("5. laporan pemasukan")
        print("6. lihat semua pesanan")
        print("7. kembali")
        print("-------------------------------")
        try:
            pilihan = int(input("pilih menu: "))
        except ValueError:
            print("MASUKKAN ANGKA!")
            continue
        if pilihan == 1:
            menu_kelola_kamera()
        elif pilihan == 2:
            menu_kelola_fotografi()
        elif pilihan == 3:
            validasi_pesanan()
        elif pilihan == 4:
            pengembalian_kamera()
        elif pilihan == 5:
            laporan_pemasukan()
        elif pilihan == 6:
            tampilkan_pesanan()
        elif pilihan == 7:
            break
        else:
            print("PILIHAN MENU TIDAK TERSEDIA!")


# PROGRAM UTAMA
while True:
    menu = menu_awal()
    if menu == 1:
        while True:
            pilihan_user = menu_user()
            if pilihan_user == 1:
                kamera()
            elif pilihan_user == 2:
                jasa_fotografi()
            elif pilihan_user == 3:
                cek_status_pesanan()
            elif pilihan_user == 4:
                batalkan_pesanan()
            elif pilihan_user == 5:
                break
            else:
                print("PILIHAN MENU TIDAK TERSEDIA!")
    elif menu == 2:
        if login_admin():
            menu_admin()
    elif menu == 3:
        print("TERIMA KASIH TELAH MENGGUNAKAN JASA KAMI!")
        break
    else:
        print("PILIHAN MENU TIDAK TERSEDIA!")
