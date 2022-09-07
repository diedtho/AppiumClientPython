import time
import pandas as pd

from appium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup

from powerpoint_elements import attrs2button
from operator import attrgetter

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

# Buttons
buttons = []

for i in range(len(elements)):
    tagname = elements[i].tag_name
    if str(tagname) in 'ControlType.Button':
        button = attrs2button(elements[i], i, "unnamed")
        buttons.append(button)


pprint(buttons)

print("\nÖffnen-Buttons")
text_getter = attrgetter('text')
#oldest = max(buttons, key=text_getter)
#print(f"Oldest: {oldest}")
oeffnen = [button for button in buttons if button.text == 'Öffnen']
pprint(oeffnen)

oeffnen[0].webelement.click()

driver.close()