import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

cep = str(14020570)

payload = {'relaxation': cep, 'semelhante': 'N', 'tipoCEP': 'ALL'}
xml_data = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data=payload).content

if __name__ == '__main__':
    model = BeautifulSoup(xml_data, features='lxml')
    fields = []
    table_data = []
    for tr in model.table.find_all('tr', recursive=False):
        for th in tr.find_all('th', recursive=False):
            fields.append(th.text)
    for tr in model.table.find_all('tr', recursive=False):
        datum = {}
        for i, td in enumerate(tr.find_all('td', recursive=False)):
            datum[fields[i]] = td.text
        if datum:
            table_data.append(datum)

    print(json.dumps(table_data, indent=4))

#print(conteudo.findAll("table", class_="tmptabela"))
