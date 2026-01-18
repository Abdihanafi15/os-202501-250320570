
# Laporan Praktikum Minggu [9]
Topik: [Simulasi scheduling CPU]

---

## Identitas
- **Nama**  : [Abdi Hanafi Alghifari]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan

1. Mampu memahami cara kerja penjadwalan CPU
2. Membandingkan berbagai algoritma penjadwalan, seperti :
   - Waiting Time
   - Turnaround Time
3. Untuk mengetahui algoritma mana yang lebih efisien dalam kondisi tertentu
4. membantu memahami dampak keputusan penjadwalan terhadap performa sistem.

---

## Dasar Teori
1. Penjadwalan CPU

    Merupakan mekanisme sistem operasi untuk menentukan urutan eksekusi proses yang ada di ready queue agar penggunaan CPU lebih efisien.

2. First Come First Serve (FCFS) 
    adalah algoritma penjadwalan CPU yang menjalankan proses sesuai urutan kedatangan. Proses yang datang lebih dulu akan dilayani lebih dulu, tanpa melihat lama atau cepat proses tersebut.

3. Shortest Job First (SJF)

    Proses dengan burst time paling pendek diprioritaskan. Algoritma ini lebih optimal dalam menurunkan rata-rata waiting time dan turnaround time, namun membutuhkan estimasi burst time yang akurat.

4. Waiting Time dan Turnaround Time

   - Waiting Time = waktu tunggu proses di ready queue sebelum dieksekusi.
   - Turnaround Time = total waktu dari kedatangan proses hingga      selesai dieksekusi. Kedua metrik ini digunakan untuk mengevaluasi performa algoritma penjadwalan. e. Simulasi Penjadwalan Digunakan untuk menguji algoritma secara otomatis dengan dataset tertentu, sehingga hasil lebih cepat, akurat, dan mudah dibandingkan dengan perhitungan manual.

---

## Langkah Praktikum
1. Menyiapkan Dataset

    Buat dataset proses minimal berisi:

    | Proses	| Arrival Time |	Burst Time |
    |---------|--------------|------------|
    | P1 | 0 | 6 |
    | P2 | 1 | 8 |
    | P3 | 2 | 7 |
    | P4 | 3 | 3 |

2. Implementasi Algoritma

    Program harus:

    - Menghitung waiting time dan turnaround time.
    - Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
    - Menampilkan hasil dalam tabel.

3. Eksekusi & Validasi

    - Jalankan program menggunakan dataset uji.
    - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
    - Simpan hasil eksekusi (screenshot).

4. Analisis

    - Jelaskan alur program.
    - Bandingkan hasil simulasi dengan perhitungan manual.
    
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. Commit & Push

       git add .
       git commit -m "Minggu 9 - Simulasi Scheduling CPU"
       git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:

FCSF
```BASH
   def fcfs(processes):
       current_time = 0
       total_wt = 0
       total_tat = 0

    # urutkan berdasarkan arrival time
    processes.sort(key=lambda x: x[1])

    print("Proses | AT | BT | WT | TAT")
    print("---------------------------")

    for p in processes:
        name, at, bt = p

        if current_time < at:
            current_time = at

        wt = current_time - at
        tat = wt + bt

        current_time += bt
        total_wt += wt
        total_tat += tat

        print(f"{name:6} | {at:2} | {bt:2} | {wt:2} | {tat:3}")

    n = len(processes)
    print("\nRata-rata Waiting Time =", total_wt / n)
    print("Rata-rata Turnaround Time =", total_tat / n)


# Data proses
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3)
]

fcfs(processes)
```

SJF non-preemptive

```bash
def sjf_non_preemptive(processes):
    time = 0
    completed = []
    results = []

    n = len(processes)

    while len(completed) < n:
        # proses yang sudah datang & belum selesai
        ready = [p for p in processes
                 if p["arrival"] <= time and p["pid"] not in completed]

        if not ready:
            time += 1
            continue

        # pilih burst time paling kecil
        p = min(ready, key=lambda x: x["burst"])

        waiting = time - p["arrival"]
        turnaround = waiting + p["burst"]

        results.append({
            "pid": p["pid"],
            "waiting": waiting,
            "turnaround": turnaround
        })

        time += p["burst"]
        completed.append(p["pid"])

    return results

```
---

output tabelnya 

```bash
def print_table(title, results):
    print(f"=== {title} ===")
    print("PID | Waiting | Turnaround")
    print("---------------------------")

    total_waiting = 0
    total_turnaround = 0

    for r in results:
        print(f"{r['pid']:>3} | {r['waiting']:>7} | {r['turnaround']:>10}")
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]

    n = len(results)
    print("---------------------------")
    print(f"Rata-rata Waiting   : {total_waiting / n:.2f}")
    print(f"Rata-rata Turnaround: {total_turnaround / n:.2f}")

```

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/simulasi%20hasil%20scheduling%20CPU.png)

---

## Analisis
1. alur program untuk kedua algoritma adalah:

- Input data proses
- Pilih algoritma scheduling
- Urutkan proses sesuai algoritma
- Hitung waktu Waiting dan Turnaround
- Hitung rata-rata
- Tampilkan tabel hasil

2. Alur FCFS (First Come First Served).
- Proses diurutkan berdasarkan Arrival Time
- Urutan eksekusi: P1 → P2 → P3 → P4
- variabel program menggunakan current_time:
- P1
     - Mulai: 0
     - Waiting Time = 0 − 0 = 0
     - Turnaround = 0 + 6 = 6

