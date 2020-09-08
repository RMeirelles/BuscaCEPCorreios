import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

cep = str(14030000)

payload = {'relaxation': cep, 'semelhante': 'N', 'tipoCEP': 'ALL'}
r = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data=payload)

conteudo = BeautifulSoup(r.content)

print(conteudo.prettify())

# conteudo = str((r.content))

# cep = cep[:5]+'-'+cep[-3:]
# inicio = conteudo.index('Logradouro/Nome:')

# fim = conteudo.index(cep)+9

# print(conteudo[inicio:fim])

