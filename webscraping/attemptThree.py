from bs4 import BeautifulSoup
import requests
for num in range(1,8):
    url = str('www.domain.com.au/sold-listings/erskineville-nsw-2043/?excludepricewithheld=1&page='+str(num))
    r = requests.get("https://" +url, headers={'User-Agent': 'Mozilla/5.0' })
    data = r.text
    #print(data)
    soup = BeautifulSoup(data, 'html.parser')
    #print(soup)
    myVariable = soup.findAll('p')
    #print(myVariable, "____ NEW MYVARIABLE" , num)
    for line in myVariable:
        #print("___hello world 1____")
        print(line.text)
        print(num)
        #print("____Hello world 2____")