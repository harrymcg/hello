from bs4 import BeautifulSoup

import requests

# Define a 'property record' class
class PropertyRecord:
    def __init__(self, pricing, address, features, propertyType, saleData):
        self.pricing = pricing
        self.address = address
        self.features = features
        self.propertyType = propertyType
        self.saleData = saleData

def has_class_but_no_id(tag):
    return tag.has_attr('class') and tag.has_attr('data-testid')

# Create list to hold all the properties
allProperties = []

for num in range(1, 20):
    # url = str(
    #     'www.domain.com.au/sold-listings/randwick-nsw-2031/?excludepricewithheld=1&page='+str(num))
    url = str(
        'www.domain.com.au/sold-listings/kingsford-nsw-2032/?excludepricewithheld=1&page='+str(num))
    r = requests.get("https://" + url, headers={'User-Agent': 'Mozilla/5.0'})
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    # Get list of Listings
    results = soup.find('ul', attrs={"data-testid": "results"})
    pageListings = results.find_all('li', attrs={"data-testid": True})

    for listing in pageListings:
        price = listing.find('p', attrs={"data-testid": "listing-card-price"})
        address = listing.find('span', attrs={"data-testid": "address-line1"})
        features = listing.find('div', attrs={"data-testid": "property-features"})
        propertyType = listing.find('span', attrs={"class": "css-693528"})
        saleData = listing.find('span', attrs={"class": "css-1nj9ymt"})

        currentRecord = PropertyRecord(getattr(price, "text", 'N/A'), getattr(address, "text", 'N/A'), getattr(
            features, "text", 'N/A'), getattr(propertyType, "text", 'N/A'), getattr(saleData, "text", 'N/A'))

        allProperties.append(currentRecord)

print('Total records found: ' + str(len(allProperties)))

for scrapedProperty in allProperties:
    #print('------------------------')
   print(scrapedProperty.address + '; ' + scrapedProperty.pricing + '; ' + scrapedProperty.features + '; ' + scrapedProperty.propertyType + '; ' + scrapedProperty.saleData + ';')
    #print('   ' + scrapedProperty.address)
    #print('   ' + scrapedProperty.pricing)
    #print('   ' + scrapedProperty.features)
    #print('   ' + scrapedProperty.propertyType)
    #print('   ' + scrapedProperty.saleData)