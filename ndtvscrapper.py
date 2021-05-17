from trial import display_data
import streamlit as st
import pandas as pd
import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from wordclouddata import Displaying_data

## create an array with URLs
#urls = ['https://ndtv.in/india-news/centre-says-it-may-blacklist-certain-telecom-equipment-vendors-amid-tension-with-china-2339437',
 #           'https://ndtv.in/world-news/us-biden-declared-national-security-team-three-women-included-2329307'

    
#]
def Web_Scrapper(urls):
    st.markdown("<h1 style='text-align: center; color: white;'>Polarity Classification</h1>", unsafe_allow_html=True)
    for url in urls:
        page=requests.get(url)
        page.text
        soup=BeautifulSoup(page.text,'html.parser')
        soup.find('p', class_='ft-social--txt').decompose()
        soup.find('div', class_='ft-social--wrap').decompose()
        soup.find('div',  attrs={'id':'jiosaavn-widget'}).decompose()
        soup.find('div',  attrs={'class':'ins_instory_dv'}).decompose()

        soup.find('aside', class_='col-300').decompose()
        soup.find('div',  attrs={'class':'reltd-main'}).decompose()
        
        headline_ele=soup.find("div",{'class':"sp-ttl-wrp"}).h1.text
        print("headline:",headline_ele)
        print("\n")
        
        print("DESCRIPTION")
        print("\n")
        
        description_name=[]
        description_ele=soup.find_all("p")
        
        for item in description_ele:
            description_name.append(item.text)
        #print(description_name)
    
        
        str1 = ''.join(description_name)


        x = str1.split('.')
        y = str1.replace(".", ".\n")

        print(y)
        print(url)
        st.text_input("URL",url)
        headline = st.text_input("Headline",headline_ele)

        st.text_area("Description",y,1000)

        print("\n")
    
        display_data(y)   
        st.markdown(
            f"""
            <style>
            <br> <br>       

            }}
            

            </style>
            """,
            unsafe_allow_html=True
        )
        Displaying_data(y)
       
        