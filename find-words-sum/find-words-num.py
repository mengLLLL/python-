from collections import Counter
import re
f = open('test.txt','r+')
content = f.read()
content = content.split(r' ')
print (Counter(content).most_common())
