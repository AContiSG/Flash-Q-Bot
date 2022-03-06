from bs4 import BeautifulSoup
import requests


def buscar_anime(anime):
    animeConSumas=anime.replace(' ','+')
    print(animeConSumas)
    busqueda = requests.get(url= "https://duckduckgo.com/?q=site%3Amyanimelist.net+"+ animeConSumas + "&ia=software", headers={"user-agent": "my-app/0.0.1"})
    #print(busqueda.text)
    urlParseada = BeautifulSoup(busqueda.content, "html.parser")
    print(urlParseada)
    link = urlParseada.find_all(class_="result__a js-result-title-link")
    #.find(class_="result__a js-result-title-link").get('href')
    return link

print(buscar_anime("violet evergarden"))
#print(buscar_anime("fate heavens feel 1"))

def buscarAnime(anime):
