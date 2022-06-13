from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver_path = "./geckodriver_0_31/geckodriver"
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('http://192.168.0.1')
driver.maximize_window()
timeout = 9
elementInputPass = 'span.password-wrap>input:first-child'
scriptLogIn = '$("a[title=\'LOG IN\']")[0].click()'
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, elementInputPass))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

driver.find_element_by_css_selector(elementInputPass).send_keys("alisuruh77")
driver.execute_script(scriptLogIn)
sleep(1)
driver.get('http://192.168.0.1/#wirelessBasic')
'''
elementWireless = "#main-menu li.navigator-li[navi-value='wirelessBasic']>a"
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, elementWireless))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

driver.find_element_by_css_selector(elementWireless).click()
'''



labelGuest = 'label[for^="guest-network"]'
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, labelGuest))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
driver.find_element_by_css_selector(labelGuest).click()
