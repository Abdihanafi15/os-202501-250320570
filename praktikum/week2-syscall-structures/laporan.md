
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**   : Abdi Hanfi Alghifari 
- **NIM**    : 250320570
- **Kelas**  : 1DSRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- memahami dan menjelaskan konsep dan fungsi system call dalam sistem operasi
- Dapat menjelaskan ciri ciri system call 

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. pengertian system call 
2. fungsi system call dalam sistem operasi
3. Jenis-jenis system call yang umum digunakan (file, process, device, communication).
---

## Langkah Praktikum
- Setup Environment

  Gunakan Linux (Ubuntu/WSL).
  Pastikan perintah strace dan man sudah terinstal.
  Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).
  Eksperimen 1 – Analisis System Call Jalankan perintah berikut:

  strace ls
  Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.
  Simpan hasil analisis ke results/syscall_ls.txt.

- Eksperimen 2 – Menelusuri System Call File I/O Jalankan:

  strace -e trace=open,read,write,close cat /etc/passwd
  Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

- Eksperimen 3 – Mode User vs Kernel Jalankan:

  dmesg | tail -n 10
  Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

- Diagram Alur System Call

  Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
  Gunakan draw.io / mermaid.
  Simpan di:
  praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
  & Push

- git add .
 git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
 git push origin main


2. Perintah yang dijalankan. 
-  strace ls
- strace -e trace=open,read,write,close cat /etc/passwd
- dmesg | tail -n 10

3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
- strace ls
- strace -e trace=open,read,write,close cat /etc/passwd
- dmesg | tail -n 10

```

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:


![Screenshot hasil](<screenshots/screenshoot analisis strace ls.png>)

 Tabel hasil observasi strace ls

 | No | System Call | Fungsi Utama | Penjelasan / Analisis Singkat | 
 |----|--------------|--------------|--------------------------------|
 | 1  | execve("/usr/bin/ls", ["ls"], 0x7ffde63799a0) | Menjalankan program ls | Kernel menjalankan file biner /usr/bin/ls dengan argumen ls. Ini tahap awal proses eksekusi program. |
 | 2  | brk(NULL) | Mengecek batas awal memori heap | Digunakan untuk mempersiapkan area memori dinamis sebelum alokasi memori dilakukan. |
 | 3  | `mmap(NULL, 8192, PROT_READ | PROT_WRITE, MAP_PRIVATE |  MAP_ANONYMOUS, -1, 0) | 
 | 4  | access("/etc/ld.so.preload", R_OK) | Mengecek file preload library | Memastikan apakah ada library tambahan yang harus dimuat lebih dulu sebelum program utama. |
 | 5  | `openat(AT_FDCWD, “/etc/ld.so.cache”, O_RDONLY | O_CLOEXEC) | Membuka file cache library sistem |
 | 6  | fstat(3, {...}) | Mengecek status file descriptor | Mengambil metadata (jenis file, ukuran, izin) dari file yang baru dibuka. |
 | 7  | mmap(NULL, 354639, PROT_READ, MAP_PRIVATE, 3, 0) | Memetakan isi file ke memori | Memasukkan isi /etc/ld.so.cache ke memori agar bisa diakses tanpa baca ulang dari disk. |
 | 8  | close(3) | Menutup file descriptor | Menutup file cache setelah selesai dibaca. |
 | 9  | openat(AT_FDCWD, “/lib/x86_64-linux-gnu/libselinux.so.1\O_RDONLY | O_CLOEXEC)` | Membuka library SELinux |
 | 10 | read(3, "\177ELF\2\1\1...", 832) | Membaca isi awal file library | Mengecek format ELF dari library untuk memastikan bisa dieksekusi oleh sistem. | 




![Screenshot hasil](<screenshots/Screenshot_dmesg.png>)

 tabel Observasi dmesg 

 | Aspek | dmesg(Log Kernel) | Output Program Biasa | 
 |--------|-------------------|------------------------|
 | Sumber data | Kernel Linux (sistem operasi) | Program user (misalnya cat, ls, python) | 
 | Isi | Pesan status sistem, error kernel, aktivitas hardware, system call gagal | Hasil langsung dari program (teks, perhitungan, tampilan data) |
 | Level operasi | Kernel space | User space |
 | Akses | Biasanya butuh izin root (administrator) | Bisa diakses user biasa |
 | Tujuan | Untuk debugging atau memonitor aktivitas kernel | Untuk menampilkan hasil kerja program ke pengguna |
 | Contoh isi | [ 12.3] audit: apparmor="DENIED" operation="open" profile="/usr/bin/cat" | root:x:0:0:root:/root:/bin/bash | 

