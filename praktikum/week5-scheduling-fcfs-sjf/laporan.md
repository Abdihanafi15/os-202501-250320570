
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

> Mampu menjelaskan konsep proses dan user dalam sistem operasi Linux dan Menggunakan perintah untuk membuat dan mengelola user.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1. Konsep proses dan user dalam sistem operasi Linux.
2. Fungsi proses init atau systemd dalam sistem Linux.
3. Hubungan antara user management dan keamanan sistem Linux.
4. Mengelola user, group, serta hak akses pengguna.
---

## Langkah Praktikum
- Langkah-langkah yang dilakukan.  

1. Setup Environment

- Gunakan Linux (Ubuntu/WSL).
- Pastikan Anda sudah login sebagai user non-root.
    Siapkan folder kerja:

       praktikum/week4-proses-user/

2. Eksperimen 1 – Identitas User Jalankan perintah berikut:

       whoami
       id
       groups

- Jelaskan setiap output dan fungsinya.
- Buat user baru (jika memiliki izin sudo):

      sudo adduser praktikan
      sudo passwd praktikan

- Uji login ke user baru.

2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
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
