#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
c = csv.writer(open("clasificacion.csv", "wb"))

url = "http://www.marca.com/futbol/primera/clasificacion.html?cid=MENUDES3601&s_kw=futbol_liga-bbva_clasificacion"
r = requests.get(url)
soup = BeautifulSoup(r.content)


c.writerow(["Posicion","Equipo","P.J.","P.G.","P.E.","P.P.","G.F.","G.C.","Ptos"])

listas = []

table = soup.find("table")
for row in table.findAll("tr"):
	celdas = row.findAll("td")
	fila = []
	celdas2 = celdas[:9]
	for celda in celdas2:
		dato = celda.string
		fila.append(dato)
	listas.append(fila)



listas = listas[2:]
for equipo in listas:
	l = []
	for col in equipo:
		l.append(col.encode('utf8'))
	c.writerow(l)
