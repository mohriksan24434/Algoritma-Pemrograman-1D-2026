def hitung_nilai_akhir(nama, tugas, uts, uas):
    """
    Fungsi untuk menghitung nilai akhir mahasiswa dan menentukan grade.
    Bobot: Tugas 30%, UTS 30%, UAS 40%
    """
    # Hitung nilai akhir
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    
    # Tentukan grade
    if nilai_akhir >= 85:
        grade = "A"
        status = "Lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "Lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "Lulus"
    else:
        grade = "D"
        status = "Tidak Lulus"
    
    # Tampilkan hasil secara lengkap
    print("\n" + "=" * 50)
    print("HASIL PERHITUNGAN NILAI MAHASISWA")
    print("=" * 50)
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {tugas}  (bobot 30%)")
    print(f"Nilai UTS      : {uts}  (bobot 30%)")
    print(f"Nilai UAS      : {uas}  (bobot 40%)")
    print("-" * 50)
    print(f"Nilai Akhir    : {nilai_akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")
    print("=" * 50)
    
    return nilai_akhir, grade, status


# Program utama (dinamis)
print("=" * 50)
print("PROGRAM PENGHITUNG NILAI AKHIR MAHASISWA")
print("=" * 50)

try:
    nama = input("Masukkan nama mahasiswa : ")
    tugas = float(input("Masukkan nilai tugas     : "))
    uts   = float(input("Masukkan nilai UTS       : "))
    uas   = float(input("Masukkan nilai UAS       : "))
    
    # Validasi rentang nilai
    if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
        print("Error: Nilai harus berada di rentang 0 - 100!")
    else:
        hitung_nilai_akhir(nama, tugas, uts, uas)
        
except ValueError:
    print("Error: Input nilai harus berupa angka!")
    