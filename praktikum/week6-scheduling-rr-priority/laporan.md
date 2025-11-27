
# Laporan Praktikum Minggu [X]
Topik: [ Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling]

---

## Identitas
- **Nama**  : [abdi hanafi alghifari]
- **NIM**   : [250320570]
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori

1. Round Robin (RR) adalah algoritma penjadwalan CPU yang termasuk dalam kategori preemptive scheduling. Algoritma ini dirancang untuk sistem time-sharing agar setiap proses mendapatkan kesempatan yang adil untuk dieksekusi.

2. Priority Scheduling adalah algoritma penjadwalan CPU yang memilih proses berdasarkan prioritas tertinggi. Prioritas dapat berupa:

   - Angka kecil berarti prioritas tinggi (atau sebaliknya, bergantung desain).
   - Ditentukan berdasarkan kebutuhan sistem (I/O bound, CPU bound, dll.).

3. Time Quantum (atau time slice) adalah satuan waktu tetap yang diberikan sistem operasi kepada setiap proses untuk menggunakan CPU dalam algoritma preemptive scheduling, khususnya Round Robin (RR) dan beberapa varian lain.

4. Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan proses mana yang akan menggunakan CPU pada suatu waktu. Penjadwalan diperlukan ketika terjadi transisi siap → berjalan, atau ketika proses berhenti, menunggu I/O, atau selesai.
---

## Langkah Praktikum
1. Siapkan Data Proses Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):

| Proses | Burst Time |	Arrival Time |	Priority |
|---------|------------|--------------|----------|
| P1 | 5 | 0 |	2 |
| P2 | 3 | 1 |	1 |
| P3 | 8 | 2 |	4 |
| P4 | 6 | 3 |	3 |

2. Eksperimen 1 – Round Robin (RR)

- Gunakan time quantum (q) = 3.
- Hitung waiting time dan turnaround time untuk tiap proses.
- Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).

   ```
    | P1 | P2 | P3 | P4 | P1 | P3 | 
    0    3    6    9   12   15   18  
   ```
- Catat sisa burst time tiap putaran.


3. Eksperimen 2 – Priority Scheduling (Non-Preemptive)

- Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
- Lakukan perhitungan manual untuk:

       WT[i] = waktu mulai eksekusi - Arrival[i]
       TAT[i] = WT[i] + Burst[i]

- Buat tabel perbandingan hasil RR dan Priority.

4. Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)

- Ubah quantum menjadi 2 dan 5.
- Amati perubahan nilai rata-rata waiting time dan turnaround time.
- Buat tabel perbandingan efek quantum.

5. Eksperimen 4 – Dokumentasi

- Simpan semua hasil tabel dan screenshot ke:

       praktikum/week6-scheduling-rr-priority/screenshots/

- Buat tabel perbandingan seperti berikut:

| Algoritma | Avg Waiting Time |	Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|-----------------|----------------------|-----------|------------|
| RR | ... | ... | Adil terhadap semua proses |	Tidak efisien jika quantum tidak tepat |
| Priority | ... | ... | Efisien untuk proses penting | Potensi starvation pada prioritas rendah |

6. Commit & Push

       git add .
       git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
       git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:

| Proses | Burst Time |	Arrival Time |	Priority |
|---------|------------|--------------|----------|
| P1 | 5 | 0 |	2 |
| P2 | 3 | 1 |	1 |
| P3 | 8 | 2 |	4 |
| P4 | 6 | 3 |	3 |


   ```
    | P1 | P2 | P3 | P4 | P1 | P3 | 
    0    3    6    9   12   15   18  
   ```

       WT[i] = waktu mulai eksekusi - Arrival[i]
       TAT[i] = WT[i] + Burst[i]

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/round%20robin%20dan%20priority%20scheduling%20.png)


---

## Analisis

1. Eksperimen 1 round robin 

| proses | arrival time | burst time | waktu mulai | waktu selesei | turnaround time | waiting time | 
|---------|--------------|------------|------------|----------------|-----------------|--------------|
| P1 | 0 | 5 | 0 | 14 | 14 | 9 |
| P2 | 1 | 3 | 3 | 6 | 5 | 2 | 
| P3 | 2 | 8 | 6 | 22 | 20 | 12 |
| P4 | 3 | 6 | 9 | 20 | 17 | 11 |
| TOTAL |---|---|---|---| 56 | 34 |
| RATA-RATA |---|---|---|---| 14 | 8,5 |

