# Deteksi Objek menggunakan OpenCV

Repository GitHub ini berisi kompilasi jawaban URO Tugas 02 Computer Vision dalam rangkaian acara seleksi Calon Kru 17 Unit Robotika ITB Divisi Programming.

Dalam proyek ini, saya menciptakan sistem deteksi objek sederhana yang mengidentifikasi dan melacak objek berwarna merah dalam video menggunakan OpenCV. Saya mendemonstrasikan konsep pemrosesan video, penyembunyian warna, deteksi kontur, dan penyimpanan video keluaran dalam Python.

## Ringkasan Program

Anda bisa melihat video dokumentasi demo dan penjelasan program [di sini.](https://itbdsti-my.sharepoint.com/:v:/g/personal/19624235_mahasiswa_itb_ac_id/ERwUq65VKBBDlSEyTHVFDXwBevOD0ddM7B47WKpDeHCwEw?e=3uTnCj) Penjelasan program kurang lebih sebagai berikut:
- **Pengambilan dan Pemrosesan Video**: Program mengambil bingkai dari video input dan memprosesnya menggunakan ruang warna HSV untuk mendeteksi lingkaran merah.
- **Pembuatan *Mask* HSV**: Masker HSV digunakan untuk mengisolasi wilayah merah dari lingkaran.
- **Deteksi Kontur**: Kontur dideteksi, difilter, dan kotak pembatas objek digambar pada setiap frame.
- **Visualisasi Informatif**: Program mengkustomisasi nama jendela, ukurannya, dan indikator kemajuan untuk membuat visualisasi lebih informatif.

## Instalasi

Pastikan Anda menginstal dependensi berikut sebelum menjalankan skrip:
- Python 3
- OpenCV (`cv2`)
- NumPy (`numpy`)

Langkah-langkah untuk instalasi program:
1. Klon repositori ini:
```bash
git clone https://github.com/m-akma1/URO-Tugas-02-Computer-Vision
```
2. Instal dependensi:
```bash
pip install opencv-python numpy
```
3. Jalankan skrip di direktori program:
```bash
python project.py
```
3. Tekan `q` untuk keluar dari tampilan video setelah selesai.

Video keluaran (`output_frame.avi` dan `output_mask.avi`) akan disimpan di direktori di mana program dijalankan.

## Penulis

Nama  : Muhammad Akmal  
NIM   : 19624235  
Email : muhammad.akmal.3806@gmail.com  
Sekolah Teknik Elektro dan Informatika - Komputasi
