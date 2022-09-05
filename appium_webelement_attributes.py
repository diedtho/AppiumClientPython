import time

from appium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup

desired_caps = {}
desired_caps["app"] = "Root"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

calculator_session = driver.find_element_by_name('Rechner')
#elements = calculator_session.find_elements_by_xpath('/*/*/*/*/*/*')
# https://discuss.appium.io/t/many-findelement-in-a-row-with-xpath/9728/2
elements = calculator_session.find_elements_by_xpath('/descendant-or-self::*')
pprint(elements)

element_attributes = ['class', 'name', 'text', 'type']

for i in range(len(elements)):
    print(f"Element Nr. {i} Tag-Name: {elements[i].tag_name}\tId: {elements[i].id}\tName: {elements[i].text}")
    is_displayed = elements[i].is_displayed()
    print(f"Element is displayed: {is_displayed}")
    print(f"Attributes of element {i}")
    for ele_attr in element_attributes:
        print(f"Attribute {ele_attr}:\t{elements[i].get_attribute(ele_attr)}")
    # All attributes of the element - https://stackoverflow.com/questions/27307131/selenium-webdriver-how-do-i-find-all-of-an-elements-attributes
    outer_html = elements[i].get_attribute('outerHTML')
    if outer_html != None:
        attrs = BeautifulSoup(outer_html, 'html.parser').a.attrsprint(f"Attributes: {attrs}")
        print(attrs)
    time.sleep(3)

driver.close()