---

## Analisis

- strace -e trace=open,read,write,close cat /etc/passwd

  - system call open() > open("/etc/psswd", O_RDONLY) = 3
  artinya: kernel membuka file/etc/passwd dalam hasil= 3 berarti  file descriptor (FD) untuk file ini adalah 3 
  FD= stdin, 1=stdout, 2=stderr, jadi 3 adalah file yang baru dibuka, kenapa open tidak muncul dihasilny? karena sistem ini pakai openat() bukan open()
  Di sistem Linux yang lebih baru (termasuk yang dipakai Google Cloud Shell),
  open() sudah digantikan oleh system call openat().
  Jadi, walaupun kamu menulis -e trace=open,..., kernel sebenarnya memanggil openat() untuk membuka file, dan karena openat tidak termasuk dalam filter open, maka tidak muncul di hasil.
  openat() berfungsi sama seperti open(), hanya saja lebih fleksibel (bisa membuka file relatif terhadap direktori tertentu).

 -  system call read() read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 131072) = 1425. Kernel membaca 1425 byte data dari file descriptor 3 (/etc/passwd) ke buffer program.
 Isi datanya adalah konten file /etc/passwd, yang kemudian akan ditampilkan ke layar.

 - system call write() write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1425root:x:0:0:root:/root:/bin/bash. File descriptor 1 = stdout (layar).
 Artinya kernel menulis 1425 byte ke layar.

 - system call close() close(3) = 0 Setelah selesai, program cat meminta kernel menutup file descriptor 3.
 Nilai 0 menunjukkan operasi berhasil.


 diagram alur syscall

![Screenshot hasil](<screenshots/Diagram_ syscall.png>)

---

- Tulis analisis 400–500 kata tentang:

1. Mengapa system call penting untuk keamanan OS?

karena berfungsi sebagai jembatan antara program aplikasi (user mode) dan kernel (privileged mode). System call tidak hanya memungkinkan aplikasi meminta layanan OS, tetapi juga menjaga keamanan, stabilitas, dan efisiensi seluruh sistem komputer.
  Berikut adalah alasan utama mengapa system call sangat penting dalam OS:
     - Isolasi dan Keamanan
       Aplikasi berjalan di user mode, yang tidak memiliki akses langsung ke perangkat keras atau memori sistem. Hal ini dilakukan untuk alasan keamanan dan proteksi. System call memungkinkan aplikasi berinteraksi dengan kernel yang memiliki kontrol penuh atas hardware, namun dengan pembatasan dan validasi yang ketat. Ini mencegah aplikasi melakukan operasi berbahaya atau ilegal.

       Contoh: Aplikasi tidak bisa langsung menulis ke disk, tapi bisa memanggil system call write() yang akan diverifikasi dan dijalankan oleh kernel jika aman.
     - Kontrol Terpusat atas Sumber Daya
       System call memberikan OS kendali penuh atas penggunaan sumber daya seperti CPU, RAM, file, jaringan, dan perangkat I/O lainnya. Setiap permintaan aplikasi harus melalui kernel, yang kemudian:
       - Memeriksa izin akses
       - Menjadwalkan penggunaan CPU
       - Mengelola memori agar tidak saling tumpang tindih
       - Menangani file dengan aman dan sinkron
       Tanpa system call, tidak ada kontrol atas bagaimana sumber daya digunakan, yang dapat menyebabkan konflik, kebocoran data, atau kerusakan sistem. 

     - Stabilitas dan Reliabilitas
       System call menjaga stabilitas sistem karena kernel dapat menangani kesalahan secara terpusat. Jika aplikasi melakukan kesalahan, kernel dapat menolaknya tanpa memengaruhi proses lain atau seluruh sistem. Kernel juga dapat memastikan bahwa semua operasi berjalan dalam urutan yang benar dan tidak saling mengganggu.
 
     - Dasar Komunikasi dan Sinkronisasi 
     System call juga digunakan untuk komunikasi antar proses (IPC) dan sinkronisasi antar thread. Ini penting dalam sistem multitasking dan multiproses agar semua proses dapat berjalan bersamaan tanpa saling mengganggu.  


