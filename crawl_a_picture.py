from bs4 import BeautifulSoup
from urllib import request
import re
import os

url = 'https://en.wikipedia.org/wiki/Hong_Kong'
root_url = 'https://en.wikipedia.org'
page = request.urlopen(url)
soup = BeautifulSoup(page, 'html5lib')
flag_src = soup.find('img', {'alt': 'Flag of Hong Kong'})
flag_src = str(flag_src)
# then find the link
link = re.sub(r'.*\ssrc=\"(.*?)\"\s.*', '\\1', flag_src.strip())
new_url = "http:"+link
with open('hong_kong_flag.png', 'wb') as file:
    img_source = request.urlopen(new_url).read()
    file.write(img_source)


