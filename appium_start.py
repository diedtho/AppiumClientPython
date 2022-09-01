from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub')
caps = driver.get()
print(caps)

driver.close()
