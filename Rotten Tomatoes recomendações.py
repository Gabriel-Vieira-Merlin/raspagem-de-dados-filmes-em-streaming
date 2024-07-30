#Importa a biblioteca requests e a biblioteca Beautiul Soup
import requests
from bs4 import BeautifulSoup

#Armazena a URL na variável URL
url = 'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular'

#Armazena a request para o site na variável request
req = requests.get(url)

#Cria o objeto BeatifulSoup
soup = BeautifulSoup(req.text, "lxml")

#Armazena os filmes em uma variável
lista_filmes_prov = soup.select(".p--small") #Provisória
lista_filmes_prov2 = [] #Provisória 2
lista_filmes = [] #Onde será adicionada os filme após edição

#Laço de repetição para extrair só o texto dos span
for filme in lista_filmes_prov:
       lista_filmes_prov2.append(filme.text)

#Laço de repetição para tirar espaços dos nomes dos filmes
for filme in lista_filmes_prov2:
       lista_filmes.append(filme.strip())

#Excluiu os 4 primeiros da lista
lista_filmes = lista_filmes[4:]

#Lista de repetição para apresentar melhor a lista junto com o índice
for filme in lista_filmes:
       print(f'{lista_filmes.index(filme)}) {filme}\n')
