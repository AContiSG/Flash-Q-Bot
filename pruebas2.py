from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

def andios(anime):
    animeConSumas=anime.replace(' ','+')
    url= "https://duckduckgo.com/?q=site%3Amyanimelist.net+"+ animeConSumas + "&ia=software"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/webdrivers/chromedriver.exe",options=option)
    driver.get(url)
    time.sleep(3) # give page a chance to fully load
    codigohtml=driver.page_source
    urlParseada = BeautifulSoup(codigohtml, "html.parser")
    link = urlParseada.find(id="r1-0").find(class_="result__a js-result-title-link").get("href")
    print(link)



andios("violet evergarden")