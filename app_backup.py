#Zadanie 9.2 obsluga API

import requests
from flask import Flask, render_template, request
import json
import pickle
import csv
from werkzeug.datastructures import MultiDict

app = Flask(__name__)
dane = ('currency','code','bid','ask')

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('waluty2.csv','w', newline='') as f:
    fieldnames = ['rates']
    csv_writer = csv.writer(f, delimiter=';')
    csv_writer.writerow(data[0]['rates'][0])


#pobranie listy kodow z pliku
lista_kodow = []
for kod in range(len(data[0]['rates'])):
    lista_kodow.append(data[0]['rates'][kod]['code'])

"""for multi in range(len(data[0]['rates'])):
    d = MultiDict(data[0]['rates'][multi])
    print(d)"""

# wyciaga dane o walucie
x= MultiDict(data[0])

with open('waluty.csv', 'w', newline='') as csvfile:
    fieldnames = ['rates']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writerows(data)

with open('waluty.csv','r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)


with open('waluty.csv','r') as csv_f:
    csv_reader_f = csv.DictReader(csv_f)

    for line in csv_reader_f:
        print(line)


"""for line in csv_reader:
print(line)"""


        

#currency;code;bid;ask

#colummy




#print(type(data[0]))
#print(data[0]['rates'][0]['code'])  

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        print('postpostpost')

    return render_template('homepage.html')