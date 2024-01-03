
######### PROJETO C-127 AQUI ##########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd 
import requests

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get(start_url)

time.sleep(10)

scarped_data=[]

#Defina o método de coleta de dados 
def scrape():
    soup=BeautifulSoup(browser.page_source, "html.parser")
    #Localize <table>
    bright_star_table= soup.find_all("table", attrs=["class", "wikitable"])

    #Localize <tbody>
    table_body= bright_star_table.find_all("tbody")

    #Localize <tr>
    table_rows= table_body.find_all("tr")

    #Obtenha os dados de <td>
    for row in table_rows:
        table_cols= row.find_all("td")
        print (table_cols)

        temp_list=[]

        for col_data in table_cols:
            #Imprima somente colunas de dados textuais usando a propriedade ".text"
            print(col_data.text)
            
            #Remova os espaçoes em branco extras usando o método strip()
            data= col_data.text.strip()
            print(data)

            temp_list.append(data)
        #Anexe os dados a lista scarped_data    
        scarped_data.append(temp_list)    
        
    stars_data=[]  

    for i in range(0,len(scarped_data)):
        Star_names= scarped_data[i][1]
        Distance= scarped_data[i][3]
        Mass= scarped_data[i][5]
        Radius= scarped_data[i][6]
        Lum= scarped_data[i][7]

        required_data= [Star_names, Distance, Mass, Radius, Lum]
        stars_data.append(required_data)  

    #Defina o cabeçalho 
    headers= ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]
    #Defina o dataframe do pandas
    star_df_1= pd.DataFrame(stars_data, colums=headers)
    #Converta para CSV
    star_df_1.to_csv("scraped_data.csv", index=True, index_label="id")


