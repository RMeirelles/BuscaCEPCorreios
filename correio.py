import requests
from urllib.request import urlopen

cep = str(14051120)

payload = {'relaxation': cep, 'semelhante': 'N', 'tipoCEP': 'ALL'}
r = requests.post("http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data=payload)
print(r.encoding)
conteudo = str((r.content))

cep = cep[:5]+'-'+cep[-3:]
inicio = conteudo.index('Logradouro/Nome:')

fim = conteudo.index(cep)+9

print(conteudo[inicio:fim])

#Logradouro/Nome:</th>\r<th width="90">Bairro/Distrito:</th>\r<th width="80">Localidade/UF:</th>\r<th width="50">CEP:</th>\r</tr>\r<tr>\r\r<td width="150">Rua Maracaj\xfa - de 273/274 ao fim&nbsp;</td>\r\r<td>Vila Monte Alegre&nbsp;</td>\r<td>Ribeir\xe3o Preto/SP&nbsp;</td>\r\r<td width="55">14051-120

# Logradouro/Nome:
# </th>\r<th width="90">
# Bairro/Distrito:
# </th>\r<th width="80">
# Localidade/UF:
# </th>\r<th width="50">
# CEP:
# </th>\r</tr>
# \r<tr>\r\r
# <td width="150">&nbsp;</td>\r \r<td>Bonfim Paulista</td>\r<td>Ribeir\xe3o Preto/SP</td>\r\r<td width="55">14110-000