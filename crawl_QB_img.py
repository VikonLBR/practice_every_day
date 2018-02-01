import urllib
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver


def cleanTheFolder():
    current_path = os.path.realpath(__file__)
    real_path = os.path.split(current_path)[0] + "\\QB\\"
    for root, dirs, files in os.walk(real_path):
        for name in files:
            os.remove(os.path.join(real_path, name))


opener = urllib.request.build_opener(urllib.request.HTTPSHandler)
header =("User-Agent", " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
opener.addheaders = [header]
cleanTheFolder()
for i in range(10):
    url = "https://www.qiushibaike.com/8hr/page/"+str(i)+"/"
    response = opener.open(url)

    soup = BeautifulSoup(response, 'html5lib')
    imgList = soup.find_all('div', {'class': 'thumb'})
    index = 0
    for img in imgList:
        img = str(img.a.img)
        img_address = re.sub(r'.*src=\"(.*?)\".*', '\\1', img.strip())
        link = "http:" + img_address
        fileName = 'QB/' + str(i) + "_" + str(index) + ".jpg"
        index += 1
        with open(fileName, 'wb') as file:
            img = opener.open(link).read()
            file.write(img)