| TAHAP 1 | TAHAP 2 | TAHAP 3 | 
|---------|----------|--------|
| P1 0-3,2 | P1 12-14,0 | P3 20-22,0 |
| P2 3-6,0 | P3 14-17,2 |------------|
| P3 6-9,5 | P4 17-20,0 |------------|
| P4 9-12,3|------------|------------|

- Gant chart 
```
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
0    3    6    9    12   14   17   20   22
```

2. Eksperiman priority scheduling 

| proses | priotity | arrival time | burst time | waktu mulai | waktu selesei | turnaround time | waiting time | 
|---------|--------------|------------|------------|----------------|-----------------|--------------|---------| 
| P1 | 2 | 0 | 5 | 0 | 5 | 5 | 0 |
| P2 | 1 | 1 | 3 | 5 | 8 | 7  | 4 |
| P4 | 3 | 2 | 6 | 8 | 14 | 11 | 5 |
| P3 | 4 | 3 | 8 | 14 | 22 | 20 | 12 | 
| total |---|---|---|---|---| 43 | 21 |
| rata-rata |---|---|---|---|---| 10,75 | 5,25 | 

3. tabel perbandingan 

| Algoritma | Avg Waiting Time |	Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|-----------------|----------------------|-----------|------------|
| RR | 8,5 | 14 | Adil terhadap semua proses |	Tidak efisien jika quantum tidak tepat |
| Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi starvation pada prioritas rendah |

---

## Kesimpulan
1. Round Robin membagi waktu secara adil untuk setiap proses.
RR memakai time quantum sehingga semua proses mendapat jatah eksekusi bergantian.
Hasilnya:

	 - Cocok untuk sistem time-sharing / multitasking
	 - Respons time cepat, tetapi
	 - Waiting time & turnaround time bisa besar jika quantum tidak   tepat.

2. Priority Scheduling memproses tugas berdasarkan tingkat prioritas, bukan urutan kedatangan.
Pada algoritma ini:

	 - Semakin kecil angka prioritas → semakin tinggi eksekusinya.
	 - Proses yang datang lebih dulu tidak selalu dieksekusi dulu (kecuali satu-satunya yang sudah datang).
	 - Bisa menimbulkan starvation, jika proses ber-prioritas rendah terus kalah.

3. Hasil TAT dan WT sangat dipengaruhi oleh jenis algoritma.
Dari perhitungan:

	 - RR membuat proses panjang tidak memonopoli CPU, tapi WT dan TAT beberapa proses bisa tinggi.
	 - Priority menghasilkan jalur eksekusi yang lebih teratur berdasarkan prioritas, sehingga WT/TAT dapat lebih optimal untuk prioritas tinggi.
	 - Pemilihan algoritma tergantung tujuan: fairness (RR) atau kepentingan proses (Priority).

---

## Quiz
1. Perbedaan Round Robin vs Priority Scheduling

Round Robin :
- Berbasis time quantum (waktu jatah).
- Proses dieksekusi bergiliran dalam antrian.
- Adil untuk semua proses.
- Cocok untuk time-sharing.
- Tidak ada starvation.

Priority Scheduling
- Berdasarkan nilai prioritas.
- Proses dengan prioritas tertinggi dieksekusi dulu.
- Bisa terjadi starvation (proses prioritas rendah menunggu lama).
- Bisa pakai aging untuk mencegah starvation.
- Cocok untuk tugas penting/real-time.

2. Pengaruh Time Quantum Terhadap Performa

    1. Time Quantum Terlalu Kecil
    - Terjadi context switching sangat sering.
    - Overhead meningkat → CPU banyak dipakai untuk gonta-ganti proses, bukan mengeksekusi.
    - Sistem terasa responsif, tapi efisiensi turun.

    2. Time Quantum Terlalu Besar

    - Mirip FCFS, karena proses bisa jalan lama sebelum bergiliran.
    - Responsivitas turun, terutama untuk banyak proses kecil.
    - Overhead context switching rendah → lebih efisien tetapi kurang adil.

3. karena CPU selalu memilih proses dengan prioritas tertinggi, sehingga jika proses berprioritas tinggi terus muncul, proses dengan prioritas rendah bisa tertunda sangat lama atau bahkan tidak pernah dieksekusi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
praktikum Round robin dan priority scheduling 

- Bagaimana cara Anda mengatasinya?  
memahami dan belajar google excel 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
