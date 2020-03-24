from selenium import webdriver
from getpass import getpass
from datetime import datetime

import os
import time

usr = '## EMAIL ##' ## Email uzywany do logowania do dziennika

pwd = getpass('> Haslo: ')

driver = webdriver.Chrome('.\chromedriver.exe') ## lokalizacja webdrivera
os.system('cls')

print('> Uruchamianie dziennika')
driver.get('https://cufs.vulcan.net.pl/bydgoszcz/Account/LogOn?ReturnUrl=%2Fbydgoszcz%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx')

print('> Wpisywanie loginu')
username_box = driver.find_element_by_id('LoginName')
username_box.send_keys(usr)
time.sleep(0.5)

print('> Wpisywanie hasla')
password_box = driver.find_element_by_id('Password')
password_box.send_keys(pwd)
time.sleep(0.5)

print('> Logowanie')
login_button = driver.find_element_by_css_selector('.center input')
login_button.submit()

time.sleep(2)
print('> Uruchamianie wiadomości')
driver.get('https://uonetplus-uzytkownik.vulcan.net.pl/bydgoszcz/')
time.sleep(2)

## driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
## driver.find_element_by_xpath("//*[contains(@id, 'odebraneTenTydzien')]").click()

while(True):
    os.system('cls')
    currTime = datetime.now().strftime("%H:%M:%S")
    time.sleep(1)
    
    print('\n\n' + 'Wiadomości dzisiaj: [ostatnie odświeżenie: ' + currTime + ']\n')
    driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
    time.sleep(1)

    mails = driver.find_elements_by_xpath("//*[contains(@data-boundview, 'gridview-')]")
    topics = driver.find_elements_by_class_name('x-grid-cell-inner')
    
    i=1
    for mail in mails:
        print (topics[i].text + " ## " + topics[i+1].text)
        mail.click()
        i=i+5
        time.sleep(0.5)

    time.sleep(300)
    driver.find_element_by_id('wiadomosci').click()

