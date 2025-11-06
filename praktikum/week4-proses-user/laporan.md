
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : ABDI HANAFI ALGHIFARI
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

-  Uji login ke user baru.
      

3. Eksperimen 2 – Monitoring Proses Jalankan:

       ps aux | head -10
       top -n 1

- Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
  Simpan tangkapan layar top ke:

       praktikum/week4-proses-user/screenshots/top.png


4. Eksperimen 3 – Kontrol Proses

- Jalankan program latar belakang:

       sleep 1000 &
       ps aux | grep sleep

- Catat PID proses sleep.
- Hentikan proses:

       kill <PID>

- Pastikan proses telah berhenti dengan ps aux | grep sleep. 

5. Eksperimen 4 – Analisis Hierarki Proses Jalankan:

        pstree -p | head -20


        
- Amati hierarki proses dan identifikasi proses induk (init/systemd).
- Catat hasilnya dalam laporan.

6. Commit & Push

       git add .
       git commit -m "Minggu 4 - Manajemen Proses & User"
       git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

       whoami
       id
       groups

       sudo adduser praktikan
       sudo passwd praktikan

       ps aux | head -10
       top -n 1

       sleep 1000 &
       ps aux | grep sleep

       kill <PID>

       pstree -p | head -20

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram :

Eksperimen 1 – Identitas User Jalankan perintah berikut:
![Screenshot hasil](screenshots/Screenshot.top%20(4).png)
![Screenshot hasil](screenshots/Screenshot.top%20(5).png)

| Perintah | Output | Fungsi / Penjelasan |
|------------|-------|----------------------|
| whoami | abdihanafi78 | Menampilkan nama user yang sedang login ke sistem. | 
| id | uid=1000(abdihanafi78) gid=1000(abdihanafi78) groups=1000(abdihanafi78),4(adm),27(sudo),996(docker) | Menampilkan identitas lengkap user: • uid → ID unik user.• gid → ID grup utama user.• groups  → daftar grup yang diikuti user beserta ID-nya. |
| groups | abdihanafi78 adm sudo docker | Menampilkan nama-nama grup tempat user tergabung tanpa menampilkan ID-nya. |

- Buat user baru (jika memiliki izin sudo):


| Baris output | Arti / Fungsi |
|---------------|----------------|
| sudo adduser praktikan | Menjalankan perintah untuk membuat user baru bernama praktikan dengan hak akses sudo. |
| Adding user 'praktikan' ... | Sistem sedang memulai proses pembuatan user baru. |
| Selecting UID/GID from range 1000 to 59999 ... | Sistem otomatis memilih User ID (UID) dan Group ID (GID) unik untuk user baru. |
| Adding new group 'praktikan' (1001) ... | Sistem membuat grup baru dengan nama yang sama (praktikan) dan ID grup 1001. |
| Adding new user 'praktikan' (1001) with group 'praktikan' (1001) ... | Sistem menambahkan user praktikan ke grup utamanya sendiri (praktikan). |
| Creating home directory '/home/praktikan' ... | Sistem membuat folder home untuk user baru di /home/praktikan. Folder ini berisi file dan konfigurasi pribadi user tersebut. |
| Copying files from '/etc/skel' ... | Sistem menyalin file konfigurasi default dari /etc/skel ke direktori home user baru. File ini termasuk .bashrc, .profile, dll, yang digunakan saat pertama kali login. |
| sudo passwd praktikan (perintah berikutnya) | Digunakan untuk mengatur password bagi user praktikan. Sistem akan meminta kamu mengetik dan mengonfirmasi password baru. |

- Eksperimen 2 – Monitoring Proses Jalankan:

![Screenshot hasil](screenshots/Screenshot.top%20(3).png)
![Screenshot hasil](screenshots/Screenshot.top%20(2).png)

| Kolom | Makna | Fungsi | 
|--------|-------|---------|
| PID | Process ID yaitu nomor identitas unik yang diberikan sistem untuk setiap proses yang berjalan. | untuk mengenali, memantau, atau mengontrol proses tertentu. Misalnya digunakan dalam perintah kill PID untuk menghentikan proses tertentu. |
| USER | Menunjukkan nama pengguna (user) yang menjalankan proses tersebut. | Berfungsi untuk mengetahui siapa pemilik atau sumber proses itu, apakah dijalankan oleh user biasa (misal abdi) atau oleh sistem (root). |
| %CPU | Persentase penggunaan CPU oleh proses tertentu. | Berfungsi untuk memantau seberapa besar beban prosesor yang digunakan oleh proses tersebut, membantu mengidentifikasi proses yang menghabiskan banyak sumber daya CPU. |
| %MEM | Persentase penggunaan memori (RAM) oleh proses tertentu | Berfungsi untuk mengetahui berapa banyak kapasitas memori yang sedang dipakai oleh proses itu, membantu mengevaluasi efisiensi penggunaan RAM. |
| COMMAND | Nama program, aplikasi, atau perintah yang dijalankan | Berfungsi untuk menampilkan proses atau aplikasi apa yang sedang aktif di sistem, sehingga pengguna tahu program apa yang menggunakan sumber daya. | 


