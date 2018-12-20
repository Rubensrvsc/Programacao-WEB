import requests

cep = '64218110'
url = "https://viacep.com.br/ws/{cep}/json/"
url = url.format(cep=cep)

response = requests.get(url).json()
#print (response)

print ("logradouro: %s \n Bairro: %s \n localidade: %s \n UF: %s"
       % (response['logradouro'],response['bairro'], response['localidade'],
          response['uf']))
