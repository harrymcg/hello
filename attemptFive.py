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


# Create list to hold all the properties
allProperties = []

for num in range(1, 2):
    url = str(
        'www.domain.com.au/sold-listings/erskineville-nsw-2043/?excludepricewithheld=1&page='+str(num))
    r = requests.get("https://" + url, headers={'User-Agent': 'Mozilla/5.0'})
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    # Get lists with each property from the page
    pricesList = soup.select('p[data-testid="listing-card-price"]')
    addressList = soup.select('span[data-testid="address-line1"]')
    featuresList = soup.select('div[data-testid="property-features"]')
    propertyTypeList = soup.findAll('span', {"class": ["css-693528"]})
    saleDataList = soup.findAll('span', {"class": ["css-1nj9ymt"]})

    # Loop the x items in the lists and add a new 'PropertyRecord' class/object for each one
    for listIndex in range(0, len(pricesList)):
        currentRecord = PropertyRecord(pricesList[listIndex].text, addressList[listIndex].text,
                                       featuresList[listIndex].text, propertyTypeList[listIndex].text, saleDataList[listIndex].text)
        allProperties.append(currentRecord)

print('Total records found: ' + str(len(allProperties)))

for scrapedProperty in allProperties:
    print('------------------------')
    print('   ' + scrapedProperty.address)
    print('   ' + scrapedProperty.pricing)
    print('   ' + scrapedProperty.features)
    print('   ' + scrapedProperty.propertyType)
    print('   ' + scrapedProperty.saleData)
