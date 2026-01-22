
# Laporan Praktikum Minggu [15]
Topik: [Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)"]

---

## Identitas
- **Nama**  : [ABDI HANAFI ALGHIFARI]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan
Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
1. CPU Scheduling mengatur urutan eksekusi proses agar penggunaan CPU efisien.
2. FCFS dan SJF adalah algoritma penjadwalan CPU, di mana SJF menghasilkan waktu tunggu rata-rata lebih kecil dibanding FCFS.
3. Page Replacement FIFO dan LRU digunakan untuk mengelola memori virtual, dengan LRU umumnya menghasilkan page fault lebih sedikit dibanding FIFO.

---
## LATAR BELAKANG

Latar Belakang Dalam sistem operasi, CPU dan memori merupakan sumber daya utama yang harus dikelola secara efisien. Sistem operasi menggunakan algoritma penjadwalan CPU untuk menentukan urutan eksekusi proses dan algoritma page replacement untuk mengelola memori virtual Untuk memahami konsep tersebut secara praktis, diperlukan simulasi algoritma scheduling dan page replacement dalam sebuah aplikasi sederhana yang dapat dijalankan secara konsisten menggunakan Docker.

---
## TUJUAN PROYEK

Tujuan Proyek
1. Mengimplementasikan algoritma CPU Scheduling FCFS dan SJF (non-preemptive).
2. Mengimplementasikan algoritma Page Replacement FIFO dan LRU.
3. Menghitung dan menampilkan metrik kinerja sistem.
4. Menjalankan aplikasi dalam lingkungan container Docker agar terisolasi dan konsisten.

---
## ARSITEKTUR APLIKASI (MODUL & ALUR DATA)

    Struktur Modul Proyek
    │
    ├── main.py
    │
    ├── scheduling.py
    │   ├── fcfs()   # Implementasi algoritma First Come First Serve
    │   └── sjf()    # Implementasi algoritma Shortest Job First
    │
    ├── pagereplacement.py
    │   ├── fifo()   # Implementasi algoritma Page Replacement FIFO
    │   └── lru()    # Implementasi algoritma Page Replacement LRU
    │
    └── Dockerfile   # Konfigurasi container Docker untuk menjalankan aplikasi

- Fungsi Tiap Modul A. main.py

1. Menyediakan menu CLI.
2. Mengatur pemanggilan algoritma berdasarkan pilihan user. B. scheduling.py
3. fcfs() menghitung waiting time dan turnaround time berdasarkan urutan kedatangan.
4. sjf() memilih proses dengan burst time terkecil yang sudah datang. C. pagereplacement.py
5. fifo() mengganti halaman berdasarkan urutan masuk.
6. lru() mengganti halaman yang paling lama tidak digunakan.

- Alur Data

1. User memilih menu di CLI. 
2. Data proses / page reference diambil dari variabel Python. 
3. Algoritma dijalankan sesuai pilihan. 
4. Output ditampilkan dalam bentuk tabel dan metrik ringkasan.
---
## Demo Menjalankan Aplikasi (Docker)

1. Build Image docker build -t os-simulator .
![Screenshot hasil](screenshots/Docker%20Build%20.png)

2. Menjalankan Container docker run -it --rm os-simulator
![Screenshot hasil](screenshots/Docker%20run.png)

- Yang Ditunjukkan Saat Demo Menu aplikasi muncul Menjalankan FCFS / SJF Menjalankan FIFO / LRU adalah Output tabel dan metrik tampil di terminal

3. OUTPUT FCFS
![Screenshot hasil](screenshots/FCFS%20scheduling%20.png)

4. OUPUT SJF 

    ![Screenshot hasil](screenshots/SJF%20scheduling%20.png)


5. OUTPUT FIFO 
![Screenshot hasil](screenshots/Output%20FIFO.png)

6. OUTPUT LRU 
![Screenshot hasil](screenshots/Output%20LRU.png)

---
## HASIL PENGUJIAN & ANALISIS

A. CPU Scheduling

- Metrik

| Algoritma |	Average Waiting Time | 	Average Turnaround Time |
|------------|-----------------------|--------------------------|
| FCFS (First Come First Serve) | Lebih besar |	Lebih besar |
| SJF (Shortest Job First)	| Lebih kecil | Lebih kecil |

- Analisis
1. FCFS sederhana tetapi tidak mempertimbangkan burst time.
2. SJF meminimalkan waiting time rata-rata dengan memilih proses terpendek.
3. SJF lebih efisien namun berpotensi starvation.


B. Page Replacement

Metrik 

| Algoritma |	Page Fault |	Hit Ratio |
|------------|--------------|------------|
| FIFO (First In First Out) |	Lebih banyak |	Lebih kecil |
| LRU (Least Recently Used) |	Lebih sedikit | Lebih besar |


Analisis

- FIFO tidak memperhatikan pola penggunaan halaman.
- LRU lebih adaptif karena mempertimbangkan histori akses.
- LRU memberikan performa memori yang lebih baik.

---

## PEMBAGIAN PERAN DAN KONTRIBUSI ANGGOTA KELOMPOK

| No	| Nama |	Peran	Kontribusi |
|------|------|------------------|
| 1 |	Aldiman |	Project Lead	Koordinasi tim, integrasi kode, build Docker |
| 2 | Alfan Nur Fadzilah |	Developer 1	Implementasi algoritma FCFS & SJF |
| 3 |	Abdi Hanafi Alghifari |	Developer 2	Implementasi algoritma FIFO & LRU |
| 4 |	Abdi Hanafi  |	Dokumentasi & QA	Testing, penulisan README, pengambilan screenshot |

---


## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?] 

   menyatukan modul scheduling.py dan pagereplacement.py ke dalam main.py agar format input–output konsisten.
  
2. [Mengapa Docker membantu proses demo dan penilaian proyek?]  
   
   Docker memastikan aplikasi berjalan pada lingkungan yang sama di semua perangkat tanpa masalah dependensi.

3. [Jika dataset diperbesar 10x, modul mana yang paling terdampak    performanya? Jelaskan.]  

   Modul yang paling terdampak adalah Page Replacement LRU, karena LRU memerlukan pencatatan histori akses halaman yang kompleks  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
