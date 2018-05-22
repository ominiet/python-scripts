from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass

#TODO: get all info necessary for script to run
#TODO: make a file to hold data for whole semester
#TODO: Maybe create GUI

username = raw_input("Enter your gatorlink username:\t")
password = raw_input("Enter your gatorlink password:\t")
# password = getpass.getpass("Enter your gatorlink password:\t")

driver = webdriver.Chrome()
driver.get("http://ufl.evanced.info/dibs")

# set driver then move to script

ele = driver.find_element_by_id("username")
ele.clear()
ele.send_keys(username)
ele = driver.find_element_by_id("password")
ele.clear()
ele.send_keys(password)
ele = driver.find_element_by_id("submit")
ele.click()


size = Select(driver.find_element_by_id('SelectedRoomSize'))
size.select_by_value("2,6")
time = Select(driver.find_element_by_id('SelectedTimeSort'))
time.select_by_value("Afternoon")
ele = driver.find_element_by_class_name("btn-block")

ele.click()


ele = driver.find_element_by_class_name("item-link")
ele.click()

ele = driver.find_element_by_class_name("item-link")
ele.click()

ele = driver.find_element_by_class_name("item-link")
ele.click()

ele = driver.find_element_by_id("Phone")
ele.clear()
ele.send_keys("3057990049")

ele = driver.find_element_by_id("btnCallDibs")
# ele.click()




