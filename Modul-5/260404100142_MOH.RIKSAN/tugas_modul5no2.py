def is_palindrome(kata):
    """
    Fungsi untuk mengecek apakah sebuah kata adalah palindrom.
    Mengembalikan True jika palindrom, False jika bukan.
    """
    # Ubah ke huruf kecil agar tidak case-sensitive
    kata = kata.lower()
    
    # Bandingkan kata dengan kebalikannya
    if kata == kata[::-1]:
        return True
    else:
        return False


# Program utama (dinamis)
print("=" * 50)
print("PROGRAM PENGECEK KATA PALINDROM")
print("=" * 50)

kata_input = input("Masukkan sebuah kata: ")

if kata_input == "":
    print("Error: Kata tidak boleh kosong!")
else:
    hasil = is_palindrome(kata_input)
    
    print(f"\nKata yang dimasukkan : '{kata_input}'")
    print(f"Hasil fungsi         : {hasil}")
    
    if hasil:
        print(f"Kesimpulan           : '{kata_input}' adalah PALINDROME")
    else:
        print(f"Kesimpulan           : '{kata_input}' BUKAN palindrome")