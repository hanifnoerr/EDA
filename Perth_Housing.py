import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(initial_sidebar_state="collapsed")
st.header('🏘️ Perth Housing Exploratory Data Analysis')

#load data
data = pd.read_csv('Perth Housing.csv')

with st.expander('Sample Dataset'):
    st.code('data.sample(5)')
    st.dataframe(data.sample(5))
    
with st.expander('Data Shape'):
    st.code('data.shape')
    st.write(data.shape)

with st.expander('Data Unik'):
    st.code('''
#total variabel unik pada kolom SUBURB
data.SUBURB.nunique()
#menampilkan semua variabel unik pada kolom SUBURB
data.SUBURB.unique()
            ''')
    st.write(data.SUBURB.nunique())
    
with st.expander('Simpulan Statistik'):
    st.code('data.describe().T')
    st.write(data.describe().T)
    
with st.expander('Missing Value'):
    st.code('data.isnull().sum()')
    st.write(data.isnull().sum())
    st.write('Jika ingin melihat persentase missing value:')
    st.code('data.isnull().sum()/len(data)')
    st.write(data.isnull().sum()/len(data))
    
with st.expander('Matriks Korelasi'):
    st.code('''import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sns.heatmap(data.corr(), ax=ax)
st.write(fig)''')
    num_col = data.select_dtypes(exclude = "object").columns
    fig,ax = plt.subplots()
    ax.set_title('Matriks Korelasi')
    sns.heatmap(data[num_col.to_list()].corr().round(1), ax=ax,  annot=True)
    st.write(fig)

with st.expander('Histogram'):
    st.code('''fig = plt.figure(figsize = (25,25))
ax = fig.gca()
data.hist(ax=ax, bins=50)
st.pyplot(fig)''')
    
    fig2 = plt.figure(figsize = (25,25))
    ax = fig2.gca()
    data.hist(ax=ax, bins=50)
    st.pyplot(fig2)
    
with st.expander('Boxplot'):
    st.code('''fig = plt.figure(figsize = (25,25))
ax = fig.gca()
data.hist(ax=ax, bins=50)
st.pyplot(fig)''')
    
    fig3 = plt.figure()
    ax = fig3.gca()
    data.boxplot(ax=ax)
    st.pyplot(fig3)
    
with st.expander('Map'):
    map = pd.read_json('https://raw.githubusercontent.com/tonywr71/GeoJson-Data/master/australian-states.json')
    data_plot = data[['LATITUDE', 'LONGITUDE', 'PRICE', 'BUILD_YEAR']]
    data_plot.rename(columns={'LATITUDE': 'lat', 'LONGITUDE': 'long', 'BUILD_YEAR':'Tahun Pembuatan', 'PRICE':'Harga'}, inplace=True)
    fig4 = px.scatter_mapbox(data_plot, lat='lat', lon='long', hover_data=['Tahun Pembuatan'], color='Harga', height=600, width=650)
    fig4.update_layout(mapbox_style="open-street-map")
    st.write(fig4)
