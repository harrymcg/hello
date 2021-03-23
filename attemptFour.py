from bs4 import BeautifulSoup
import requests
for num in range(1,20):
    url = str('www.domain.com.au/sold-listings/erskineville-nsw-2043/?excludepricewithheld=1&page='+str(num))
    r = requests.get("https://" +url, headers={'User-Agent': 'Mozilla/5.0' })
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    #old query!    #myVariable = soup.findAll('p', {"class":["css-mgq8y"]})
    #pricing    
    #myVariable = soup.select('p[data-testid="listing-card-price"]')
    #address:
    #myVariable = soup.select('span[data-testid="address-line1"]')
    #features
    #myVariable = soup.select('div[data-testid="property-features"]')
    #property type
    #myVariable = soup.findAll('span', {"class":["css-693528"]})
    #sale date
    myVariable = soup.findAll('span', {"class":["css-1nj9ymt"]})
    for line in myVariable:
            print(line.text)
    