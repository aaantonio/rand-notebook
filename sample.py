from bs4 import BeautifulSoup
import requests

url = ''

source = requests.get(url)
soup = BeautifulSoup(source.text)

