#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("goleadores.csv", "wb"))

url = "http://www.resultados-futbol.com/estadisticas/Granada"
r = requests.get(url)
soup = BeautifulSoup(r.content)


table = soup.find("div","tipo goles cards3")
titulo = table.find("div","tit")

cabecera = []
cabecera.append(titulo.string.encode('utf8'))
cabecera.append("Goles")
c.writerow(cabecera)

items = table.findAll("div", "eitem")
for item in items:
	fila = []
	a=item.find("span","jug")
	nombrejudador = a.find("a")
	fila.append(nombrejudador.string.encode('utf8'))
	num_goles=item.find("span", "num")
	fila.append(num_goles.string.encode('utf8'))
	c.writerow(fila)
