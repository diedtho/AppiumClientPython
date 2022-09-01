from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import By

desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
desired_caps["platformName"] = "Windows"
desired_caps["deviceName"] = "WindowsPC"
driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
#el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'SomeAccessibilityID')
caps = driver.capabilities
print(caps)
element = driver.find_elements(By.NAME, 'Rechner')
print(element)

if type(element) is dict:
    for ele_key, ele_value in element:
        print(ele_key, ele_value)
    #first_element = list(element.values())[0]
    #element = driver.create_web_element(element_id=first_element)

if type(element) is list:
    for ele in element:
        print(element)
    #first_element = list(element.values())[0]
    #element = driver.create_web_element(element_id=first_element)

driver.close()
