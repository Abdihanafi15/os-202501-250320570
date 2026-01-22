
# Laporan Praktikum Minggu [12]
Topik: [Virtualisasi Menggunakan Virtual Machine]

---

## Identitas
- **Nama**  : [Abdi Hanafi Alghifari]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan
1. Memahami konsep dasar virtualisasi dan cara kerja virtual machine.

2. Mengetahui peran hypervisor dalam menjalankan lebih dari satu sistem operasi pada satu perangkat fisik.

3. Melakukan instalasi dan konfigurasi sistem operasi tamu (guest OS) pada virtual machine.

4. Menganalisis kelebihan virtualisasi dalam efisiensi penggunaan sumber daya perangkat keras.

5. Menerapkan virtualisasi sebagai solusi untuk pengujian sistem, pembelajaran, dan simulasi lingkungan jaringan. 

---

## Dasar Teori
1. Virtualisasi
Virtualisasi adalah teknologi yang memungkinkan satu komputer fisik menjalankan beberapa sistem operasi secara bersamaan dengan membagi sumber daya perangkat keras secara virtual.
2. Virtual Machine (VM)
Virtual machine adalah komputer virtual yang memiliki sistem operasi, CPU, memori, dan penyimpanan sendiri, namun berjalan di atas satu mesin fisik.
3. Isolasi Sistem
Setiap virtual machine berjalan secara terpisah sehingga gangguan pada satu VM tidak memengaruhi VM lainnya.
4. Manajemen Sumber Daya
Virtualisasi memungkinkan pengaturan penggunaan CPU, RAM, dan storage agar lebih efisien dan fleksibel.

---

## Langkah Praktikum
1. Instalasi Virtual Machine

- Instal VirtualBox atau VMware pada komputer host.
- Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. Pembuatan OS Guest
- Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).
- Atur resource awal:
       - CPU: 1–2 core
       - RAM: 2–4 GB
       - Storage: ≥ 20 GB

3. Instalasi Sistem Operasi

- Jalankan proses instalasi OS guest sampai selesai.
- Pastikan OS guest dapat login dan berjalan normal.

4. Konfigurasi Resource

- Ubah konfigurasi CPU dan RAM.
- Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. Analisis Proteksi OS

- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
- Kaitkan dengan konsep sandboxing dan hardening OS.

6. Dokumentasi

- Ambil screenshot setiap tahap penting.
- Simpan di folder screenshots/.

7. Commit & Push

       git add .
       git commit -m "Minggu 12 - Virtual Machine"
       git push origin main

---

## Kode / Perintah
```bash

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
 

---

## Kesimpulan


---

## Quiz
1. [Apa perbedaan antara host OS dan guest OS?]   

Host OS adalah sistem operasi utama yang berjalan pada komputer fisik, sedangkan guest OS adalah sistem operasi yang berjalan di dalam virtual machine.

2. [Apa peran hypervisor dalam virtualisasi?]

Hypervisor berfungsi mengelola virtual machine dan membagi sumber daya perangkat keras agar dapat digunakan oleh setiap VM


3. [Mengapa virtualisasi meningkatkan keamanan sistem?]

Virtualisasi meningkatkan keamanan karena setiap virtual machine terisolasi, sehingga gangguan atau serangan pada satu sistem tidak memengaruhi sistem lainnya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
