
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from time import sleep

requisicao = webdriver.Chrome()
requisicao.get('https://siteexemplo.com.br/')

dic_ = {'Categoria':[], 'URL':[]}

soup = BeautifulSoup(requisicao.page_source)
sleep(10)

#inserir tag e classe respectiva ao menu navegacional
resp = soup.find('div-exemplo', class_ = 'exemplo-classe')

for urls in resp.find_all('a'):
    URL = urls.get('href')
    dic_['URL'].append(str(URL))

for categorias in resp.find_all('a'):
    #inserir a tag respecitiva ao nome das categorias
    categoria = categorias.get_text('span-exemplo')
    dic_['Categoria'].append(str(categoria))
print(dic_)

#Exportando os arquivos
df = pd.DataFrame(dic_, columns=['Categoria', 'URL'])
print(df)
df.to_csv("saida.csv", encoding='utf-8')
