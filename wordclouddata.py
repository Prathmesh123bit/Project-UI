from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import numpy as np
import pandas as pd
import xmltodict
from pandas import *
import urllib.request
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
from PIL import Image
import gender_guesser.detector as gender
from streamlit_lottie import st_lottie
import requests

def Displaying_data(txt):
  
    url = "https://hindityping.info/download/assets/Hindi-Fonts-Unicode/gargi.ttf"
    r = requests.get(url, allow_redirects=True)
    font_path="gargi.ttf"

    with open(font_path, "wb") as fw:
      fw.write(r.content)

       
    text=txt
    
    wordcloud = WordCloud(max_font_size=50, max_words=100,regexp=r"[\u0900-\u097F]+", background_color="white",font_path=font_path).generate(text)
    wordcloud.generate(text)
    plt.figure(figsize=(100,100))
    fig,axes=plt.subplots()
    plt.imshow(wordcloud, interpolation="bilinear")
    
    plt.axis("off")
    
    st.pyplot(fig)
  
  
    url = "https://hindityping.info/download/assets/Hindi-Fonts-Unicode/gargi.ttf"

    r = requests.get(url, allow_redirects=True)
    font_path="gargi.ttf"

    with open(font_path, "wb") as fw:
      fw.write(r.content)

      text="       सकारात्मक कण "
      
    wordcloud = WordCloud(max_font_size=50, max_words=100,regexp=r"[\u0900-\u097F]+", background_color="white",font_path=font_path).generate(text)
    wordcloud.generate(text)
    plt.figure(figsize=(100,100))
    fig,axes=plt.subplots()
    plt.imshow(wordcloud, interpolation="bilinear")
  
    plt.axis("off")
  
    st.pyplot(fig)
  

    
    


