import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go

st.title("Analysis Data Angka Pendidikan Indonesia Tahun 2017 ")
st.markdown("Data Angka Partisipasi Sekolah 2017 di Indonesia")

st.sidebar.title("Analysis Data")
st.sidebar.markdown("Aplikasi adalah aplikasi untuk menvisualisasi dalam menganalisis Angka Pendidikan Indonesia Tahun 2017")

DATA_URL = ("Angka Partisipasi Sekolah 2017.csv")

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()
st.dataframe(data) 
st.info(data) 

# ---- SIDEBAR ----
st.sidebar.subheader("Select item data disini :")

# ---- BAR CHART DAN PIE CHART ----
st.sidebar.markdown("BAR CHART DAN PIE CHART")
choice = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '0')

if len(choice) >0:
    choice_data = data[data.Provinsi.isin(choice)]
    fig_histogram1 = px.histogram(choice_data, x='Provinsi', y='SD', histfunc='sum', color='Provinsi', labels={'Provinsi':'Provinsi'},  title="<b>Pendidikan SD di Indonesia 2017</b>", height=600, width=800)
    st.plotly_chart(fig_histogram1)

    fig_pie1 = px.pie(choice_data, values='SD', names='Provinsi', title="<b>Pendidikan SD di Indonesia 2017</b>")
    st.plotly_chart(fig_pie1)

    fig_histogram2 = px.histogram(choice_data, x='Provinsi', y='SMP', histfunc='sum', color='Provinsi', labels={'Provinsi':'Provinsi'},  title="<b>Pendidikan SMP di Indonesia 2017</b>", height=600, width=800)
    st.plotly_chart(fig_histogram2)

    fig_pie2 = px.pie(choice_data, values='SMP', names='Provinsi', title="<b>Pendidikan SMP di Indonesia 2017</b>")
    st.plotly_chart(fig_pie2)

    fig_histogram3 = px.histogram(choice_data, x='Provinsi', y='SMA', histfunc='sum', color='Provinsi', labels={'Provinsi':'Provinsi'},  title="<b>Pendidikan SMA di Indonesia 2017</b>", height=600, width=800)
    st.plotly_chart(fig_histogram3)

    fig_pie3 = px.pie(choice_data, values='SMA', names='Provinsi', title="<b>Pendidikan SMA di Indonesia 2017</b>")
    st.plotly_chart(fig_pie3)

    fig_histogram4= px.histogram(choice_data, x='Provinsi', y='PT', histfunc='sum', color='Provinsi', labels={'Provinsi':'Provinsi'},  title="<b>Pendidikan PT di Indonesia 2017</b>", height=600, width=800)
    st.plotly_chart(fig_histogram4)
    
    fig_pie4 = px.pie(choice_data, values='PT', names='Provinsi', title="<b>Pendidikan PT di Indonesia 2017</b>")
    st.plotly_chart(fig_pie4)

# ---- LINE CHART ----
st.sidebar.markdown("LINE CHART")
choice1 = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '1')

if len(choice1) >0:
    choice_data1 = data[data.Provinsi.isin(choice1)]
    fig_line1 = px.line(choice_data1, x ='Provinsi', y ='SD', title='Pendidikan SD di Indonesia 2017')
    st.plotly_chart(fig_line1)

    fig_line2 = px.line(choice_data1, x ='Provinsi', y ='SMP', title='Pendidikan SMP di Indonesia 2017')
    st.plotly_chart(fig_line2)

    fig_line3 = px.line(choice_data1, x ='Provinsi', y ='SMA', title='Pendidikan SMA di Indonesia 2017')
    st.plotly_chart(fig_line3)

    fig_line4 = px.line(choice_data1, x ='Provinsi', y ='PT', title='Pendidikan PT di Indonesia 2017')
    st.plotly_chart(fig_line4)

# ---- BUBBLE CHARTS ----
st.sidebar.markdown("BUBBLE CHARTS")
choice2 = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '2')

if len(choice2) >0:
    choice_data2 = data[data.Provinsi.isin(choice2)]
    fig_scatter1 = px.scatter(choice_data2, x="SD", y="Provinsi", size="SD", color="Provinsi", hover_name="SD", title='Pendidikan SD di Indonesia 2017', log_x=True, size_max=30)
    st.plotly_chart(fig_scatter1 )

    fig_scatter2 = px.scatter(choice_data2, x="SMP", y="Provinsi", size="SMP", color="Provinsi", hover_name="SMP", title='Pendidikan SMP di Indonesia 2017', log_x=True, size_max=30)
    st.plotly_chart(fig_scatter2 )

    fig_scatter3 = px.scatter(choice_data2, x="SMA", y="Provinsi", size="SMA", color="Provinsi", hover_name="SMA", title='Pendidikan SMA di Indonesia 2017', log_x=True, size_max=30)
    st.plotly_chart(fig_scatter3 )

    fig_scatter4 = px.scatter(choice_data2, x="PT", y="Provinsi", size="PT", color="Provinsi", hover_name="PT", title='Pendidikan PT di Indonesia 2017', log_x=True, size_max=30)
    st.plotly_chart(fig_scatter4 )

