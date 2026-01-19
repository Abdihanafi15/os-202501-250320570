
# Laporan Praktikum Minggu [10]
Topik: [Manajemen Memori – Page Replacement (FIFO & LRU)]

---

## Identitas
- **Nama**  : [Abdi Hnafi Alghifari]  
- **NIM**   : [250320570]  
- **Kelas** : [1DSRA]

---

## Tujuan
1. Mengetahui dan menjelaskan cara kerja algoritma Page Replacement.
2. Menganalisis prinsip dan langkah kerja algoritma FIFO (First In First Out).
3. Menganalisis prinsip dan langkah kerja algoritma LRU (Least Recently Used).
4. Menghitung dan membandingkan jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU.
5. Membandingkan kinerja dan efisiensi FIFO dan LRU dalam penggunaan memori.

---

## Dasar Teori
1. FIFO (First In First Out)
FIFO mengganti page yang paling awal masuk ke memori tanpa mempertimbangkan frekuensi atau waktu terakhir penggunaan page tersebut.
2. LRU (Least Recently Used)
LRU mengganti page yang paling lama tidak digunakan berdasarkan waktu akses terakhir.
3. Page Replacement
Page replacement adalah proses mengganti page yang berada di memori dengan page baru ketika memori penuh dan terjadi page fault.
4. Algoritma Page Replacement
Algoritma page replacement menentukan page mana yang akan dikeluarkan dari memori untuk meminimalkan jumlah page fault.
5. Manajemen Memori
Manajemen memori adalah mekanisme pengaturan penggunaan memori sehingga beberapa proses dapat berjalan bersamaan tanpa konflik dan dengan pemanfaatan memori yang optimal.

---

## Langkah Praktikum
1. Menyiapkan Dataset

    Gunakan reference string berikut sebagai contoh:

         7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

    Jumlah frame memori: 3 frame.

2. Implementasi FIFO
- Simulasikan penggantian halaman menggunakan algoritma FIFO.
- Catat setiap page hit dan page fault.
- Hitung total page fault.

3. Implementasi LRU
- Simulasikan penggantian halaman menggunakan algoritma LRU.
- Catat setiap page hit dan page fault.
- Hitung total page fault.

4. Eksekusi & Validasi
- Jalankan program untuk FIFO dan LRU.
- Pastikan hasil simulasi logis dan konsisten.
- Simpan screenshot hasil eksekusi.

5. Analisis Perbandingan
- Buat tabel perbandingan seperti berikut:

| Algoritma	| Jumlah Page Fault | Keterangan |
|-----------|--------------------|------------|
| FIFO |	... |	... |
| LRU	| ... |	... |

- Jelaskan mengapa jumlah page fault bisa berbeda.
- Analisis algoritma mana yang lebih efisien dan alasannya.

6. Commit & Push

        git add .
        git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
        git push origin main


---

## Kode / Perintah
```bash
def fifo(reference_string, frame_size):
    frames = []
    page_faults = 0
    index = 0

    print("=== Simulasi FIFO ===")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % frame_size
        print(f"Page {page} -> Frame {frames}")

    return page_faults


def lru(reference_string, frame_size):
    frames = []
    page_faults = 0

    print("\n=== Simulasi LRU ===")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)

        print(f"Page {page} -> Frame {frames}")

    return page_faults


# Data Praktikum
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

# Eksekusi
fifo_faults = fifo(reference_string, frame_size)
lru_faults = lru(reference_string, frame_size)

print("\n=== Hasil Akhir ===")
print("Total Page Fault FIFO:", fifo_faults)
print("Total Page Fault LRU :", lru_faults)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_simulasi.png)

---

## Analisis
- Analisis perbandingan 

  | Algoritma	| Jumlah Page Fault | Keterangan |
  |-----------|--------------------|------------|
  | FIFO |	10 | FIFO kurang efisien karena tidak mempertimbangkan pola akses |
  | LRU	| 9 |	Lebih sedikit page fault dibanding FIFO, Page yang sering diakses dipertahankan lebih lama |

- Jelaskan mengapa jumlah page fault bisa berbeda?
1. FIFO (First In First Out)
   - Mengganti page yang paling lama masuk ke memori
   - Tidak memperhatikan apakah page tersebut masih sering digunakan
   - Akibatnya, page yang masih dibutuhkan bisa terhapus

 Hal ini menyebabkan page fault tambahan ketika page tersebut diakses kembali.

2. Mengganti page yang paling lama tidak digunakan
   - Mempertimbangkan riwayat akses
   - Page yang sering diakses akan dipertahankan

Kemungkinan page yang dibutuhkan masih ada di memori lebih besar, sehingga page fault lebih sedikit.

- Analisis algoritma mana yang lebih efisien dan alasannya.

Algoritma yang lebih efisien adalah LRU.  
     Alasannya:
- LRU menyimpan page yang sering digunakan dan hanya mengganti page yang sudah lama tidak dipakai.
- Hal ini membuat jumlah page fault lebih sedikit.
- FIFO hanya melihat urutan masuk page, sehingga bisa menghapus page yang masih dibutuhkan.



---

## Kesimpulan
1. Page replacement diperlukan saat memori penuh dan terjadi page fault.
2. FIFO mengganti page berdasarkan urutan masuk, sedangkan LRU berdasarkan pemakaian terakhir.
3. Dari hasil simulasi, LRU menghasilkan page fault lebih sedikit dibanding FIFO.
4. LRU lebih efisien karena mempertahankan page yang sering digunakan.
5. FIFO lebih sederhana, tetapi kinerjanya kurang optimal dibanding LRU.

---

## Quiz
1. [Apa perbedaan utama FIFO dan LRU?]  
   **Jawaban:**  

 - FIFO (First In First Out)
 FIFO mengganti page yang paling awal masuk ke memori tanpa mempertimbangkan frekuensi atau waktu terakhir penggunaan page tersebut.
 - LRU (Least Recently Used)
 LRU mengganti page yang paling lama tidak digunakan berdasarkan waktu akses terakhir.

2. [Mengapa FIFO dapat menghasilkan Belady’s Anomaly?]  
   **Jawaban:**  
  Belady’s Anomaly terjadi karena FIFO tidak mempertimbangkan frekuensi atau pola akses page, hanya urutan masuknya saja.

3. [Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?]  
   **Jawaban:**  
  Karena program biasanya mengakses data yang sama secara berulang (locality of reference).
  LRU mampu menjaga page yang sering dipakai tetap di memori, sehingga page fault lebih sedikit dibanding FIFO.
  
  jadi, LRU lebih efisien karena lebih pintar dalam menebak page mana yang akan dibutuhkan kembali.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
