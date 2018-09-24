import requests
from lxml.html import fromstring as parser
from bs4 import BeautifulSoup
import urllib
def main():
    busca_url()
    baixar_arquivo()
    busca_link()
    pass

def busca_url():
    site="http://www.google.com"
    response=requests.get(site)
    print (response.status_code)
    print (response.headers)
    print (response.headers["content-length"])
    pass

def baixar_arquivo():
    url = "http://ap.imagensbrasil.org/images/imagens-lobos.jpg"
    r = requests.get(url)
    with open("imagens-lobos.jpg", "wb") as code:
        code.write(r.content)

def busca_link():
    response=requests.get("http://www.google.com")
    html = parser(response.text)
    soup = BeautifulSoup(response.text,"lxml")

    print("Links")
    all_links=soup.find_all("a")
    for link in all_links:
        print(link.get("href"))

    print(soup.find_all("src"))

    print("\nNome do link")
    links=soup.a
    lista_links=[]
    for i in links:
        lista_links.append(i)
    for i in lista_links:
        print (i)
    pass
if __name__=="__main__":
    main()
