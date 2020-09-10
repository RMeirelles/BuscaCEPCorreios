import requests
import json
from bs4 import BeautifulSoup


print('Qual o CEP a ser pesquisado?')

while True:

    cep = str(input('> '))

    if len(cep) == 8 and cep.isnumeric() :
            
        payload = {'relaxation': cep, 'semelhante': 'N', 'tipoCEP': 'ALL'}
        html_data = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data=payload).text

        if BeautifulSoup(html_data, features='lxml').table is None:
            print('O CEP não foi encontrado na base de dados!')

        else:

            if __name__ == '__main__':
                model = BeautifulSoup(html_data, features='lxml')
                tituloCampo = []
                dataCampo = []
                for tr in model.table.find_all('tr', recursive=False):
                    for th in tr.find_all('th', recursive=False):
                        tituloCampo.append(th.text)
                for tr in model.table.find_all('tr', recursive=False):
                    datum = {}
                    for i, td in enumerate(tr.find_all('td', recursive=False)):
                        datum[tituloCampo[i]] = td.text
                    if datum:
                        dataCampo.append(datum)


            print(json.dumps(dataCampo, indent=2, ensure_ascii=False))
            break

    else:
        print('Digite um CEP válido!')
