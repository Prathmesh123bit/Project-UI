import streamlit as st
import pandas as pd
import numpy as np
import base64
from Polarity import *
from Headline import * 

main_bg = "Polarity.jpg"
main_bg_ext = "jpg"

st.sidebar.title("Polarity Classification")

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-image: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover;
        background-repeat: no-repeat;        

    }}
    

    </style>
    """,
    unsafe_allow_html=True
)

 

st.markdown("<h1 style='text-align: center; color: white;'>Sentiment Analysis Of Hindi News Articles</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: Red;'>A Ui based Model which is used to find the Polarity of the articles based on the sentiments</h5>", unsafe_allow_html=True)

Polarity()


#Headline()