- Eksperimen 3 – Kontrol Proses

![Screenshot hasil](screenshots/Screenshot.top%20.png)

 PID yang dicatat pada baris sleep adalah 11024

- Eksperimen 4 – Analisis Hierarki 

![Screenshot hasil](screenshots/Screenshot.top%206.png)

- Amati hierarki proses dan identifikasi proses induk (init/systemd).

 Analisis Hierarki Proses :

 1. Proses Utama / Induk:
	•	Proses tertinggi yang terlihat adalah bash(1).
	•	Biasanya, proses tertinggi di sistem Linux adalah systemd(1) atau init(1).
	•	Namun, pada Cloud Shell atau lingkungan container, sistem berjalan di atas container terisolasi yang tidak menampilkan systemd.
   Oleh karena itu, bash(1) berfungsi sebagai proses induk tertinggi dalam lingkungan ini.

 2. Turunan dari bash(1):
	•	dockerd(207) → daemon utama Docker, bertugas mengatur container.
	•	logger(26) → mencatat log sistem.
	•	python(25) → menjalankan proxy editor dan script lain (Node.js di bawahnya).

 3. Turunan dari dockerd(207):
	•	containerd(231) → container runtime yang mengatur eksekusi container.
	•	Dari containerd(231) muncul beberapa proses dengan PID berbeda seperti (244), (249), (250), (252), (258), dan (262).
   Ini merupakan container yang aktif di sistem.

 4. Proses yang Berhubungan dengan Editor:
	•	Rangkaian python(25) → editor-proxy(235) → runuser(565) → sh(571) → node(608) → node(1208) → cloudcode_cli(11081)
   menunjukkan adanya proses editor berbasis cloud (kemungkinan VS Code Cloud Shell) yang berjalan di atas Node.js.

- Identifikasi Proses Induk (inid / systemd)

1. Proses induk tertinggi yang muncul : bash(1)

2. Proses yang biasanya menjadi induk di sistem Linux penuh : systemd(1) atau init(1)

3. Alasan bash(1) menjadi proses tertinggi di hasil ini :
Karena lingkungan yang digunakan adalah Cloud Shell / container-based, bukan sistem Linux penuh, sehingga systemd tidak ditampilkan. Cloud Shell hanya memunculkan shell (bash) sebagai proses pertama yang menginisialisasi semua proses lainnya.

## TUGAS

2. Diagram pohon 

  | bash─┬─ dockerd ─┬─ containerd ───6*[{containerd}] │ └─9*[{dockerd}] ├─logger ]
  ├─python─┬─editor-proxy─┬─runuser───sh───node─┬─node─┬─cloudcode_cli───6*[{cloudcode_cli}] │ │ │ │ ├─node───6*[{node}] │ │ │ │ ├─2*[node───10*[{node}]] │ │ │ │ └─12*[{node}] │ │ │ └─10*[{node}] │ │ └─4*[{editor-proxy}] │ └─sudo───tmux-agent───3*[{tmux-agent}] ├─rsyslogd───3*[{rsyslogd}] ├─sleep ├─sshd─┬─sshd───sshd───bash───bash │ └─sshd───sshd───bash───start-shell.sh───tmux └─tmux───bash───pstree

3. jelaskan hubungan antara user management dan keamanan sistem Linux.

Peran User Management dalam Keamanan

Berikut beberapa cara user management berkontribusi terhadap keamanan sistem Linux:

- Pembatasan Hak Akses (Principle of Least Privilege)
Setiap pengguna hanya diberi hak sesuai kebutuhan tugasnya.
Hanya root (superuser) yang memiliki akses penuh ke sistem.
Mencegah kesalahan atau serangan yang bisa merusak sistem secara menyeluruh.

- Isolasi Pengguna
Setiap pengguna memiliki home directory terpisah.
File dan proses antar pengguna tidak saling mengganggu.
Jika satu akun terkompromi, akun lain tetap aman.

- Kontrol Akses File (File Permissions dan Ownership)
Linux menggunakan mekanisme permission (r, w, x) untuk owner, group, dan others.
Melindungi file penting sistem dari modifikasi oleh pengguna biasa.

- Penggunaan Group
Pengguna dengan kebutuhan akses serupa dapat dikelompokkan.
Mempermudah pengelolaan hak akses tanpa harus mengatur per pengguna.

- Kebijakan Autentikasi dan Password
Sistem dapat menerapkan kebijakan kompleksitas kata sandi, batas waktu kadaluarsa, dan pembatasan login.
Mengurangi risiko akses tidak sah melalui brute force atau password lemah.

