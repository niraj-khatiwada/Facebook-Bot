from selenium import webdriver
from shutil import which
from selenium.webdriver.common.action_chains import ActionChains
import time

path = which("geckodriver")
driver = webdriver.Firefox(executable_path= path)


driver.get("https://jqueryui.com/droppable/")
time.sleep(3)
driver.switch_to_frame(driver.find_element_by_class_name("demo-frame"))
source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")
ActionChains(driver).drag_and_drop(source, target).perform()