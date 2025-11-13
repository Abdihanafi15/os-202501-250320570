
# Laporan Praktikum Minggu [X]
Topik: [Manajemen Proses dan User di Linux]

---

## Identitas
- **Nama**  : Abdi Hanafi Alghifari
- **NIM**   : 250320570
- **Kelas** : 1DSRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

> Dapat memahami, mengimplementasikan, dan menganalisis kinerja kedua algoritma penjadwalan CPU (CPU Scheduling) 
  - FCFS (First Come First Served)
  - SJF (Shortest Job First)

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1. FCFS (First Come First Served): Algoritma penjadwalan CPU yang melayani proses berdasarkan urutan kedatangan, yaitu proses yang datang pertama kali akan dilayani pertama kali.

2. SJF (Shortest Job First): Algoritma penjadwalan CPU yang melayani proses berdasarkan waktu eksekusi terpendek, yaitu proses dengan waktu eksekusi terpendek akan dilayani pertama kali.

3. Algoritma penjadwalan CPU (CPU Scheduling) 
  - FCFS (First Come First Served)
  - SJF (Shortest Job First)

4. Penjadwalan CPU: Proses pengelolaan dan pengalokasian waktu CPU untuk menjalankan proses-proses yang ada di sistem operasi.

---

## Langkah Praktikum
- Langkah-langkah yang dilakukan :

1. Siapkan Data Proses Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):

| Proses | Burst Time |	Arrival Time |
|---------|------------|--------------|
| P1 | 6 | 0 |
| P2 | 8 | 1 |
| P3 | 7 | 2||
| P4 | 3 | 3 | 

2. Eksperimen 1 – FCFS (First Come First Served)

- Urutkan proses berdasarkan Arrival Time.
- Hitung nilai berikut untuk tiap proses:

       Waiting Time (WT) = waktu mulai eksekusi - Arrival Time

       Turnaround Time (TAT) = WT + Burst Time

- Hitung rata-rata Waiting Time dan Turnaround Time.
- Buat Gantt Chart sederhana:

       | P1 | P2 | P3 | P4 |
       0    6    14   21   24

3. Eksperimen 2 – SJF (Shortest Job First)

- Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan).
- Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.

- Bandingkan hasil FCFS dan SJF pada tabel berikut:

| Algoritma |	Avg Waiting Time |	Avg Turnaround Time |	Kelebihan |	Kekurangan |
|-----------|--------------------|-----------------------|---------|------------------------|
|FCFS |	... |	... |	Sederhana dan mudah diterapkan |	Tidak efisien untuk proses panjang |
| SJF |	... |	... | Optimal untuk job pendek |	Menyebabkan starvation pada job panjang | 

4. Eksperimen 3 – Visualisasi Spreadsheet (Opsional)

- Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
   - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
   - Gunakan formula dasar penjumlahan/subtraksi.
- Screenshot hasil perhitungan dan simpan di:

       praktikum/week5-scheduling-fcfs-sjf/screenshots/
       
5. Analisis
- Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.
- Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.
- Tambahkan kesimpulan singkat di akhir laporan.

6. Commit & Push

       git add .
       git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
       git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
       Waiting Time (WT) = waktu mulai eksekusi - Arrival Time

       Turnaround Time (TAT) = WT + Burst Time

```

---
## Tugas 

- 2 skenario FCFS dan SJF



## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/)

---

## Analisis


---

## Kesimpulan

1. Algoritma FCFS (First Come First Served) mengeksekusi proses berdasarkan urutan kedatangan — proses yang datang lebih dulu akan dijalankan lebih dulu tanpa interupsi.

2. Algoritma SJF (Shortest Job First) memilih proses dengan waktu eksekusi (burst time) paling pendek terlebih dahulu, sehingga waktu tunggu rata-rata biasanya lebih kecil dibanding FCFS.

3. Hasil percobaan menunjukkan bahwa SJF menghasilkan rata-rata waiting time dan turnaround time lebih rendah dibanding FCFS, karena proses pendek diprioritaskan lebih awal.

4. Kelemahan FCFS adalah bisa terjadi convoy effect (proses cepat menunggu proses panjang), sedangkan kelemahan SJF adalah kemungkinan starvation (proses panjang terus tertunda).

5. Secara umum, SJF lebih efisien dalam penggunaan CPU, tetapi FCFS lebih sederhana dan mudah diimplementasikan karena tidak memerlukan perkiraan burst time proses.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?

   **Jawaban:**  
   Perbedaan utama antara algoritma FCFS (First Come First Served dan SJF (Shortest Job First) terletak pada cara menentukan urutan eksekusi proses. Pada FCFS, proses dijalankan berdasarkan urutan kedatangan, jadi siapa yang datang lebih dulu akan dieksekusi lebih dulu. Sedangkan pada SJF, proses yang memiliki waktu eksekusi (burst time) paling singkat akan mendapat prioritas lebih dulu. Secara umum, SJF lebih efisien karena mampu menghasilkan waktu tunggu rata-rata yang lebih kecil dibanding FCFS. Namun, FCFS lebih sederhana untuk diterapkan, sementara SJF membutuhkan perkiraan burst time yang akurat dan berisiko menyebabkan starvation pada proses yang durasinya lebih lama.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?

   **Jawaban:**  
   karena algoritma ini selalu menjalankan proses dengan burst time paling pendek terlebih dahulu, sehingga proses-proses cepat tidak perlu menunggu proses yang lama selesai. Akibatnya, total waktu tunggu semua proses menjadi lebih kecil, dan rata-ratanya pun menjadi minimum.

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  
   **Jawaban:**  
   - Kelemahan SJF pada Sistem Interaktif:

1. Sulit memperkirakan burst time — pada sistem interaktif, waktu eksekusi proses sering berubah-ubah, sehingga sulit menentukan proses mana yang paling singkat.

2. Berpotensi menyebabkan starvation — proses dengan burst time panjang bisa terus tertunda jika selalu ada proses singkat yang datang lebih dulu.

3. Tidak cocok untuk kebutuhan respon cepat — sistem interaktif memerlukan keadilan dan waktu respon yang stabil, sedangkan SJF cenderung lebih fokus pada efisiensi total daripada kecepatan respon tiap proses.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
cara memahami scheduling CPU dan membuat table perhitungan FCFS dan SJF

- Bagaimana cara Anda mengatasinya?  
Selalu mencoba dan mengulangi 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
