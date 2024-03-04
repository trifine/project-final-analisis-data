import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

st.title('Project Final Analisis Data all Sharing Data Set')
st.subheader('Data Sewa Sepeda')

col1, col2, col3 = st.columns(3)
    
with col1:
    total_casual = all_df['casual'].sum()
    st.metric("Total Penyewa Casual", value=total_casual)
    
with col2:
    total_registered = all_df['registered'].sum() 
    st.metric("Total Penyewa Registered", value=total_registered)
    
with col3:
    total_rents =  total_casual + total_registered
    st.metric("Total Seluruh Penyewa", value=total_rents)

st.image("https://media.istockphoto.com/id/1264197650/id/foto/tempat-parkir-sepeda-bawah-tanah-modern.jpg?s=612x612&w=is&k=20&c=7C7PLFhbNdGzT6mkrpIKF23OKCz6cp9gHz8xsqIyfYU=")

st.write("Tabel Data Set")
st.write(all_df)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.subheader('Data Sewa Sepeda Berdasarkan Musim')
season_rentals = all_df.groupby('season')[['casual', 'registered']].sum().reset_index()
season_rentals['total_rentals'] = season_rentals['casual'] + season_rentals['registered']
    
plt.figure(figsize=(10, 6))
sns.barplot(data=season_rentals, x='season', y='total_rentals', palette='viridis')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewa')
plt.title('Jumlah Penyewa Sepeda Berdasarkan Musim')
st.pyplot()


st.subheader('Data Sewa Sepeda Berdasarkan Cuaca')
weather_rentals = all_df.groupby('weather_cond')[['casual', 'registered']].sum().reset_index()
weather_rentals['total_rentals'] = weather_rentals['casual'] + weather_rentals['registered']

plt.figure(figsize=(10, 6))
sns.barplot(data=weather_rentals, x='weather_cond', y='total_rentals', palette='viridis')
plt.xlabel('Jenis Cuaca')
plt.ylabel('Jumlah Penyewa')
plt.title('Jumlah Penyewa Sepeda Berdasarkan Jenis Cuaca')
st.pyplot()

st.caption("© 2024 Trifine Laurensi Br Ginting")
