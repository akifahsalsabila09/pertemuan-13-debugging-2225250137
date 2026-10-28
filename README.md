
# Pertemuan 13 - Debugging dan Testing

Nama: AKIFAH SALSABILA
NIM: 2225250137
Kelas: 3F

## Kasus

Program yang diuji adalah program pengolahan nilai mahasiswa. Program memiliki tiga fungsi, yaitu menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi. Pengujian dilakukan untuk menemukan bug, mengetahui akar penyebabnya, memperbaiki kode, dan memastikan hasilnya sesuai harapan.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | PASS setelah perbaikan |
| T2 | [100, 80] | 90.0 | 36.0 | PASS setelah perbaikan |
| T3 | 60 | Lulus | Tidak lulus | PASS setelah perbaikan |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | PASS setelah perbaikan |

## Bug Report

### B01 - Kesalahan Perhitungan Rata-rata
- Gejala: Hasil rata-rata tidak sesuai dengan jumlah data.
- Test case: T1 dan T2.
- Lokasi: Fungsi hitung_rata_rata().
- Akar penyebab: Program selalu membagi total nilai dengan 5, meskipun jumlah datanya berbeda.
- Perbaikan: Menggunakan len(nilai) sebagai pembagi dan menangani daftar kosong.
- Retest: PASS setelah hasil pengujian sesuai expected.

### B02 - Kesalahan Batas Kelulusan
- Gejala: Nilai 60 dinyatakan tidak lulus.
- Test case: T3.
- Lokasi: Fungsi status().
- Akar penyebab: Operator > tidak memasukkan nilai yang sama dengan 60 sebagai nilai lulus.
- Perbaikan: Mengganti operator > menjadi >=.
- Retest: PASS setelah hasil pengujian sesuai expected.

### B03 - Kesalahan Menentukan Nilai Tertinggi
- Gejala: Program menghasilkan nilai tertinggi 0.
- Test case: T5.
- Lokasi: Fungsi nilai_tertinggi().
- Akar penyebab: Nilai awal ditetapkan 0 dan kondisi perbandingan menggunakan operator <, sehingga nilai terbesar tidak tersimpan.
- Perbaikan: Menggunakan elemen pertama sebagai nilai awal dan operator > untuk membandingkan nilai berikutnya.
- Retest: PASS setelah hasil pengujian sesuai expected.

## Retest

Hasil yang diharapkan setelah perbaikan:
- T1: 75.0
- T2: 90.0
- T3: Lulus
- T4: Tidak lulus
- T5: 90

Seluruh test case harus dijalankan kembali setelah perbaikan untuk memastikan tidak ada bug yang tersisa atau regresi.

## Cara Menjalankan

Jalankan perintah berikut dari folder utama proyek:

python3 praktik/praktik_4_debugging.py

## Refleksi

Teknik debugging yang paling membantu adalah pengujian menggunakan test case karena hasil aktual dapat dibandingkan dengan hasil yang diharapkan. Dari pengujian tersebut, kesalahan logika dapat diketahui dan diperbaiki berdasarkan bukti. Setelah perbaikan, seluruh test case perlu dijalankan kembali untuk memastikan program bekerja sesuai harapan.
