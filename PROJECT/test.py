from bs4 import BeautifulSoup
import requests

url = 'https://www.gofundme.com/f/the-adeline-movement'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

value = soup.find('div', class_ = "hrt-disp-inline")

donation_value = [x.text.strip() for x in value]

print(donation_value)