2. Bagaimana OS memastikan transisi user–kernel berjalan aman?
 
  - Penggunaan Mode Eksekusi (User Mode & Kernel Mode)
    CPU bekerja dalam dua mode utama:
      User mode: untuk menjalankan aplikasi biasa, dengan akses terbatas.
      Kernel mode: untuk menjalankan kode sistem operasi, dengan akses penuh ke perangkat keras dan memori.
    Aplikasi hanya bisa masuk ke kernel mode melalui mekanisme resmi seperti system call. CPU mencegah akses langsung dari user mode ke kernel mode, sehingga aplikasi tidak bisa sembarangan mengakses bagian sensitif sistem.

  - System Call (Pintu Masuk yang Terkontrol)
    System call adalah satu-satunya cara aplikasi berinteraksi dengan kernel. Ketika aplikasi ingin menggunakan layanan OS, seperti membuka file atau mengirim data, ia memanggil system call.

    Panggilan ini menyebabkan trap, yaitu interupsi lunak yang memberitahu CPU untuk berpindah ke kernel mode. CPU kemudian menjalankan handler system call yang telah ditentukan OS, bukan kode yang dikirim dari user.

    Ini memastikan bahwa hanya jalur yang aman dan tervalidasi yang digunakan untuk masuk ke kernel.


  - Validasi Parameter oleh Kernel
    Saat system call dipanggil, semua parameter dari user space akan diperiksa oleh kernel:

    Apakah pointer valid?
    Apakah ukuran data sesuai?
    Apakah proses punya izin untuk melakukan tindakan itu?
    Jika ada hal yang mencurigakan atau tidak sah, kernel akan menolak system call tersebut. Ini mencegah kesalahan atau serangan seperti buffer overflow dan pointer palsu.

  - Isolasi Memori (Memory Protection)
    Sistem operasi memanfaatkan virtual memory untuk mengisolasi ruang memori antara aplikasi dan kernel. Proses di user mode tidak bisa membaca atau menulis data milik kernel secara langsung.

    Jika aplikasi mencoba mengakses memori kernel, CPU akan memicu pelanggaran memori (segmentation fault), dan proses tersebut akan dihentikan.

  - Tabel System Call dan Akses Terbatas
    Kernel hanya menyediakan akses ke fungsi tertentu melalui tabel system call. Aplikasi tidak bisa menjalankan sembarang fungsi kernel, hanya yang tersedia dalam tabel tersebut.
    Dengan membatasi akses hanya pada fungsi yang aman, OS mengurangi risiko eksploitasi.

  - Level Privilege CPU (Ring 0 - Ring 3)
    Pada arsitektur seperti x86, CPU memiliki empat level hak akses (ring):

    Ring 0: untuk kernel

    Ring 3: untuk aplikasi

    Transisi dari Ring 3 ke Ring 0 hanya bisa terjadi melalui jalur resmi seperti system call atau interrupt. Ini adalah proteksi level hardware yang sangat efektif.

  - Kembali ke User Mode Secara Aman
    Setelah system call selesai, kernel akan mengembalikan kontrol ke aplikasi melalui instruksi khusus, memastikan register, memori, dan stack dalam keadaan bersih dan aman.



3. Sebutkan contoh system call yang sering digunakan di Linux.

- read()
Fungsi: Membaca data dari file atau input (seperti keyboard).
Kenapa sering? Hampir semua aplikasi perlu membaca data — baik dari file, socket, atau stdin.

- write()
Fungsi: Menulis data ke file, terminal, atau jaringan.
Kenapa sering? Digunakan untuk mencetak ke layar atau menyimpan data ke file.

- open()
Fungsi: Membuka file dan mengembalikan file descriptor.
Kenapa sering? Semua akses file, log, konfigurasi, atau data dimulai dari sini.

- close()
Fungsi: Menutup file descriptor yang sudah dibuka.
Kenapa sering? Digunakan setiap kali file atau resource selesai digunakan.

- execve()
Fungsi: Menjalankan program baru (mengganti proses saat ini dengan program baru).
Kenapa sering? Digunakan oleh shell saat mengeksekusi perintah seperti ls, cat, dll.

- fork()
Fungsi: Membuat proses baru (anak).
Kenapa sering? Banyak program (terutama shell) menggunakan ini untuk menjalankan proses baru.

