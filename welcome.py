import streamlit as st
import pandas as pd 
import os

file_name_list=[]
for i in os.listdir():

if i.endswith('csv'):
st.write('Hello world')

df=pd.read_csv('C:/Users/korkm/Downloads/Exercises & Data/data/Bastar craton.csv')
st.dataframe(df)

el_list=df.columns.tolist()[27:80]
x_axis=st.selectbox('select element',el_list)
