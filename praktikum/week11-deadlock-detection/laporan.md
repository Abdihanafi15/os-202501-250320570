
# Laporan Praktikum Minggu [11]
Topik: [Simulasi dan Deteksi Deadlock]

---

## Identitas
- **Nama**  : [Abdi Hanafi Alghifari]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan
1. Memahami konsep deadlock dalam sistem operasi.
2. Mampu mensimulasikan kondisi deadlock pada proses dan sumber daya.
3. Mengimplementasikan metode deteksi deadlock (misalnya Banker's Algorithm / Deteksi Resource Allocation Graph).
4. Menganalisis kondisi sistem apakah mengalami deadlock atau tidak.
5. Melatih kemampuan debugging dalam simulasi manajemen sumber daya.

---

## Dasar Teori
1. Deadlock adalah kondisi di mana beberapa proses saling menunggu sumber daya yang sedang dipakai proses lain, sehingga tidak ada proses yang bisa berjalan.
2. Deadlock terjadi jika keempat kondisi ini terpenuhi: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait
3. Deteksi deadlock dilakukan dengan memeriksa apakah terdapat siklus (cycle) pada alokasi sumber daya. Jika ada siklus, berarti deadlock terjadi.
4. Jika deadlock terdeteksi, dapat dilakukan:
- Abort proses (menghentikan proses tertentu)
- Preemption (mengambil sumber daya dari proses)
- Rollback (mengembalikan proses ke kondisi sebelumnya)

---

## Langkah Praktikum
1. Menyiapkan Dataset

Gunakan dataset sederhana yang berisi:
- Daftar proses
- Resource Allocation
- Resource Request / Need
- Contoh tabel:

 | Proses |	Allocation | Request |
 |--------|-------------|---------|
 | P1 | R1 | R2 |
 | P2 | R2 | R3 |
 | P3 | R3 | R1 |


2. Implementasi Algoritma Deteksi Deadlock

  Program minimal harus:

- Membaca data proses dan resource.
- Menentukan apakah sistem berada dalam kondisi deadlock.
- Menampilkan proses mana saja yang terlibat deadlock.

3. Eksekusi & Validasi
- Jalankan program dengan dataset uji.
- Validasi hasil deteksi dengan analisis manual/logis.
- Simpan hasil eksekusi dalam bentuk screenshot.

4. Analisis Hasil
- Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
- Jelaskan mengapa deadlock terjadi atau tidak terjadi.
- Kaitkan hasil dengan teori deadlock (empat kondisi).

5. Commit & Push

        git add .
        git commit -m "Minggu 11 - Deadlock Detection"
        git push origin main

---

## Kode / Perintah
```bash 

# PROGRAM DETEKSI DEADLOCK (TABEL)
# ===================================

# 1. Dataset berbentuk tabel (list of dict)
table = [
    {"Proses": "P1", "Allocation": "R1", "Request": "R2"},
    {"Proses": "P2", "Allocation": "R2", "Request": "R3"},
    {"Proses": "P3", "Allocation": "R3", "Request": "R1"}
]

# Menampilkan tabel dataset
print("DATASET:")
print("Proses | Allocation | Request")
for row in table:
    print(f"{row['Proses']}     | {row['Allocation']}         | {row['Request']}")

# 2. Mencatat resource yang sedang dipegang
allocation = {}
for row in table:
    allocation[row["Allocation"]] = row["Proses"]

# 3. Membentuk Wait-For Graph
graph = {}
for row in table:
    process = row["Proses"]
    request = row["Request"]

    holder = allocation.get(request)
    if holder:
        graph.setdefault(process, []).append(holder)

# 4. Fungsi DFS untuk deteksi siklus
visited = set()
rec_stack = set()

def detect_deadlock(p):
    visited.add(p)
    rec_stack.add(p)

    for neighbor in graph.get(p, []):
        if neighbor not in visited:
            if detect_deadlock(neighbor):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(p)
    return False

# 5. Eksekusi deteksi deadlock
deadlock = False
for p in graph:
    if p not in visited:
        if detect_deadlock(p):
            deadlock = True
            break

# 6. Menampilkan hasil
print("\nWAIT-FOR GRAPH:")
for p in graph:
    print(f"{p} -> {graph[p]}")

print("\nHASIL EKSEKUSI:")
if deadlock:
    print("DEADLOCK TERDETEKSI")
else:
    print("TIDAK ADA DEADLOCK")


```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil%20deadlock.png)

