
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import requests


# In[2]:

url = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=AED&To=PHP'


# In[3]:

headers = {'User-Agent': 'Mozilla/5.0'}
source = requests.get(url, headers=headers)


# print(source.text)

# In[4]:

soup = BeautifulSoup(source.text, 'html.parser')


# In[5]:

php = soup.find_all('td', {'class':'rightCol'})[0].get_text()


# In[6]:

print(php)

