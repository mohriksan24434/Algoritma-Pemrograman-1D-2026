def input_set(nama):
    data = set()
    jumlah = int(input(f"Jumlah {nama}: "))
    for i in range(jumlah):
        item = input(f"  {nama} ke-{i+1}: ")
        data.add(item)
    return data

print("=== INPUT DATA WEBINAR ===")
undangan = input_set("undangan")
webinar_a = input_set("peserta Webinar A")
webinar_b = input_set("peserta Webinar B")

print("\n=== HASIL ANALISIS ===")
print(f"Semua peserta kedua webinar: {webinar_a | webinar_b}")
print(f"Peserta yang hadir di keduanya: {webinar_a & webinar_b}")
print(f"Peserta yang hanya hadir di salah satu webinar: {webinar_a ^ webinar_b}")
print(f"Undangan yang tidak hadir di webinar mana pun: {undangan - (webinar_a | webinar_b)}")





