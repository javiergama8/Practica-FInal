#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("plantillagranadab.csv", "wb"))

url = "http://www.resultados-futbol.com/Granada-B"
r = requests.get(url)
soup = BeautifulSoup(r.content)

table = soup.find("table","sdata_table")

cabecera = ["Jugador","Goles","Tarjetas Rojas","Tarjetas Amarillas"]
c.writerow(cabecera)
tbody = table.find("tbody")


trs = tbody.findAll("tr",itemprop="employee")
for tr in trs:
	lista = []
	nombre = tr.find("span",itemprop="name")
	lista.append(nombre.string.encode('utf8'))

	datos = tr.findAll("td","dat")
	datos2 = datos[2:]
	
	for i in datos2:
		lista.append(i.string.encode('utf8'))
	c.writerow(lista)
