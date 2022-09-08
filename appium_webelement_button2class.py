import time
import pandas as pd

from appium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup

from powerpoint_elements import attrs2buttons, attrs2tab_items, attrs2menu_items
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

for elem in elements:
    print(elem.tag_name, elem.text)

# Buttons
buttons = []
menu_items = []
tab_items = []

for i in range(len(elements)):
    tagname = elements[i].tag_name
    if str(tagname) in 'ControlType.Button':
        button = attrs2buttons(elements[i], i, "unnamed")
        buttons.append(button)
    if str(tagname) in 'ControlType.TabItem':
        tab_item = attrs2tab_items(elements[i], i, "unnamed")
        tab_items.append(tab_item)
    if str(tagname) in 'ControlType.MenuItem':
        menu_item = attrs2menu_items(elements[i], i, "unnamed")
        menu_items.append(menu_item)

pprint(buttons)
pprint(tab_items)
pprint(menu_items)

print("\nÖffnen-Buttons")
text_getter = attrgetter('text')
#oldest = max(buttons, key=text_getter)
#print(f"Oldest: {oldest}")
start = [tab_item for tab_item in tab_items if tab_item.text == 'Start']
pprint(start)

start[0].webelement.click()
start[0].webelement.click()

datei = [button for button in buttons if button.text == 'Registerkarte "Datei"']
datei[0].click()
datei[0].click()


driver.close()