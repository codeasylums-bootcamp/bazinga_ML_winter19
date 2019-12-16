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

table_id = driver.find_element_by_class_name('table')
rows = table_id.find_element_by_tag_name("tr") # get all of the rows in the table
print(str(rows))

url = "https://www.trainspnrstatus.com/pnrformcheck.php"
r= requests.get(url)
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

url = 'https://www.trainspnrstatus.com/pnrformcheck.php'
r = requests.get(url)
root = LH.fromstring(r.content)

for table in root.xpath('//table[@id="td"]'):
    header = [text(th) for th in table.xpath('//th')]        # 1
    data = [[text(td) for td in tr.xpath('td')]  
            for tr in table.xpath('//tr')]                   # 2
    data = [row for row in data if len(row)==len(header)]    # 3 
    data = pd.DataFrame(data, columns=header)                # 4
    print(data)

# driver.quit()
     
