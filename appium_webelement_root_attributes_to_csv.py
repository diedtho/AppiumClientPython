import time
import pandas as pd

from appium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup

desired_caps = {}
desired_caps["app"] = "Root"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

session = driver.find_element_by_name('Präsentation1 - PowerPoint')
#session = driver.find_element_by_name('Hirsch, Patrick (Gast) | Microsoft Teams')
#buttons = driver.find_elements_by_custom()
elements = session.find_elements_by_xpath('/descendant-or-self::*')
#elements = session.find_element_by_xpath('/parent')
pprint(elements)
print('='*222)



element_attributes = []

for i in range(len(elements)):
    #print(f"Element Nr. {i} Tag-Name: {elements[i].tag_name}\tId: {elements[i].id}\tName: {elements[i].text}")
    tagname = elements[i].tag_name
    elemid = elements[i].id
    elemtext = elements[i].text
    element_attributes.append([tagname, elemid, elemtext])

for ele_attr in element_attributes:
    print(ele_attr)

df = pd.DataFrame(element_attributes, columns=['Tagname', 'Id', 'Text'])
print(df)

df.to_csv('app_attributes.csv', sep=';', encoding='utf-8')

# Buttons
buttons = []
for ele in element_attributes:
    print(ele[0])
    if str(ele[0]) in 'ControlType.Button':
        buttons.append(ele)

print("\nButtons:")
pprint(buttons)

driver.close()