'''
Created on Nov 9, 2017

@author: pshastri
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.get("https://www.netiq.com/")
driver.maximize_window()

support= driver.find_element_by_xpath("//*[@id='nav_service']")
ActionChains(driver).move_to_element(support).perform()

wait = WebDriverWait(driver, 20)
docButton= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='hdr_support_documentation']")))