# ---- STRIP CHARTS----
st.sidebar.markdown("STRIP CHARTS")
choice3 = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '3')

if len(choice3) >0:
    choice_data3 = data[data.Provinsi.isin(choice3)]
    fig_strip1 = px.strip(choice_data3, x="SD", y="Provinsi", title='Pendidikan SD di Indonesia 2017')
    st.plotly_chart(fig_strip1)

    fig_strip2 = px.strip(choice_data3, x="SMP", y="Provinsi", title='Pendidikan SMP di Indonesia 2017')
    st.plotly_chart(fig_strip2)

    fig_strip3 = px.strip(choice_data3, x="SMA", y="Provinsi", title='Pendidikan SMA di Indonesia 2017')
    st.plotly_chart(fig_strip3)

    fig_strip4 = px.strip(choice_data3, x="PT", y="Provinsi", title='Pendidikan PT di Indonesia 2017')
    st.plotly_chart(fig_strip4)


# ---- POLAR CHART ----
st.sidebar.markdown("POLAR CHART")
choice4 = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '4')

if len(choice4) >0:
    choice_data4 = data[data.Provinsi.isin(choice4)]
    fig_polar1 = px.scatter_polar(choice_data4, r="Provinsi", theta="SD", title='Pendidikan SD di Indonesia 2017')
    st.plotly_chart(fig_polar1)

    fig_polar2 = px.scatter_polar(choice_data4, r="Provinsi", theta="SMP", title='Pendidikan SMP di Indonesia 2017')
    st.plotly_chart(fig_polar2)

    fig_polar3 = px.scatter_polar(choice_data4, r="Provinsi", theta="SMA", title='Pendidikan SMA di Indonesia 2017')
    st.plotly_chart(fig_polar3)

    fig_polar4 = px.scatter_polar(choice_data4, r="Provinsi", theta="PT", title='Pendidikan PT di Indonesia 2017')
    st.plotly_chart(fig_polar4)

# ---- SUNBURST CHART ----
st.sidebar.markdown("SUNBURST CHART")
choice5 = st.sidebar.multiselect("Pilih Provinsi :", ('ACEH','SUMATERA UTARA','SUMATERA BARAT','RIAU','JAMBI','SUMATERA SELATAN','BENGKULU','LAMPUNG','KEP. BANGKA BELITUNG','KEP. BANGKA BELITUNG','KEP. RIAU','DKI JAKARTA','JAWA BARAT','JAWA TENGAH',
'DI YOGYAKARTA','JAWA TIMUR','BANTEN','BALI','NUSA TENGGARA BARAT','NUSA TENGGARA TIMUR','KALIMANTAN BARAT','KALIMANTAN TENGAH','KALIMANTAN SELATAN','KALIMANTAN TIMUR','KALIMANTAN UTARA','SULAWESI UTARA','SULAWESI TENGAH','SULAWESI SELATAN','SULAWESI TENGGARA',
'GORONTALO','SULAWESI BARAT','MALUKU','MALUKU UTARA','PAPUA BARAT','PAPUA'), key = '5')

if len(choice5) >0:
    choice_data5 = data[data.Provinsi.isin(choice5)]
    fig_sunburst1 = px.sunburst(choice_data5,path=['Provinsi'], values='SD', title='Pendidikan SD di Indonesia 2017')
    st.plotly_chart(fig_sunburst1)

    fig_sunburst2 = px.sunburst(choice_data5,path=['Provinsi'], values='SMP', title='Pendidikan SMP di Indonesia 2017')
    st.plotly_chart(fig_sunburst2)

    fig_sunburst3 = px.sunburst(choice_data5,path=['Provinsi'], values='SMA', title='Pendidikan SMA di Indonesia 2017')
    st.plotly_chart(fig_sunburst3)

    fig_sunburst4 = px.sunburst(choice_data5,path=['Provinsi'], values='PT', title='Pendidikan PT di Indonesia 2017')
    st.plotly_chart(fig_sunburst4)