import time

from appium import webdriver
from pprint import pprint

desired_caps = {}
desired_caps["app"] = "Root"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

calculator_session = driver.find_element_by_name('Rechner')
elements = calculator_session.find_elements_by_xpath('/*/*/*')
pprint(elements)

for i in range(len(elements)):
    print(f"Element Nr. {i} Tag-Name: {elements[0].tag_name}")
    time.sleep(3)

driver.close()
