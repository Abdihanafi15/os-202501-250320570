
# Laporan Praktikum Minggu [13]
Topik: [Docker – Resource Limit (CPU & Memori)]

---

## Identitas
- **Nama**  : [ABDI HANAFI ALGHIFARI]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan
1. Memahami cara membatasi penggunaan CPU pada container Docker.

2. Memahami cara membatasi penggunaan memori pada container Docker.

3. Mempelajari perbedaan penggunaan resource pada container dan sistem host.

4. Menganalisis dampak limit CPU dan memori terhadap performa aplikasi dalam container.

5. Menerapkan pengaturan resource limit untuk mencegah container menghabiskan sumber daya host.

---

## Dasar Teori
1. DOCKER 
 
 Docker adalah platform untuk menjalankan aplikasi dalam container yang bersifat ringan dan terisolasi.

Container menggunakan kernel host, sehingga lebih efisien dibanding virtual machine.

2. Resource Limit

Resource limit adalah batasan penggunaan CPU dan memori yang diberikan pada container agar tidak mengganggu sistem host.

3. CPU Limit

- Docker dapat membatasi jumlah CPU core atau persentase CPU yang digunakan container.

- Contoh pengaturan:

        --cpus="1.5" → membatasi container menggunakan maksimal 1,5 core.

        --cpu-shares → prioritas penggunaan CPU.

2. Memory Limit

- Docker dapat membatasi jumlah memori RAM yang boleh dipakai container.

- Contoh pengaturan:

       --memory="512m" → membatasi memori maksimal 512 MB.

       --memory-swap → batas total memori + swap.

---

## Langkah Praktikum
1. Persiapan Lingkungan

- Pastikan Docker terpasang dan berjalan.
- Verifikasi:
        docker version
        docker ps

2. Membuat Aplikasi/Skrip Uji

Buat program sederhana di folder code/ (bahasa bebas) yang:

- Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
- Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. Membuat Dockerfile

- Tulis Dockerfile untuk menjalankan program uji.
- Build image:
        docker build -t week13-resource-limit .

4. Menjalankan Container Tanpa Limit

- Jalankan container normal:
        docker run --rm week13-resource-limit
        
- Catat output/hasil pengamatan.

5. Menjalankan Container Dengan Limit Resource

- Jalankan container dengan batasan resource (contoh):

        docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit

- Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. Monitoring Sederhana

- Jalankan container (tanpa --rm jika perlu) dan amati penggunaan resource:
        docker stats
- Ambil screenshot output eksekusi dan/atau docker stats.

7. Commit & Push

       git add .
       git commit -m "Minggu 13 - Docker Resource Limit"
       git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
