import requests
from bs4 import BeautifulSoup as bs
class Data:
    def getData():  
        url = "https://www.worldometers.info/coronavirus/"
        r  = requests.get(url)
        htmlcontent = r.content
        soup = bs(htmlcontent,  "html.parser")

        country = soup.find_all("a", class_ = "mt_a")[:215]
        names = ["sno", 'Country', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases', 'Serious', 'TotCases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/1M pop']
        tbody = soup.find_all("tbody")[0]
        countryInfo = [a.string if a.string is not None else "" for i in tbody.find_all("tr")[8:] for a in i.find_all("td")[:14] ]
        covidInfo = {x: {y:z for y, z in zip(names, countryInfo[ind*len(names):])} for ind, x in enumerate([i.string for i in country])}
        return covidInfo

        
