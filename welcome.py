import streamlit as st
import pandas as pd 
st.write('Hello world')

df=pd.read_csv('Bastar craton.csv')
st.dataframe(df)
