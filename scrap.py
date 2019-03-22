from bs4 import BeautifulSoup
import csv

raw_html = open('Socios.html').read()
html = BeautifulSoup(raw_html, 'html.parser')

empresas = []

tablaEmpresas = html.select('#socios-list')
filasEmpresas = tablaEmpresas[0].findChildren('div', {"class": "vanilla"})

for fila in filasEmpresas:
    empresa = {}
    empresa['logo'] = fila.findChild('div', {"class": "logo"}).select('img')[0]
    empresa['nombre'] = fila.findChild('div', {"class": "detail"}).select('h1')[0].text
    empresa['leyenda'] = fila.findChild('div', {"class": "detail"}).select('h2')[0].text
    empresa['descripcion'] = fila.findChild('div', {"class": "detail"}).select('p')[0].text
#    direccion = 
    if len(fila.select('address')[0].text.split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')) > 2:
        empresa['calle'] = fila.select('address')[0].text.split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[1].split('\n')[0]
        empresa['ciudad'] = fila.select('address')[0].text.split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[2].split('\n')[0]
    else:
        empresa['ciudad'] = fila.select('address')[0].text.split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[0].split('\n')[0]
        empresa['calle'] = ""
    empresa['telefono'] = fila.select('address')[0].findChild('div', {"class": "phone"}).text
    empresa['mail'] = fila.select('address')[0].findChild('div', {"class": "email"}).text.split('\n')[1]
    if fila.select('address')[0].findChild('div', {"class": "web"}) is not None:
        empresa['web'] = fila.select('address')[0].findChild('div', {"class": "web"}).text.split('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')[1].split('\t')[1]
    else:
        empresa['web'] = ""
    empresas.append(empresa)

for e in empresas:
    print((e['nombre'] + "            ")[:20] + "\t" + e['ciudad'])
    


with open('empresas.csv', mode='w') as csv_file:
    fieldnames = ['logo', 'nombre', 'leyenda', 'descripcion', 'calle', 'ciudad', 'telefono', 'mail', 'web']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for empresa in empresas:
        writer.writerow(empresa)

    
