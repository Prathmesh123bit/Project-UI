import streamlit as st
import pandas as pd
import numpy as np
import base64
from Polarity import *
from Headline import Headline

main_bg = "Polarity.jpg"
main_bg_ext = "jpg"


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

st.markdown("<h1 style='text-align: center; color: Red;'>What do You Want to  do</h1>", unsafe_allow_html=True)


# pol=st.button("Polarity Classification")
# st.markdown("""<br>""",True)
# head=st.button("Headline Classification")

Polarity()
Headline()