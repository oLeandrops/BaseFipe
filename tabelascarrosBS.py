from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

url = 'https://tabelacarros.com/marcas/carros#'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text,'html.parser')
elemento = soup.find_all('h1')
print(elemento)