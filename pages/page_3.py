import streamlit as st
import pandas as pd

df = pd.read_csv('./data/東日本営業部.csv')
st.dataframe(df)