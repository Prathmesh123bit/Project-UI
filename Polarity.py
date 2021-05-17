import streamlit as st
import pandas as pd
import numpy as np
import csv
import base64
import xlsxwriter
from indiatv import *
from subprocess import call
from ndtvscrapper import *
from csv import reader
main_bg = "bg.jpg"
main_bg_ext = "jpg"


def Polarity():
#    st.markdown(
 #       f"""
  #      <style>


   #     .reportview-container {{
     #       background-image: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
    #        background-size: cover;
      #      background-repeat: no-repeat;        
      #  }}


       # </style>
        #""",
     #   unsafe_allow_html=True
    #)
    select_option=['NDTV Article','INDIATV Article']
    page=st.sidebar.radio('',select_option)
    if page=='NDTV Article':
      st.sidebar.markdown("<h3 style='text-align: center; color: yellow;'>NDTV Article</h3>", unsafe_allow_html=True)
      st.sidebar.markdown("<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
      name1 = st.sidebar.text_input("","https://" )
      ana=st.sidebar.button("Analyze")
      name = ([name1])
      if ana:
        url=name
        #st.write(url)
        #url.append(name)
        #filename='data.csv'
        #with open(filename,'w') as csvwrite:
         #   csvwriter=csv.writer(csvwrite,delimiter='-')
          #  csvwriter.writerow(name)
        Web_Scrapper(url)

    else:
      st.sidebar.markdown("<h3 style='text-align: center; color: yellow;'>INDTV Article</h3>", unsafe_allow_html=True)
      st.sidebar.markdown("<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
      name2 = st.sidebar.text_input("","https://" )
      ana1=st.sidebar.button("Analyze")
      name3 = ([name2])
      if ana1:
        url=name3
       # st.write(url)
        web_Scrapping(url)

        