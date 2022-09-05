import time

from appium import webdriver
from pprint import pprint

desired_caps = {}
desired_caps["app"] = "Root"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

# Magic methods of webdriver
print("Magic methods of the webdriver:")
pprint(dir(driver))

# Magic methods of webdriver
print("Magic methods of an element (e.g. calculator):")
calculator = driver.find_element_by_name('Rechner')
print("Attributes and methods of an element (e.g. calculator) in detail:")
attribs_and_methods = dir(calculator)
for attr_or_method in attribs_and_methods:
    type_of_attr_or_method = type(getattr(calculator,attr_or_method))
    print(f"Attribut or method: {attr_or_method}\tis type: {type_of_attr_or_method}")



