
# Laporan Praktikum Minggu 1
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Abdi hanafi Alghifari 
- **NIM**   : 250320570 
- **Kelas** : 1DSRA

---

## Tujuan
Dapat mengidentifikasikan komponen utama OS (kernel, system call, device driver, file system) dan juga bisa menggambarkan diagram sederhana arsitektur OS


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. perbedaan antara monolithic kernel, microkernel, dan layered architecture.
2. mempelajari hubungan antara user-system call-kernel-hardware
3. perbedaan antara linux dan windows 
4. komponen arsitektur operasi system 
5. peran operasi siste dalam arsitektur komputer 
---

## Langkah Praktikum
- membuat akun githhub.
- mencari repositori akun orang lain yang ingin di fork.
- fork repositori sampai muncul diakun github kita sendiri.
- copy fork repositori ke dalam folder dengan code "git clone" dan hubungkan ke dalam github.
- git config user.name dan user.email untuk memastikan akun kita terdaftar 
- edit repositori di dalam vs code
- setelah edit  sudah selesei  upload repositori yang sudah diedit dengan code git commit add 
- cek repositori di github untuk memastikan sudah ada perubahan didalam repositori yg sudah di fork 
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
![Screenshot hasil](./screenshots/screenshoot%20hasil%20percobaan.jpeg

---

## Analisis
 makna hasil percobaan  
1. uname -a : 
- menampilkan informasi sistem operasi kernel yang sedang dijlankan yaitu kernel linux versi 6.6.10s+. 
- Arsitektur prosesor : x86_64(64-bit)
- menggunakan fitur SMP (Symmetric Multi Processing) dan PREEMPT_DYNAMIC (mendukung premmption dinamis, artinya kernel bisa beralih konteks cepat untuk performa interaktif)

2. lsmod | head :
Menampilkan modul kernel yang sedang dimuat, seperti:
	•	iptable_nat, xt_nat, xt_mark → modul terkait jaringan dan NAT (Network Address Translation)
	•	veth → modul virtual ethernet, menandakan sistem berjalan dalam lingkungan virtual (container / VM)

3. dmesg | head : 
Menandakan  tidak memiliki izin root, jadi akses langsung ke kernel buffer ditolak. Ini umum di Cloud Shell untuk alasan keamanan.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 

1. Kernel : 
Kernel adalah inti dari sistem operasi yang mengatur:
	•	Manajemen perangkat keras
	•	Manajemen proses
	•	Manajemen memori
	•	Manajemen sistem file
 terlihat kernel Linux 6.6.10, yang bekerja mengatur semua operasi sistem Cloud Shell.
Kernel ini juga memuat modul (hasil lsmod) agar dapat menangani fungsi tambahan seperti jaringan virtual.
2. system call 
system call adalah antarmuka antara program dan kernel.
Contohnya: ketika mengetik perintah uname, shell memanggil system call uname() untuk meminta info kernel.
Begitu juga lsmod dan dmesg menggunakan system call untuk:
	•	Mengakses daftar modul kernel
	•	Membaca buffer pesan kernel
Namun, karena bukan user root, system call untuk dmesg ditolak dengan pesan “Operation not permitted” — ini menunjukkan mekanisme proteksi kernel terhadap akses pengguna biasa.
3. arsitektur OS :
Linux menggunakan arsitektur monolithic kernel, artinya:
	•	Semua layanan inti OS (file system, device driver, jaringan, dll.) berjalan di mode kernel (ring 0).
	•	Namun modul seperti iptable_nat atau veth bisa dimuat atau dilepas secara dinamis, membuatnya lebih fleksibel.

Dalam hasil ini, daftar modul di lsmod menunjukkan fleksibilitas ini — bagian dari desain modular monolithic kernel.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
1. Linux 
- kernel : mengggunakan monolithic kernel 
- shell/command line : menggunakan Bash,zsh, atau sh. perintah lsmoed,uname, dmesg digunakan untuk interaksi langsung dengan kernel 
- perintah uname : menampilkan detail kernel Linux (versi arsitektur, tanggal buld)
- perintah lsmod : menampilkanm modul kernel yang dimuat (driver, jaringan, dll)
- perintah dmesg : menampilkan log pesan kernel (boot, device, error)
- akses ke kernel bisa langsung lewat system call 
- hak akses pengguna : dibedakan jelas root vs user  biasa 
2. Windows 
- menggunakan hybrid  kernel (gabungan monolithic+microkernel)
- menggunakan Command Prompt (CMD) atau PowerShell
- uname tidak tersedia. sebagai gantinya
di PoweShell : systeminfo 
-  lsmod tidak ada di Windows, driver bisa dilihat di Device Manager  
- tidak ada dmesg. Windows menggunakan Event viewer   
- Akses kernel lebih dibatasi interaksi dilakukan melalui API windows 
- hak akses pengguna : ada kensep administrator 
---

## Kesimpulan
1.  kernel berperan sebagai inti sistem operasi yang mengatur seluruh sumber daya perangkat keras dan perangkat lunak.
2. System call menjadi perantara antara pengguna (user space) dengan kernel (kernel space). Perintah seperti uname, lsmod, dan dmesg menggunakan system call untuk meminta informasi dari kernel. Namun, akses ke beberapa fungsi kernel dibatasi bagi pengguna non-root,
3. Arsitektur OS memengaruhi cara sistem beroperasi. Linux dengan arsitektur monolithic memberikan fleksibilitas dan keterbukaan akses, sementara Windows dengan hybrid kernel lebih membatasi akses langsung ke kernel demi stabilitas dan keamanan sistem.
---

## Quiz
1. 3 fungsi system kernel 
- Manajemen sumber daya (Resource Management)
- Manajemen file dan sisem  I/O
- Manajemen proses dan keamanan sistem 

2. - USER MODE  
adalah mode tempat semua program aplikasi berjalan — seperti Microsoft Word, browser, atau pemutar musik.
   Ciri-cirinya:
	•	Akses ke perangkat keras (CPU, memori, disk, dll.) terbatas.
	•	Jika aplikasi error atau crash, tidak akan memengaruhi sistem operasi.
	•	Tidak boleh menjalankan instruksi khusus CPU (privileged instructions).
	•	Untuk melakukan tugas penting (misalnya membaca file atau mencetak dokumen), aplikasi harus meminta bantuan kernel melalui system call.
- KERNEL MODE 
Kernel Mode adalah mode di mana kernel (inti sistem operasi) berjalan.
Di sini sistem punya hak penuh terhadap perangkat keras dan seluruh memori komputer.
   Ciri-cirinya:
	•	Bisa menjalankan semua instruksi CPU, termasuk privileged instructions.
	•	Digunakan untuk mengelola proses, memori, file system, dan perangkat keras.
	•	Jika terjadi kesalahan di mode ini, bisa menyebabkan crash seluruh sistem (kernel panic).
- PERBEDAAN 
 USER MODE 
- Tingkat akses : akses terbatas, tidak bisa langsung akses hardware 
- fungsi utama : mejalankan aplikasi pengguna seperti browser,word,dsb
- keamanan : lebih aman, error aplikasi tidak memengaruhi sistem 
- lokaksi kerja  : berjalan di user space 
- Intruksi CPU : tidak bisa menjalankan intruksi istimewa 
-contoh aktivitas : menjalankan program aplikasi biasa

 KERNEL MODE 
- Tingkat akses : akses penuh ke seluruh sumber daya sistem 
- fungsi utama : menjalankan fungsi inti sistem operasi  
- keamanan : risiko tinggi jika error karena bisa merusak sistem 
- lokasi kekrja : Berjalan di kernel space 
- intruksi CPU : bisa menjalankan intruksi istemewa (privilage intruction)
- contoh aktivitas : system call, manajemen memory, driver perangkat 
3. contoh OS arsitektur monolithic :   
- LINUX,(UBUNTU,Fedora, Debian, Android)
- MS-DOS 
- Unix(versi lama sperti system v)
  contoh OS arsitektur Microkernel: 
- Minix
- QNX
- Mach(digunakan di MacOS dan IOS)
- Integrity OS
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Cara memahami sistem operasi dan mengoperasikannya, langkah langkah untuk men fork di github dan edit repo kemudian cara upload supaya tersimpan di githhub.karena baru pertama kali terjun ke dunia ini jadi mungkin lebih asing,  tapi bagian yg paling penting adalah ketika kesusahan itu bisa diseleisaikan walaupun harus berkali kali mengulang. 
- Bagaimana cara Anda mengatasinya?  
Pastinya sabar dan juga kerja keras, salah satunya yaitu berdiskusi dengan teman, dengan sperti ini memudahkan untuk mencari solusi dan juga ilmu baru yang belum diketahui seblumnya.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
