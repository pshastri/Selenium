'''
Created on Nov 3, 2017

@author: pshastri
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

# executable_path="C:\Users\pshastri\Desktop\googExercise\geckodriver.exe"
browser=webdriver.Chrome()
# print "wait start"
# browser.implicitly_wait(30)
# print "wait done"
browser.get("http://www.phonecurry.com/")
# browser.implicitly_wait(300)
browser.maximize_window()
findPhone=browser.find_element_by_name("q")
findPhone.send_keys("Oneplus")
findPhone.submit()
elm=browser.find_element_by_tag_name("html")
elm.send_keys(Keys.END)
browser.find_element_by_xpath(".//*[@id='page-content-wrapper']/div[3]/div[2]/div/div/div/p/a").click()
time.sleep(5)
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)
# mobiles=elm.find_elements_by_css_selector(".list-wrapper")
# print mobiles
print len(elm.find_elements_by_css_selector(".list-wrapper"))
print elm.find_elements_by_css_selector("#item3")
# phonePrice=browser.find_element_by_xpath("//*[@id='item1']/div[3]/p[1]").text
# print phonePrice


# browser.close()
print "Done"
