from urllib.request import Request,urlopen
# from urllib import request 这样是不行的
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
postData = parse.urlencode([
	("StartStation", "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"),
	("EndStation", "e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"),
	("SearchDate", "2016/09/07"),
	("SearchTime", "20:30"),
	("SearchWay", "DepartureInMandarin")
	])
req.add_header("Origin","http://www.thsrc.com.tw")
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")
response = urlopen(req,data=postData.encode('utf-8'))
print(response.read().decode('utf-8'))