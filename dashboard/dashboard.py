import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.title('Dashboard Analisis Data Penyewaan Sepeda')
st.subheader('Menganalisis Pengaruh Suhu dan Hari Libur terhadap Penyewaan Sepeda')

# Mengambil dataset dari folder 'data'
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

st.write("Beberapa baris pertama dari dataset 'day.csv':")
st.write(day_df.head())

st.write("Beberapa baris pertama dari dataset 'hour.csv':")
st.write(hour_df.head())

# Pembersihan dataset
day_df_cleaned = day_df.drop(columns=['instant'])
hour_df_cleaned = hour_df.drop(columns=['instant'])

# Distribusi jumlah penyewa sepeda harian
st.subheader('Distribusi Jumlah Penyewa Sepeda Harian')
plt.figure(figsize=(10,6))
counts, bins, patches = plt.hist(day_df_cleaned['cnt'], bins=30, color="lightblue", edgecolor="black")
max_patch = np.argmax(counts)
patches[max_patch].set_facecolor("darkblue")
plt.title('Distribusi Jumlah Penyewa Sepeda Harian (Highlight Balok Tertinggi)')
plt.xlabel('Jumlah Penyewa (cnt)')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Distribusi jumlah penyewa sepeda per jam
st.subheader('Distribusi Jumlah Penyewa Sepeda Per Jam')
plt.figure(figsize=(10,6))
counts, bins, patches = plt.hist(hour_df_cleaned['cnt'], bins=30, color="lightgreen", edgecolor="black")
max_patch = np.argmax(counts)
patches[max_patch].set_facecolor("darkgreen")
plt.title('Distribusi Jumlah Penyewa Sepeda Per Jam (Highlight Balok Tertinggi)')
plt.xlabel('Jumlah Penyewa (cnt)')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Heatmap korelasi untuk dataset harian
st.subheader('Heatmap Korelasi Dataset day.csv')
day_numeric = day_df_cleaned.select_dtypes(include=[np.number])
plt.figure(figsize=(10,8))
sns.heatmap(day_numeric.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi Dataset day.csv')
st.pyplot(plt)

# Heatmap korelasi untuk dataset per jam
st.subheader('Heatmap Korelasi Dataset hour.csv')
hour_numeric = hour_df_cleaned.select_dtypes(include=[np.number])
plt.figure(figsize=(10,8))
sns.heatmap(hour_numeric.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Korelasi Dataset hour.csv')
st.pyplot(plt)

# Model regresi linear
st.subheader('Regresi Linear: Pengaruh Suhu terhadap Jumlah Penyewa')
X = day_df_cleaned[['temp']]
y = day_df_cleaned['cnt']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
correlation = day_df_cleaned['temp'].corr(day_df_cleaned['cnt'])

plt.figure(figsize=(10,6))
plt.scatter(day_df_cleaned['temp'], day_df_cleaned['cnt'], alpha=0.5, color='blue', label="Data Penyewaan")
plt.plot(day_df_cleaned['temp'], y_pred, color='red', linewidth=2, label=f"Garis Regresi (korelasi = {correlation:.2f})")
plt.title('Pengaruh Suhu terhadap Jumlah Penyewa Sepeda Harian')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewa Sepeda Harian (cnt)')
plt.legend()
st.pyplot(plt)

# Binning suhu menjadi kelompok rendah, sedang, tinggi
st.subheader('Binning Suhu menjadi Kelompok Rendah, Sedang, dan Tinggi')
bins_temp = [0, 0.3, 0.6, 1]
labels_temp = ['Rendah', 'Sedang', 'Tinggi']
day_df_cleaned['temp_group'] = pd.cut(day_df_cleaned['temp'], bins=bins_temp, labels=labels_temp)

temp_rendah = day_df_cleaned[day_df_cleaned['temp_group'] == 'Rendah']['cnt'].mean()
temp_sedang = day_df_cleaned[day_df_cleaned['temp_group'] == 'Sedang']['cnt'].mean()
temp_tinggi = day_df_cleaned[day_df_cleaned['temp_group'] == 'Tinggi']['cnt'].mean()

categories = ['Rendah', 'Sedang', 'Tinggi']
values = [temp_rendah, temp_sedang, temp_tinggi]

colors = ['lightblue', 'lightblue', 'lightblue']
max_index = np.argmax(values)
colors[max_index] = 'blue'

plt.figure(figsize=(8,6))
plt.bar(categories, values, color=colors, edgecolor='black')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kelompok Suhu')
plt.xlabel('Kelompok Suhu (Temp)')
plt.ylabel('Rata-rata Jumlah Penyewaan (Cnt)')
st.pyplot(plt)

# Manual grouping jam
st.subheader('Manual Grouping Waktu (Jam)')
def manual_grouping_time(hr):
    if hr < 6:
        return 'Malam'
    elif hr < 12:
        return 'Pagi'
    elif hr < 18:
        return 'Siang'
    else:
        return 'Sore'

hour_df_cleaned['manual_time_group'] = hour_df_cleaned['hr'].apply(manual_grouping_time)

time_malam_manual = hour_df_cleaned[hour_df_cleaned['manual_time_group'] == 'Malam']['cnt'].mean()
time_pagi_manual = hour_df_cleaned[hour_df_cleaned['manual_time_group'] == 'Pagi']['cnt'].mean()
time_siang_manual = hour_df_cleaned[hour_df_cleaned['manual_time_group'] == 'Siang']['cnt'].mean()
time_sore_manual = hour_df_cleaned[hour_df_cleaned['manual_time_group'] == 'Sore']['cnt'].mean()

categories_manual_time = ['Malam', 'Pagi', 'Siang', 'Sore']
values_manual_time = [time_malam_manual, time_pagi_manual, time_siang_manual, time_sore_manual]

time_colors_manual = ['lightgreen'] * 4
max_time_index = np.argmax(values_manual_time)
time_colors_manual[max_time_index] = 'green'

plt.figure(figsize=(8,6))
plt.bar(categories_manual_time, values_manual_time, color=time_colors_manual, edgecolor='black')
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Manual Grouping Waktu (Jam)')
plt.xlabel('Kelompok Waktu (Jam)')
plt.ylabel('Rata-rata Penyewaan Sepeda (Cnt)')
st.pyplot(plt)
