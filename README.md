````markdown
# Face and Motion Detection with Age Estimation

Proyek ini adalah aplikasi untuk mendeteksi wajah, gerakan, dan memperkirakan usia pengguna menggunakan OpenCV dan model pre-trained untuk estimasi usia.

## Fitur

- **Deteksi Wajah**: Menggunakan Haar Cascade untuk mendeteksi wajah dalam video.
- **Deteksi Gerakan**: Menggunakan background subtraction untuk mendeteksi gerakan dalam frame.
- **Estimasi Usia**: Memperkirakan usia pengguna berdasarkan wajah yang terdeteksi.

## Prerequisites

Pastikan Anda memiliki Python 3 dan paket berikut terinstal:

- OpenCV

Anda dapat menginstalnya dengan pip:

```bash
pip install opencv-python
```
````

## Struktur Folder

```
FaceAndMotionDetection/
├── main.py
├── detector/
│   ├── detector.py
│   └── __init__.py
└── utils/
    ├── utils.py
    └── __init__.py
```

## Model Usia

Unduh model yang diperlukan untuk estimasi usia:

1. **Model Arsitektur**: [deploy_age.prototxt](https://github.com/spmallick/learnopencv/blob/master/AgeGender/deploy_age.prototxt)
2. **Model Bobot**: [age_net.caffemodel](https://github.com/spmallick/learnopencv/blob/master/AgeGender/age_net.caffemodel)

Simpan kedua file ini di direktori yang sama dengan `main.py`.

## Cara Menjalankan Aplikasi

1. **Clone Repository**:

   ```bash
   git clone <repository-url>
   cd FaceAndMotionDetection
   ```

2. **Jalankan Aplikasi**:

   ```bash
   python3 main.py
   ```

3. **Menghentikan Aplikasi**:
   Tekan `q` pada keyboard untuk keluar dari aplikasi.

## Catatan

- Pastikan webcam Anda berfungsi dengan baik, karena aplikasi ini menggunakan webcam untuk menangkap video secara langsung.
- Model usia hanya berfungsi jika wajah terdeteksi dengan jelas.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu untuk mendiskusikan fitur yang ingin ditambahkan.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat [LICENSE](LICENSE) untuk detail lebih lanjut.

```

### Cara Menggunakan

1. Salin konten di atas dan simpan dalam file bernama `README.md` di direktori proyek Anda.
2. Pastikan untuk memperbarui `<repository-url>` dengan URL repositori Anda jika Anda menggunakan sistem kontrol versi seperti Git.

Ini akan memberi pengunjung informasi yang jelas tentang proyek Anda dan cara menggunakannya. Jika Anda ingin menambahkan informasi lain atau melakukan penyesuaian, silakan beri tahu!
```
