from bs4 import BeautifulSoup
from selenium import webdriver
import time
import html5lib
import re
from urllib import request
import urllib
import os


'''
https://www.instagram.com/explore/tags/cat/
'''



def cleanTheFolder():
    current_path = os.path.realpath(__file__)
    real_path = os.path.split(current_path)[0] + "\\instagram\\"
    for root, dirs, files in os.walk(real_path):
        for name in files:
            os.remove(os.path.join(real_path, name))




opener = urllib.request.build_opener(urllib.request.HTTPSHandler)
header =("User-Agent", " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
opener.addheaders = [header]



url = "https://www.instagram.com/explore/tags/cat/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:
    driver.find_element_by_xpath("//a[contains(text(),'更多')]").click()
except:
    pass

def scrollPage(times):
 for i in range(times):
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(5)

scrollPage(5)

page = driver.page_source
soup = BeautifulSoup(page, "html5lib")
cleanTheFolder()
imgs = soup.find_all('img', {'sizes':'293px'})
index = 0
for item in imgs:
    img = str(item)
    link = re.search(r'https.*?\.jpg', img.strip())[0]

    fileName = 'instagram/' + str(index) +".jpg"
    index += 1
    #此处可以用多线程来写
    with open(fileName, 'wb') as file:
        img = opener.open(link).read()
        file.write(img)