- wait() / waitpid()
Fungsi: Menunggu proses anak selesai.
Kenapa sering? Digunakan setelah fork() untuk sinkronisasi.

- stat() / fstat() / lstat()
Fungsi: Mengambil informasi file (ukuran, tipe, waktu akses).
Kenapa sering? Digunakan oleh shell, editor, dan manajer file untuk menampilkan info file.

- mmap()
Fungsi: Memetakan file atau memori ke ruang alamat proses.
Kenapa sering? Digunakan untuk efisiensi akses file besar dan oleh malloc() di belakang layar.

- brk() / sbrk()
Fungsi: Mengatur batas heap proses.
Kenapa sering? Digunakan oleh sistem alokasi memori (seperti malloc), meski sekarang lebih banyak digantikan oleh mmap().


## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

1. strace digunakan untuk memantau dan menampilkan system call yang dilakukan oleh program, sehingga kita dapat mengetahui bagaimana program berinteraksi dengan kernel saat dijalankan.
2. dmesg menampilkan log aktivitas kernel, seperti deteksi perangkat, error sistem, dan pesan kernel saat proses berjalan.
3. Melalui kedua perintah ini, kita dapat memahami bahwa setiap perintah di Linux selalu melalui lapisan kernel, dan strace serta dmesg membantu menganalisis proses serta mendeteksi kesalahan sistem dengan lebih detail.

---

## Quiz
1. [Pertanyaan 1. Apa fungsi utama system call dalam sistem operasi?]  
   **Jawaban:**

   - Akses Terhadap Sumber Daya Sistem
   - Pengelolaan Proses
   - Manajemen Memori
   - Komunikasi Antar Proses (IPC)
   - Keamanan dan Proteksi
   - Abstraksi Hardware


2. [Pertanyaan 2. Sebutkan 4 kategori system call yang umum digunakan.]  
   **Jawaban:** 


   1. System Call untuk Manajemen Proses (Process Control)
    Digunakan untuk mengelola proses dalam sistem, seperti membuat, menjalankan, atau mengakhiri proses.

     Contoh:
   - fork() – membuat proses baru
   - exec() – menjalankan program baru dalam proses
   - exit() – keluar dari proses
   - wait() – menunggu proses anak selesai


   2. System Call untuk Manajemen File (File Management)
    Digunakan untuk melakukan operasi pada file dan direktori, seperti membuka, membaca, atau menulis file.
   
     Contoh:
   - open() – membuka file
   - read() – membaca isi file
   - write() – menulis ke file
   - close() – menutup file  
   - unlink() – menghapus file

   
   3. System Call untuk Manajemen Memori (Memory Management)
    Digunakan untuk mengatur alokasi dan penggunaan memori oleh proses.

     Contoh:
   - brk() – mengatur batas akhir area data proses (heap)
   - mmap() – memetakan file atau perangkat ke memori
   - munmap() – melepaskan pemetaan memori


   4. System Call untuk Komunikasi Antar Proses (Interprocess
    Communication / IPC)
    Digunakan agar proses dapat bertukar data dan berkoordinasi.

     Contoh:
   - pipe() – membuat saluran komunikasi antar proses
   - shmget() – mendapatkan segmen memori bersama (shared memory)
   - msgget() – membuat/mendapatkan antrean pesan
   - socket() – komunikasi antar proses melalui jaringan




3. [Pertanyaan 3. Mengapa system call tidak bisa dipanggil langsung oleh user program? ]  
   **Jawaban:** 
   - Keamanan Sistem
   - Perlindungan Kernel Space
   - Validasi & Pengendalian Akses
   - Konsistensi dan Stabilitas


Kesimpulan:

Program pengguna tidak bisa memanggil system call secara langsung karena:

- Harus melalui transisi dari user mode ke kernel mode.
- Butuh validasi, keamanan, dan kontrol dari OS.
- CPU dan OS dirancang untuk melindungi kernel dari akses langsung. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
 
  Yang menantang adalah cara bagaimana memahami syscall dan fungsi fungsi syscall karena ternyata system operasi sangat luas jangkauannya.


- Bagaimana cara Anda mengatasinya?  
 
  cara mengatasinya harus konsisten dalam memahami syscall dan operaasi sistem, juga memiliki rasa ingin tahu yang tinggi supaya terbiasa dan menjadi mudah.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_


[def]: screenshots