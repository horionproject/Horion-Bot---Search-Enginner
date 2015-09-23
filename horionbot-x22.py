#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HORION BOT versão X2.2;
# Protótipo: http://31.220.49.93:8228 -> bot parado, aprox. 264K de resultados pelo bot;

# Importando Bibliotecas;
# Por: Raphael Paulo, Raphael Rodriguez e Pedro Souza;
import urllib
from bs4 import BeautifulSoup
import os
import MySQLdb
import config

# Conexão com o MySQL;
con = MySQLdb.connect(host='localhost', user='root', passwd='<$#js72j109kk22uHEG#2@PPPp4P',db='search')
c = con.cursor()

# Variáveis Globais;
ATIVA     = "1"

# Conexão com o Bing e pesquisa da palavra digitada;
def getInfo(dork, depth):
  global TITULO, URL, DESCRICAO
  dork = dork.replace(" ", "+")
  link = "http://www.bing.com/search?q=" + dork + "&first=" + str(cont)
  soup = BeautifulSoup(urllib.urlopen(link).read())
  for li in soup.find_all('li', {'class':"b_algo"}):
    for h2 in li.find_all('h2'):
      print("TITULO: " + h2.find('a').getText().encode('utf-8'))
      TITULO = h2.find('a').getText().encode('utf-8')
      URL = h2.find('a').get('href').encode('utf-8')
    for p in li.find_all('p'):
      DESCRICAO = p.getText().encode('utf-8')
	  
	# Espécie de "bind automática", para busca de dados existentes;
	sql  = ("SELECT * FROM noticias WHERE titulo IN '%s'", TITULO)
	sql2 = ("SELECT * FROM noticias WHERE texto IN '%s'", DESCRICAO)
	sql3 = ("SELECT * FROM noticias WHERE url IN '%s'", URL)
	#data=cursor.fetchall()
	#print(data)

	# Condição que testa dado obtido com dado no MySQL;
	 if (sql==TITULO):
	 print("descarta")
	 break
	 elif (sql2==DESC):
	 print("descarta")
	 break
	 elif (sql3==URL):
	 print("descarta")
	 break
	 
	 else:
    #Executando a query, caso não exista o dado, para armazena-lo;
    query = ("""INSERT INTO noticias (titulo, texto, ativa, url) VALUES (%s, %s, %s, %s)""", (TITULO, DESCRICAO, ATIVA, URL))
    c.execute(*query)
    con.commit()

	cont = 1
	reset = 0
	dork = raw_input("Dork: ") #Digitado pelo User, irei implementar uma WordList;

while True:
  print("CONTADOR " + str(cont) + " : ----------------------------")
  getInfo(dork, cont)
  cont += 10
  reset += 10

  if reset == 100:
    print ("###### RENOVANDO IP ######") #Troca de IP na rede TOR, evitando ban de IP pelas buscas;
    os.system("[ -z 'pidof tor' ] || pidof tor | xargs sudo kill -HUP;")
    reset = 0
