from selenium import webdriver
from time import sleep
#import os

#options = webdriver.ChromeOptions()
#options.binary_location = '/usr/bin/brave'
#driver_path = os.path.join(os.getcwd(), "/program-wifi/chromedriver")
#driver_path = "/home/cakdeny49/Downloads/MSIB/chromedriver_93/chromedriver"
#browser = webdriver.Chrome(chrome_options = options, executable_path = driver_path)

driver_path = "/home/cakdeny49/Downloads/MSIB/geckodriver_0_31/geckodriver"
browser = webdriver.Firefox(executable_path=driver_path)
browser.maximize_window()
browser.get('http://192.168.0.1')

#script = '$("span.password-wrap>input:first-child()")[0].value="alisuruh77"'
scriptLogIn = '$("a[title=\'LOG IN\']")[0].click()'
password = 'alisuruh77'
elementInputPass = 'span.password-wrap>input:first-child'

sleep(9)
browser.find_element_by_css_selector(elementInputPass).send_keys(password)
sleep(2)
browser.execute_script(scriptLogIn)
sleep(3)


wireless = "#main-menu li.navigator-li[navi-value='wirelessBasic']>a"
browser.find_element_by_css_selector(wireless).click()
sleep(1)
scriptLogOut = '$("a[title=\'Log Out\']")[0].click()'
browser.execute_script(scriptLogOut)
sleep(.5)
scriptClickYes = '$("a[title=\'YES\']")[0].click()'
browser.execute_script(scriptClickYes)




'''
print(script)
print(script2)
time.sleep(7)
browser.execute_script(script)
browser.execute_script(script2)
'''
