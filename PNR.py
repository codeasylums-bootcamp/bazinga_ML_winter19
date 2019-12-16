from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests


s=input("Pnr No??: ")
driver = webdriver.Chrome()
driver.get("https://www.trainspnrstatus.com/")

from selenium.webdriver.common.by import By

#s='4613209408'

element = driver.find_element_by_id('fullname').send_keys(s)
element = driver.find_element_by_id('idbtn').click()

# import requests
# import urllib.request
# from bs4 import BeautifulSoup

# url = "https://www.trainspnrstatus.com/pnrformcheck.php"
# r = requests.get(url)
# l = []
# html_content = r.text
# soup = BeautifulSoup(html_content,"html.parser")
# link = soup.find("table",{"class":"wikitable"})
# z=link.find_all("tr")
# for i in z:
#     print(i)
#     print("------------------------")
#     l.append(i)
    #each row is in l

# driver.quit()