---

## Analisis
1. Tabel Hasil Deteksi Deadlock

| Proses	| Status |
|---------|-------|
| P1	| Deadlock |
| P2	| Deadlock |
| P3	| Deadlock |

sistem mengalami deadlock.Semua proses saling menunggu dan tidak ada yang bisa lanjut.

2. Mengapa Deadlock Terjadi ,

  Deadlock terjadi karena setiap proses:
- Memegang satu resource
- Menunggu resource lain yang sedang dipegang proses lain

    Urutan tunggu:

        P1 menunggu R2 (dipegang P2)
        P2 menunggu R3 (dipegang P3)
        P3 menunggu R1 (dipegang P1)


    Terbentuk circular wait:

        P1 → P2 → P3 → P1

sehingga 
- Tidak ada proses yang bisa maju
- Tidak ada resource yang dilepas
- Sistem berhenti (deadlock) 

3.  Deadlock terjadi jika keempat kondisi ini terpenuhi:

| Kondisi          | Terpenuhi? | Penjelasan                                                  |
| ---------------- | ---------- | ----------------------------------------------------------- |
| Mutual Exclusion | ✔️ Ya      | Setiap resource (R1, R2, R3) hanya bisa dipakai satu proses |
| Hold and Wait    | ✔️ Ya      | Proses memegang satu resource sambil menunggu resource lain |
| No Preemption    | ✔️ Ya      | Resource tidak bisa diambil paksa oleh sistem               |
| Circular Wait    | ✔️ Ya      | Terjadi siklus P1 → P2 → P3 → P1                            |


---

## Kesimpulan
Berdasarkan hasil deteksi deadlock pada dataset yang diberikan, sistem mengalami deadlock karena seluruh proses (P1, P2, dan P3) saling menunggu resource yang sedang dipegang oleh proses lain sehingga membentuk circular wait. Setiap proses memegang satu resource dan menunggu resource lain tanpa adanya mekanisme pengambilan paksa, menyebabkan tidak ada proses yang dapat melanjutkan eksekusi. Kondisi ini memenuhi keempat syarat terjadinya deadlock menurut teori Coffman, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait, sehingga deadlock tidak dapat dihindari dan sistem berada dalam keadaan macet.

---

## Quiz
1. [Apa perbedaan antara deadlock prevention, avoidance, dan detection?]  
   **Jawaban:**

Perbedaan Deadlock Prevention, Avoidance, dan Detection

- Deadlock Prevention
Mencegah deadlock dengan menghilangkan salah satu dari empat kondisi deadlock (misalnya melarang hold and wait).
➜ Deadlock tidak mungkin terjadi, tetapi penggunaan resource jadi kurang efisien.

- Deadlock Avoidance
Menghindari deadlock dengan memeriksa kondisi sistem sebelum resource dialokasikan (contoh: algoritma Banker).
➜ Sistem aman dari deadlock, tetapi perlu informasi kebutuhan resource di awal.

- Deadlock Detection
Mengizinkan deadlock terjadi, lalu mendeteksinya dan melakukan pemulihan.
➜ Lebih fleksibel dan efisien dalam penggunaan resource.

2. [Mengapa Deteksi Deadlock Tetap Diperlukan?]  
   **Jawaban:**  

   Deteksi deadlock diperlukan karena tidak semua sistem bisa menerapkan prevention atau avoidance, terutama pada sistem besar dan dinamis. Dalam kondisi tersebut, membiarkan deadlock terjadi lalu mendeteksinya adalah cara paling realistis agar sistem tetap berjalan dan resource dapat dipulihkan.

3. [Apa kelebihan dan kekurangan pendekatan deteksi deadlock?]  
   **Jawaban:**  

Kelebihan:
- Pemakaian resource lebih efisien
- Cocok untuk sistem kompleks dan dinamis
- Tidak perlu informasi kebutuhan resource di awal

Kekurangan:
- Deadlock tetap bisa terjadi
- Membutuhkan proses pemulihan (terminasi proses)
- Ada overhead untuk proses deteksi

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
