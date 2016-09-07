from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
response = urlopen("https://en.wikipedia.org/wiki/Wiki").read().decode('utf-8')
soup = BeautifulSoup(response,"html.parser")
urls = soup.find_all("a",href=re.compile("^/wiki/"))
for url in urls:
	if not re.search("\.(jpg|JPG)$",url["href"]):
		print(url.get_text(),"<---->","https://en.wikipedia.org" + url["href"])