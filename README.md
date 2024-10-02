# Proyek Analisis Data: Tren Penyewaan Sepeda: Mengkaji Pengaruh Suhu dan Hari Libur pada Pengguna Kasual 🚴‍♂️

Proyek ini bertujuan untuk mengkaji pengaruh suhu dan hari libur terhadap tren penyewaan sepeda oleh pengguna kasual. Proyek ini menggunakan dataset harian dan per jam, serta melakukan analisis menyeluruh terhadap variabel-variabel yang mempengaruhi jumlah penyewa sepeda, seperti suhu dan status hari libur.

## Fitur Utama 🚀

- **Pertanyaan Bisnis**: Proyek ini fokus pada dua pertanyaan utama:
  1. Bagaimana pengaruh suhu (temp) terhadap jumlah total penyewa sepeda harian (cnt)?
  2. Bagaimana tren penggunaan sepeda oleh pengguna kasual (casual) pada hari libur (holiday) dibandingkan dengan hari biasa (non-holiday)?
- **Import Data & Wrangling**: Proses memuat, menilai, dan membersihkan data dilakukan secara bertahap, termasuk penghapusan kolom yang tidak diperlukan seperti `instant`.
- **Exploratory Data Analysis (EDA)**: Melakukan eksplorasi data menggunakan visualisasi distribusi jumlah penyewa sepeda per hari dan per jam, serta heatmap untuk melihat korelasi antar variabel.

- **Regresi Linear**: Proyek ini melakukan analisis regresi linear untuk memodelkan hubungan antara suhu dan jumlah penyewa sepeda harian.

- **Visualisasi Interaktif**: Menggunakan **Streamlit** untuk menghasilkan visualisasi dan analisis interaktif.

- **Analisis Lanjutan**: Mengelompokkan suhu menjadi kategori rendah, sedang, dan tinggi, serta melakukan manual grouping jam menjadi pagi, siang, sore, dan malam.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:

- `notebook.ipynb`: Jupyter Notebook yang berisi analisis mendalam terkait tren penyewaan sepeda.
- `data/`: Direktori yang berisi dataset penyewaan sepeda.
  - `day.csv`: Dataset penyewaan sepeda harian.
  - `hour.csv`: Dataset penyewaan sepeda per jam.
- `dashboard.py`: Script Python untuk menjalankan dashboard interaktif menggunakan **Streamlit**.
- `README.md`: Dokumentasi proyek ini.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek ini.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook

Untuk menjalankan analisis di **Jupyter Notebook**:

1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit

Proyek ini juga menyediakan dashboard interaktif menggunakan **Streamlit**. Ikuti langkah berikut untuk menjalankannya:

1. Instal semua dependensi menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi **Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

## Insight Utama 📊

1. **Pengaruh Suhu terhadap Penyewaan Sepeda**:

   - Terdapat korelasi positif antara suhu dan jumlah penyewa sepeda. Semakin tinggi suhu, semakin tinggi pula jumlah penyewaan sepeda.

2. **Penggunaan Sepeda pada Hari Libur dan Hari Biasa**:

   - Pengguna kasual lebih banyak menggunakan sepeda pada hari libur dibandingkan hari biasa, namun perbedaan ini tidak terlalu signifikan.

3. **Distribusi Penggunaan Berdasarkan Waktu**:
   - Puncak penggunaan sepeda terjadi pada pagi hari (sekitar jam 8) dan sore hari (sekitar jam 5), yang bertepatan dengan jam sibuk.

## Dataset

Dataset yang digunakan dalam proyek ini adalah:

- **day.csv**: Dataset harian yang mencatat data penyewaan sepeda termasuk informasi tentang suhu, kondisi cuaca, dan status hari libur.
- **hour.csv**: Dataset per jam yang mencatat data penyewaan sepeda per jam, memberikan detail yang lebih spesifik terkait waktu.

## Library yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk analisis dan visualisasi data.
- **Streamlit**: Library Python untuk membuat aplikasi web interaktif.
- **Matplotlib & Seaborn**: Digunakan untuk visualisasi data.
- **Scikit-learn**: Digunakan untuk analisis regresi linear dan pemodelan.
