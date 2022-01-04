import requests
from bs4 import BeautifulSoup

url = "https://www.boursorama.com/bourse/devises/taux-de-change/"
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
resultsEUR=soup.find_all('a',attrs={'title':"Taux de change EUR-MAD"})
resultsUSD=soup.find_all('a',attrs={'title':"Taux de change USD-MAD"})
resultsCHF=soup.find_all('a',attrs={'title':"Taux de change CHF-MAD"})
resultsCNY=soup.find_all('a',attrs={'title':"Taux de change CNY-MAD"})
print("1 EUR = " + resultsEUR[0].text + "MAD")
print("1 USD = " + resultsUSD[0].text + "MAD")
print("1 CHF = " + resultsCHF[0].text + "MAD")
print("1 CNY = " + resultsCNY[0].text + "MAD")