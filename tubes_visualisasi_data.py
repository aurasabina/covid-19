import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load data dengan handling error
try:
    data = load_data('covid.csv')  # Pastikan file 'covid.csv' ada di folder yang sama
    st.success("Data berhasil dimuat!")
    st.dataframe(data)
except FileNotFoundError:
    st.error("File 'covid.csv' tidak ditemukan.")
    st.stop()

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# 1. Visualisasi interaktif tren jumlah kasus baru harian
st.write("### Tren Jumlah Kasus Baru Harian (Interaktif)")
fig1 = px.line(
    data,
    x="Date",
    y="New Cases",
    color="Location",
    title="Tren Jumlah Kasus Baru Harian",
    labels={"Date": "Tanggal", "New Cases": "Jumlah Kasus Baru"},
)
fig1.update_layout(hovermode="x unified")
st.plotly_chart(fig1)

# 2. Visualisasi interaktif tren jumlah kematian baru harian
st.write("### Tren Jumlah Kematian Baru Harian (Interaktif)")
fig2 = px.line(
    data,
    x="Date",
    y="New Deaths",
    color="Location",
    title="Tren Jumlah Kematian Baru Harian",
    labels={"Date": "Tanggal", "New Deaths": "Jumlah Kematian Baru"},
)
fig2.update_layout(hovermode="x unified")
st.plotly_chart(fig2)

# 3. Visualisasi total kasus dan total kematian dari waktu ke waktu
st.write("### Tren Total Kasus dari Waktu ke Waktu (Interaktif)")
fig3 = px.line(
    data,
    x="Date",
    y="Total Cases",
    color="Location",
    title="Tren Total Kasus dari Waktu ke Waktu",
    labels={"Date": "Tanggal", "Total Cases": "Total Kasus"},
)
fig3.update_layout(hovermode="x unified")
st.plotly_chart(fig3)

st.write("### Tren Total Kematian dari Waktu ke Waktu (Interaktif)")
fig4 = px.line(
    data,
    x="Date",
    y="Total Deaths",
    color="Location",
    title="Tren Total Kematian dari Waktu ke Waktu",
    labels={"Date": "Tanggal", "Total Deaths": "Total Kematian"},
)
fig4.update_layout(hovermode="x unified")
st.plotly_chart(fig4)

# 4. Perbandingan kasus baru, kematian baru, dan pemulihan baru
st.write("### Perbandingan Kasus Baru, Kematian Baru, dan Pemulihan Baru (Interaktif)")
fig5 = px.line(
    data.melt(id_vars=["Date", "Location"], value_vars=["New Cases", "New Deaths", "New Recovered"]),
    x="Date",
    y="value",
    color="Location",
    line_group="variable",
    title="Perbandingan Kasus Baru, Kematian Baru, dan Pemulihan Baru",
    labels={"Date": "Tanggal", "value": "Jumlah", "variable": "Jenis Data"},
)
fig5.update_layout(hovermode="x unified")
st.plotly_chart(fig5)
