from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.trainspnrstatus.com/")

from selenium.webdriver.common.by import By

while s=input("Enter PNR"):
    element = driver.find_element_by_id('fullname').send_keys(s)
    element = driver.find_element_by_id('idbtn').click()


# element=driver.find_element_by_id('indiGoFlightSchedule.Origin')
# element.sendKeys("Ranchi")
# element = driver.find_element_by_name("autocomplete-wrapper station-wrapper")
# element = driver.find_element_by_name("indiGoFlightSchedule.Origin")
# element.send_keys("some text")