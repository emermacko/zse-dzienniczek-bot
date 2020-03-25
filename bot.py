from selenium import webdriver
from getpass import getpass
from datetime import datetime
import os
import time

usr = 'mr.macko.yt@gmail.com'
pwd = getpass('> Haslo: ')
driver = webdriver.Chrome('.\chromedriver.exe')

def stronaLogowania():
    while(True):
        os.system('cls')
        print('> Uruchamianie dziennika')
        driver.get('https://cufs.vulcan.net.pl/bydgoszcz/Account/LogOn?ReturnUrl=%2Fbydgoszcz%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx')
        try:
            x = driver.find_element_by_xpath("//input[@type='submit']")
            logowanie()
        except:
            print('Błąd strony logowania')
            time.sleep(5)
            pass


def logowanie():
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

    print('> Ładowanie strony glownej')
    while(True):
        try:
            x = driver.find_element_by_class_name('panel')
            if(x.size() != 0): break
        except:
            print('Logowanie :: Wczytywanie strony głównej')
            time.sleep(5)
            pass

    print('> Ładowanie wiadomości')
    driver.get('https://uonetplus-uzytkownik.vulcan.net.pl/bydgoszcz/')
    petla()

'''
time.sleep(5)
            if driver.find_element_by_class_name('loginButton').size()>0 or driver.find_element_by_class_name('neterror'):
                stronaLogowania()
'''


def petla():

    while(True):

        while(driver.find_element_by_xpath("//*[contains(@id, 'loadmask')]").size()>0):
            os.system('cls')
            print('Ładowanie . . .')
            time.sleep(5)

        try:
            os.system('cls')
            currTime = datetime.now().strftime("%H:%M:%S")
            print('\n\n' + 'Wiadomości dzisiaj: [ostatnie odświeżenie: ' + currTime + ']\n')
            driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()

            while(driver.find_element_by_xpath("//*[contains(@id, 'loadmask')]").size()>0):
            os.system('cls')
            print('Ładowanie . . .')
            time.sleep(5)

            time.sleep(10)

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
        except:
            print('Pętla :: Błąd serwerów czy chuj wie co // ponowne próbowanie')
            pass


###
stronaLogowania()
###


#driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
#driver.find_element_by_xpath("//*[contains(@id, 'odebraneTenTydzien')]").click()
