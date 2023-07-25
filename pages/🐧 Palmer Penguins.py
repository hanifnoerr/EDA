import streamlit as st
import pandas as pd
from palmerpenguins import load_penguins
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(initial_sidebar_state="collapsed")

st.header('🐧 Palmers Penguins Exploratory Data Analysis')

data = load_penguins()

with st.expander('Sample Dataset'):
    st.code('data.sample(5)')
    st.dataframe(data.sample(5))
    
with st.expander('Data Shape'):
    st.code('data.shape')
    st.write(data.shape)
    
with st.expander('Proporsi data spesies'):
    st.code('data.species.value_counts().plot(kind="bar")')
    st.bar_chart(data.species.value_counts())
    st.write(' ')
    st.write('spesies per pulau')
    st.code('sns.countplot(x="island", hue="species", data=data)')
    sns.countplot(x="island", hue="species", data=data)
    st.pyplot(plt)

with st.expander('Missing Value'):
    st.code('data.isnull().sum()')
    st.write(data.isnull().sum())
    st.write('Jika ingin melihat persentase missing value:')
    st.code('data.isnull().sum()/len(data)')
    st.write(data.isnull().sum()/len(data))
    
with st.expander('Simpulan Statistik'):
    st.code('data.describe().T')
    st.write(data.describe().T)
    
with st.expander('Pairplot'):
    st.code("sns.pairplot(data=data, hue='species')")
    sns.pairplot(data=data, hue='species')
    st.pyplot(plt)


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
    
# pair plot, color = spesies

