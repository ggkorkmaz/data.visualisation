from bokeh.plotting import figure,show

import streamlit as st
import pandas as pd 
import os

file_name_list=[]
for i in os.listdir():
  if i.endswith('.csv'): 
    file_name_list.append(i)
  
df=pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list=df.columns.tolist()[27:100]
#x_axis=st.selectbox('select element', el_list)

el_x =st.selectbox('select x element', el_list)
el_y =st.selectbox('select y element', el_list)

file_name=st.selectbox('select file', file_name_list)

df=pd.read_csv('file_name')
p = figure(x_axis_label='X', y_axis_label='Y')

p.circle(df[el_x], df[el_y])

st.bokeh_chart(p)
