import streamlit as st
import pandas as pd
import numpy as np
import csv
import base64
import xlsxwriter
from subprocess import call
from indiatv import *
from csv import reader
main_bg = "Polarity.jpg"
main_bg_ext = "jpg"


def Polarity():
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

    st.markdown("<h1 style='text-align: center; color: white;'>Polarity Classification</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
    name1 = st.text_input("","https://" )
    name = ([name1])
    st.write(name)
    if st.button("Analyze"):
        
        #df=pd.DataFrame([name])
        #df.to_csv('data.csv')
        filename='data.csv'
        with open(filename,'w') as csvwrite:
            csvwriter=csv.writer(csvwrite,delimiter='-')
            csvwriter.writerow(name)
        Web_Scrapping()
        # wb = xlsxwriter.Workbook(filename)
        # ws = wb.add_worksheet()
        # ws.write(name)
        # wb.close()
        

        