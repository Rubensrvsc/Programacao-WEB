#Tradução
'''import requests, json
key = 'key'
q = 'Prezados, boa tarde, gerem uma chave para a API.'
target = 'en'
url ='https://translation.googleapis.com/language/translate/v2'
params = {'key':key,'q':q,'target':target}
response = requests.get(url, params=params)
json = response.json()
print(json)'''

#Localização
'''import requests
key = 'key'
localizacao = "Avenida frei serafim"
url ='https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (localizacao, key)
response = requests.get(url)
json = response.json()
print (json)
latitude = json['results'][0]['geometry']['location']['lat']
longitude = json['results'][0]['geometry']['location']['lng']
print('Latitude: %f - Longitude: %f' % (latitude, longitude ))'''

