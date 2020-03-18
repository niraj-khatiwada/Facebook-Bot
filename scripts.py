from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

path = which("geckodriver")

firefox_option = Options()
firefox_option.add_argument("--disable-notifications")

driver = webdriver.Firefox(executable_path= path,options= firefox_option )

driver.get("https://www.facebook.com")

driver.find_element_by_id("email").send_keys("heavenandhell368@gmail.com")

driver.find_element_by_id("pass").send_keys("_sn0r13xfk")

driver.find_element_by_id("loginbutton").click()


#Logout
driver.find_element_by_id("userNavigationLabel").click()
time.sleep(5)
driver.find_element_by_xpath("//ul[@class='_54nf']/li[position()=last()]").click()