- P2
     - Mulai setelah P1 selesai → waktu 6
     - Waiting Time = 6 − 1 = 5
     - Turnaround = 5 + 8 = 13

- P3
     - Mulai: 14
     - Waiting Time = 14 − 2 = 12
     - Turnaround = 12 + 7 = 19

- P4
     - Mulai: 21
     - Waiting Time = 21 − 3 = 18
     - Turnaround = 18 + 3 = 21

- Rata-rata 
     - Waiting Time (0+5+12+18)/4=8.75
     - Turnaround Time (6+13+19+21)/4=14.75

3. Alur SJF (Shortest Job First – Non-Preemptive)
- CPU memilih proses dengan Burst Time terkecil
- Hanya dari proses yang sudah datang (arrival ≤ current time)
- Urutan Eksekusi
     - P1 (yang datang di waktu 0)
     - P4 (burst terkecil: 3)
     - P3 (burst 7)
     - P2 (burst terpanjang: 8)
- Urutan : P1 → P4 → P3 → P2
- Perhitungan :
     - P1
         - Waiting = 0
         - Turnaround = 6

     - P4
         - Mulai: 6
         - Waiting = 6 − 3 = 3
         - Turnaround = 3 + 3 = 6

     - P3
         - Mulai: 9
         - Waiting = 9 − 2 = 7
         - Turnaround = 7 + 7 = 14

     - P2
         - Mulai: 16
         - Waiting = 16 − 1 = 15
         - Turnaround = 15 + 8 = 23

- Rata-rata
     - Waiting : (0+3+7+15)/4=6.25
     - Turnaround : (6+6+14+23)/4=12.25

3. Perbandingan hasil simulasi hasil  hitungan FCFS dan SJF:

a. FCFS (First Come First Serve)
- Urutan eksekusi: P1 → P2 → P3 → P4
- Waiting time: 0, 5, 12, 18
- Turnaround time: 6, 13, 19, 21
- Rata-rata waiting = 8.75
- Rata-rata turnaround = 14.75

b. SJF (Shortest Job First – Non-Preemptive)
- Urutan eksekusi: P1 → P4 → P3 → P2
- Waiting time: 0, 3, 7, 13
- Turnaround time: 6, 6, 14, 21
- Rata-rata waiting = 5.75
- Rata-rata turnaround = 11.75

4. Kelebihan Simulasi

- Mudah memahami cara kerja algoritma
- Aman dan tidak menggunakan sistem nyata
- Perhitungannya cepat dan otomatis
- Memudahkan membandingkan FCFS dan SJF

5. Keterbatasan simulasi 

- Tidak menggambarkan kondisi sistem nyata sepenuhnya
- Menggunakan asumsi sederhana
- Tidak memperhitungkan overhead dan interupsi
- Hasil bergantung pada data yang digunakan

---

## Kesimpulan
1. CPU Scheduling digunakan untuk mengatur urutan eksekusi proses agar CPU bekerja efisien.

2. Algoritma FCFS mengeksekusi proses berdasarkan urutan kedatangan dan mudah diimplementasikan, namun menghasilkan waiting time lebih besar.

3. Algoritma SJF memilih proses dengan burst time paling kecil sehingga menghasilkan waiting time dan turnaround time lebih kecil dibanding FCFS.

4. Hasil simulasi sesuai dengan perhitungan manual, menandakan algoritma berjalan dengan benar.

5. Setiap algoritma memiliki kelebihan dan keterbatasan, sehingga pemilihan algoritma bergantung pada kebutuhan sistem.

---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]
- Memudahkan pemahaman : simulasi menunjukkan secara langsung urutan eksekusi proses dan waktu tunggu.
- Menghindari risiko pada sistem nyata : Pengujian tidak dilakukan langsung pada sistem operasi asli.
- Memungkinkan perbandingan algoritma : FCFS, SJF, dan algoritma lain bisa dibandingkan hasilnya dengan data yang sama.
- Memverifikasi kebenaran algoritma : Hasil simulasi dapat dibandingkan dengan perhitungan manual.
- Lebih efisien dan fleksibel : Data proses dapat diubah tanpa biaya atau dampak besar.


2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]

   Perbedaan utama hasil simulasi dan perhitungan manual pada dataset besar terletak pada pendekatan dan kompleksitas, di mana simulasi (numerik/komputer) unggul dalam menangani skala dan kompleksitas tinggi melalui aproksimasi dan model, sementara perhitungan manual (analitik/rumus sederhana) menjadi tidak praktis atau mustahil karena waktu dan sumber daya, namun hasilnya idealnya mendekati nilai sebenarnya jika model simulasi akurat, meskipun simulasi memiliki potensi kesalahan pemodelan, diskritisasi, dan iteratif yang perlu dikelola untuk validitas.


3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]
   
   - Logika sederhana → proses dijalankan sesuai urutan kedatangan, mirip antrean.
   - Tidak perlu parameter tambahan → tidak ada prioritas, kuantum waktu, atau perhitungan kompleks.
   - Implementasi mudah → cukup menggunakan struktur data queue (FIFO).
   - Perhitungan metrik sederhana → waktu tunggu dan turnaround dapat dihitung langsung dari urutan eksekusi.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
