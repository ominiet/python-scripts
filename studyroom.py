from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://ufl.evanced.info/dibs")

ele = driver.find_element_by_id("username")
ele.clear()
ele.send_keys("")
ele = driver.find_element_by_id("password")
ele.clear()
ele.send_keys("")
ele = driver.find_element_by_id("submit")
ele.click()