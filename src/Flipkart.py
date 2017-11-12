'''
Created on Nov 8, 2017

@author: pshastri
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("http://flipkart.com")
# time.sleep(5)
# driver.find_element_by_css_selector("._2AkmmA _29YdH8").click()
print "Done"