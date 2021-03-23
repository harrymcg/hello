msg = "test print function"
print(msg)

from bs4 import BeautifulSoup
import requests

msg = "line 7 print test"
print(msg)

>>>>for num in range(0,20):
>>>>url = str(‘www.realestate.com.au/sold/in-olivers+hill,+vic+3199%3b/list-‘+str(num))
>>>>r = requests.get(“http://” +url)

msg = "line 14 print test"
print(msg)

>>>>data = r.text
>>>>soup = BeautifulSoup(data)
>>>>mydivs = soup.findAll(“span”, {“class”: “property-price”})
>>>>for line in mydivs:
>>>>>>>>print(line.text)
