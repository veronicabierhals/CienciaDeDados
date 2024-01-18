import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import pandas as pd

html = requests.get(
    "https://statisticstimes.com/tech/top-computer-languages.php").content
soup = BeautifulSoup(html, 'html5lib')

# find busca o primeiro que ele achar
primeiro_paragrafo = soup.find('p')
# print(primeiro_paragrafo) # aparece com as tags
# print(primeiro_paragrafo.text) # aparece somente texto

# find_all busca tudo que tem e joga em uma lista
todos_paragrafos = soup.find_all('p')
# print(todos_paragrafos) # lista todos os parágrafos
# print(todos_paragrafos[0].text) # imprime somente o primeiro parágrafo

todos_links = soup.find_all('a')
# print(todos_links)

'''
abre o site e busca no código HTML dele o nome da informação que deseja coletar
'''
# busca table com nome table_id na parte de tbody (todas essas infos são retiradas do site)
tabela = soup.find('table', {'id': 'table_id1'}).find('tbody')
print(tabela)

linhas=tabela.find_all('tr')
for linha in linhas:
    dados = linha.find_all('td')
    print(dados[0].text)
    print(dados[2].text)
    print(dados[3].text)
    print('------')

# continua no arquivos Colab
