#Zadanie 9.2 obsluga API
import requests
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('waluty.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    csv_writer.writerow(data[0]['rates'][0])

def lista_kodow():
    """Dostepne waluty po kodzie"""
    kody = []    
    for kod in range(len(data[0]['rates'])):
        kody.append(data[0]['rates'][kod]['code'])
    return kody

def lista_walut():
    """Dostepne waluty po nazwie"""
    waluty = []
    for waluta in range(len(data[0]['rates'])):
        print(data[0]['rates'][waluta]['currency'])
    return waluty

def slownik_kodow(kody_walut):
    '''zindeksowane kody walut'''
    slownik_kodow = {key: i for i, key in enumerate(kody_walut) }
    return slownik_kodow

def waluta_ask_price(kod_waluty):
    '''cena ask waluty'''
    kody = lista_kodow()
    kody_dict = slownik_kodow(kody)
    if kod_waluty in kody:
        return data[0]['rates'][kody_dict[kod_waluty]]['ask']

def kalkulator_walut(waluta, kwota):
    '''przelicza wartosc waluty'''
    wynik = waluta * float(kwota)
    return wynik

@app.route("/", methods=["GET","POST"])
def homepage():
    '''strona glowna kantoru'''
    kody = lista_kodow()
    
    if request.method == "POST":
        data = request.form
        waluta = data.get('waluta')
        kwota = data.get('kwota')
        ask_price = waluta_ask_price(waluta)
        wynik = round(kalkulator_walut(ask_price,kwota),2)
        return render_template('homepage.html', kody=kody, wynik=wynik)
    else:

        print('nope')
        return render_template('homepage.html', kody=kody)

if __name__ == '__main__':
    app.run(debug=True)