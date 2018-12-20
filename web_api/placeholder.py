import requests

url = 'https://jsonplaceholder.typicode.com/todos/'
dados = {
"userId": 1,
"title": 'ok placeholder',
"completed": False
}
response = requests.post(url, data = dados)
print(response.json())
up={
"userId": 1,
"title": 'ok',
"completed": False
}
response = requests.patch(url, data={"title":"ok"})
#response = requests.delete(url + '210')
# 404
print(response.json())
