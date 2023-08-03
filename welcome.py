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


el_x =st.selectbox('select x element', el_list)
el_y =st.selectbox('select y element', el_list)

file_name=st.selectbox('select file', file_name_list)


p = figure(x_axis_label='X', y_axis_label='Y') #title

p.circle(df[el_x], df[el_y]) #color, size, alpha
p.line([np.min(df[el_x]), np.max(df[el_y])], ([np.mean(df[el_x]), np.mean(df[el_y])]))
                                                                   
#p.line([0,20], [5,5]) #line_width=2, line_color='green'
#p.rect(x=24, y=4, height=3, color='yellow')

st.header("plot")
st.bokeh_chart(p)
