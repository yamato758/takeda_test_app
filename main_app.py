from audioop import add
import code
from email.mime import image
from encodings import utf_8
from gettext import install
from re import I
from readline import insert_text
from this import d
import streamlit as st
from PIL import Image
import pandas as pd

st.title('竹田アプリ')
st.caption('竹田アプリです。')

image = Image.open('./data/スクリーンショット 2022-09-19 100930.png')
st.image(image,width=200)