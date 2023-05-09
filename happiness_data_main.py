import streamlit as st
from plotly import express as px
import columns

st.title('In Search for Happiness')

my_cols = [let.title().replace("_", " ") for let in columns.columns()]


data1 = st.selectbox(label='Select data for the X axis',
                     options=my_cols, key='1')
data1_plot = columns.compare(data1)

data2 = st.selectbox(label='Select data for the X axis',
                     options=my_cols, key='2')
data2_plot = columns.compare(data2)

st.subheader(f'{data1} and {data2}')


figure = px.line(x=data1_plot, y=data2_plot, labels={'x': f'{data1}', 'y': f'{data2}'})
st.plotly_chart(figure)