- Auditing dan Logging
Aktivitas pengguna tercatat di log seperti /var/log/auth.log.
Memudahkan pelacakan aktivitas mencurigakan dan analisis keamanan.



---

## Analisis
- Jelaskan makna hasil percobaan.  

  Manajemen User:

1. Pengelolaan user yang efektif: Hasil percobaan menunjukkan bahwa kita dapat mengelola user dengan efektif menggunakan perintah-perintah seperti useradd, passwd, dan usermod.

2. Kontrol atas akses: Kita dapat mengontrol akses user ke sistem dan file dengan menggunakan hak akses dan kepemilikan file.

2. Peningkatan keamanan sistem: Dengan mengelola user dan hak akses yang efektif, kita dapat meningkatkan keamanan sistem dan mengurangi risiko akses tidak sah.

  
  Manajemen Proses:

1. Pengelolaan proses yang efektif: Hasil percobaan menunjukkan bahwa kita dapat mengelola proses dengan efektif menggunakan perintah-perintah seperti ps, kill, bg, dan fg.

2. Kontrol atas proses: Kita dapat mengontrol proses yang sedang berjalan, seperti menghentikan atau melanjutkan proses, serta memindahkannya ke latar belakang atau depan.

3. Peningkatan efisiensi sistem: Dengan mengelola proses yang efektif, kita dapat meningkatkan efisiensi sistem dan mengurangi penggunaan sumber daya yang tidak perlu.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  

1. Fungsi Kernel: Kernel Linux berperan sebagai pengelola sumber daya sistem, termasuk proses dan user. Kernel memastikan bahwa proses berjalan dengan baik dan aman.

2. System Call: System call seperti fork(), exec(), kill(), dan wait() digunakan untuk berinteraksi dengan kernel dan mengelola proses. System call memungkinkan user space untuk meminta layanan dari kernel.

3. Arsitektur OS: Arsitektur Linux yang terdiri dari kernel space dan user space memungkinkan kernel untuk mengelola proses dan user secara efektif. Kernel memiliki kontrol penuh atas sumber daya sistem, sedangkan user space menjalankan aplikasi dan program.


- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  


Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

 - Manajemen Proses:

Linux: Menggunakan perintah seperti ps, kill, bg, fg untuk mengelola proses.
Windows: Menggunakan Task Manager atau perintah seperti tasklist, taskkill untuk mengelola proses.

- Manajemen User:

Linux: Menggunakan perintah seperti useradd, userdel, usermod untuk mengelola user.
Windows: Menggunakan Control Panel atau perintah seperti net user, net localgroup untuk mengelola user.

- Hak Akses:

Linux: Menggunakan sistem izin berbasis akses kontrol (ACL) dan permission (rwx).
Windows: Menggunakan sistem izin berbasis ACL dan atribut keamanan.

- Proses Induk:

Linux: Proses induk adalah init atau systemd.
Windows: Proses induk adalah wininit.exe atau services.exe.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

1. Manajemen proses dan manajemen pengguna merupakan dua komponen penting dalam sistem Linux yang saling berkaitan untuk menjaga keamanan, kestabilan, dan efisiensi sistem operasi.

2. Manajemen pengguna (user management) di Linux berfungsi untuk mengatur identitas, hak akses, dan izin tiap pengguna. Dengan sistem ini, administrator dapat mengontrol siapa yang dapat masuk ke sistem dan apa saja yang dapat dilakukan oleh pengguna tersebut.

3. Manajemen proses (process management) memungkinkan pengguna atau administrator untuk memantau, mengontrol, dan mengatur proses yang sedang berjalan di sistem. Hal ini penting untuk menjaga performa dan kestabilan sistem.
---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux? 
  
    Fungsi utama dari proses init (kependekan dari initialization) atau systemd dalam sistem Linux adalah sebagai sistem inisialisasi dan pengelola sistem. Mereka adalah program pertama yang dijalankan oleh kernel Linux setelah kernel dimuat, dan bertanggung jawab untuk membawa sistem ke keadaan yang dapat digunakan.

2. Apa perbedaan antara kill dan killall?

    Perbedaan utama antara perintah kill dan killall di Linux terletak pada cara mereka mengidentifikasi proses target yang akan dihentikan:

   - kill menargetkan proses berdasarkan Process ID (PID).
   - killall menargetkan proses berdasarkan nama proses (nama perintah).

3. Mengapa user root memiliki hak istimewa di sistem Linux?

    User root memiliki hak istimewa di sistem Linux karena mereka adalah Superuser atau Administrator sistem, yang secara filosofis dan teknis diperlukan untuk mengelola dan memelihara seluruh sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 

 mengalami kesulitan untuk memahami  praktkum kali ini 

- Bagaimana cara Anda mengatasinya?  

Mencoba mengulangi lagi dan lagii.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
