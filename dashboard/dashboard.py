import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import ampy

# Set judul untuk dashboard
st.title("Dashboard Layanan Penyewaan Sepeda")

# Memuat dataset
day_df = pd.read_csv('dashboard/cleaned_days_df.csv')
hour_df = pd.read_csv('dashboard/cleaned_hours_df.csv')

# Mengonversi kolom 'date' menjadi format datetime
day_df['date'] = pd.to_datetime(day_df['date'])
hour_df['date'] = pd.to_datetime(hour_df['date'])

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih halaman:", ("Analisis Tren", "Faktor yang Mempengaruhi Penggunaan Layanan"))

if page == "Analisis Tren":
    st.header("Analisis Tren Layanan Penyewaan Sepeda")

    # Tren Penggunaan Bulanan
    monthly_usage = day_df.groupby(['year', 'month'])['count'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=monthly_usage, x='month', y='count', hue='year', palette='pastel')
    plt.title('Tren Penggunaan Bulanan')
    plt.xlabel('Bulan')
    plt.ylabel('Total Penggunaan')
    plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agt', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(plt)

    # Penggunaan Berdasarkan Hari dalam Seminggu
    day_df['weekday'] = day_df['date'].dt.dayofweek
    weekday_usage = day_df.groupby('weekday')['count'].mean().reset_index()
    weekday_usage['weekday'] = weekday_usage['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})

    plt.figure(figsize=(10, 5))
    sns.barplot(x='weekday', y='count', data=weekday_usage, palette='coolwarm')
    plt.title('Rata-rata Penggunaan berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Penggunaan')
    st.pyplot(plt)

elif page == "Faktor yang Mempengaruhi Penggunaan Layanan":
    st.header("Faktor yang Mempengaruhi Penggunaan Layanan Penyewaan Sepeda")

    # Pengaruh Cuaca
    weather_usage = day_df.groupby('weather')['count'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x='weather', y='count', data=weather_usage, palette='viridis')
    plt.title('Rata-rata Penggunaan berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Penggunaan')
    st.pyplot(plt)

    # Heatmap Korelasi
    correlation = day_df[['temp', 'humidity', 'windspeed', 'count']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Korelasi antara Suhu, Kelembaban, Kecepatan Angin, dan Penggunaan')
    st.pyplot(plt)

    # Penggunaan Berdasarkan Hari Kerja dan Hari Libur
    workingday_usage = day_df.groupby('workingday')['count'].agg(['mean', 'sum', 'max', 'min']).reset_index()
    workingday_usage.columns = ['Hari Kerja', 'Rata-rata Penggunaan', 'Total Penggunaan', 'Penggunaan Maksimum', 'Penggunaan Minimum']
    
    st.subheader("Penggunaan pada Hari Kerja vs Hari Libur")
    st.write(workingday_usage)

    holiday_usage = day_df.groupby('holiday')['count'].agg(['mean', 'sum', 'max', 'min']).reset_index()
    holiday_usage.columns = ['Hari Libur', 'Rata-rata Penggunaan', 'Total Penggunaan', 'Penggunaan Maksimum', 'Penggunaan Minimum']
    
    st.write(holiday_usage)

# Footer
st.sidebar.write("Dashboard dibuat oleh Muhammad Arsayuan Wijaya")
