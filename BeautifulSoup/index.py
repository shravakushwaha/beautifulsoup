import bs4
from bs4 import BeautifulStoneSoup
import requests

url=requests.get('https://gstserver.com/tools/distance-between-pin-codes/')
soap=bs4.BeautifulSoup(url.text, 'html.parser')
print(soap.get_text())