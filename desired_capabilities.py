from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from shutil import which

#Desired Capabilities
DesiredCapabilities = {
    'platform': 'Windows',
    'browserName': 'Firefox',
    'browserName': 'Edge'
}

#Firefox
path_firefox = which("geckodriver")
driver_firefox = webdriver.Firefox(executable_path= path_firefox)

#Edge
path_edge = which("msedgedriver")
driver_edge = webdriver.Edge(executable_path= path_edge)

twitter = "https://www.twitter.com"
driver_edge.get(twitter)
driver_firefox.get(twitter)