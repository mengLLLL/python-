from urllib import request
from bs4 import BeautifulSoup
import re

url='http://www.imooc.com/'
response = request.urlopen(url)
html = response.read()
#html要解码才可以 
html = html.decode('utf-8')
listurl = re.findall(r'http:.+\.jpg',html)
#将图片保存到本地
i = 0
for url in listurl[30:]:
	f=open(str(i)+'.jpg','wb')
	#i=open如果文件不存在，是会创建文件的
	req = request.urlopen(url)
	buf = req.read()
	# print (buf)
	f.write(buf)
	f.close()
	i=i+1