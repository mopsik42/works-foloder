import requests
import bs4 as bs


url = 'https://www.banki.ru/products/currency/cash/eur/stavropol~skiy_kray/pyatigorsk/'
response = requests.get(url)
soup = bs.BeautifulSoup(response.text, 'html.parser')
price = soup.find_all('div', class_='Text__sc-vycpdy-0 cQqMIr')
organization = soup.find_all('div', class_='Text__sc-vycpdy-0 OiTuY')

for i in range(0, len(price), 2):
    print(organization[i//2].text.strip()+': Покупка:'+price[i].text.strip()+', Продажа:'+price[i+1].text.strip())



