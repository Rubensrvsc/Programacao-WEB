import requests
response=requests.get("http://www.google.com")
print (response)
print (response.headers["content-length"])
for i in response.text:
    if(i!="s".lower()):
        print (i)

