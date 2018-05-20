from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0



def searchSeats(username,password,coursecode):
    username = raw_input("Enter GatorLink Username:\t")
    password  = raw_input("Enter GatorLink Password:\t")
    courseCode = "CEN4722"

    driver = webdriver.Chrome()
    driver.get("http://one.uf.edu/login/")

    ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body layout-row']/div[@class='layout-column flex']/md-content[@id='main']/root[@id='root']/div[@class='root-view ng-scope']/uf-login[@class='ng-scope ng-isolate-scope']/div[@id='ufLogin']/md-card[@class='md-whiteframe-2dp layout-padding _md']/md-list[@class='layout-align-center-center layout-column']/md-list-item[@class='login-item md-no-proxy _md md-clickable'][1]/button[@class='md-primary md-raised md-ink-ripple login-button md-button']")
    ele.click()
    driver.implicitly_wait(5)
    # ele = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.TAG_NAME, "md-menu-item"))
    # )
    # ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body ng-scope layout-row']/div[@id='menu_container_0']/md-menu-content/md-menu-item[1]/button[@class='md-button md-ink-ripple']")

    # ele.click()
    # driver.implicitly_wait(0)
    ele = driver.find_element_by_id("username")
    # ele.clear()
    ele.send_keys(username)
    ele = driver.find_element_by_id("password")
    # ele.clear()
    ele.send_keys(password)
    ele = driver.find_element_by_id("submit")
    ele.click()

    ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body layout-row']/div[@class='layout-column flex']/md-content[@id='main']/root[@id='root']/div[@class='ng-scope']/uf-tab[@class='ng-scope ng-isolate-scope']/md-tabs[@id='ufTab']/md-tabs-content-wrapper[@class='_md']/md-tab-content[@id='tab-content-4']/div[@class='ng-scope ng-isolate-scope']/div[@class='ng-scope']/uf-panel[@class='ng-isolate-scope']/div[@id='ufPanel']/md-grid-list[@class='ng-scope ng-isolate-scope _md']/md-grid-tile[@class='ng-scope ng-isolate-scope'][2]/figure/uf-card[@class='uf-card card-wrapper ng-scope ng-isolate-scope']/div[@class='card-wrapper']/div[@class='card-wrapper ng-scope']/myschedule-card[@class='ng-scope ng-isolate-scope']/div[@id='myscheduleCard']/md-card[@class='_md']/md-card-actions[@class='layout-align-start-center layout-row']/a[@class='md-raised md-primary md-button md-ink-ripple']")

    ele.click()

    ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body ng-scope layout-row']/div[@class='layout-column flex']/md-content[@id='main']/div[@class='ng-scope flex-noshrink']/div[@id='termContainer']/md-card[@class='uf-card ng-scope _md flex-xs-100 flex-sm-45 flex-gt-sm-30'][2]/md-card-action[@class='layout-align-start-end layout-row']/a[@class='md-raised md-primary md-button ng-scope md-ink-ripple']")

    ele.click()

    ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body ng-scope layout-row']/div[@class='layout-column flex']/md-content[@id='main']/div[@class='ng-scope flex-noshrink']/section[@class='schedule-box-md-container ng-scope flex']/div[@id='scheduleBox']/div[@class='schedule-block']/div[@class='schedule-title hide-in-print-view ng-scope']/a[@class='add-course ng-scope']")

    ele.click()

    ele = driver.find_element_by_xpath("/html[@class='ng-scope']/body[@class='uf-body ng-scope layout-row registration']/div[@class='layout-column flex']/md-content[@id='main']/div[@class='ng-scope flex-noshrink']/section[@class='search-layout ng-scope flex-none']/md-content[@class='center-content _md layout-row flex reg-content']/div[@id='ufSOC']/uf-semesters/div[@id='subHeader']/button[@class='md-button md-ink-ripple']")
    ele.click()

    ele = Select(driver.find_element_by_id("progLevel"))
    ele.select_by_value("UGRD")

    ele = driver.find_element_by_id("courseCode")
    ele.send_keys(courseCode)

    ele = driver.find_element_by_class_name("filter-sidebar-search-button")
    ele.click()

    driver.implicitly_wait(10)

    ele = driver.find_element_by_class_name("course-code")
    ele.click()

    ele = driver.find_element_by_class_name("section-open-seats")

    seats = ele.text


    if seats == "Open Seats: 0":
        print "booty"
        #TODO set up email for failures
    else:
        #setup email for success
        ele = driver.find_element_by_class_name("section-add-section")
        ele.click()

        ele = driver.find_element_by_class_name("modal-confirm-button")
        ele.click()
        print "woohoo"
        print seats

    driver.close();
