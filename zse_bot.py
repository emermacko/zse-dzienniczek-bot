'''
    !! Bot sam nie wyjdzie z wiadomosci ktora zawiera link !!

    Wybór folderu wiadomości - 24 linijka - domyślnie odebrane z bieżącego dnia 
    Interfejs - 27 linijka - Domyślnie brak (headless)
'''

from selenium import webdriver
from getpass import getpass
from datetime import datetime

import os
import time
import platform

clear = 'clear'

wiadomosci = [
    'odebranRoot',          # Wszystkie wiadomosci
    'odebraneDzisiaj',      # Wiadomosci z dzisiaj
    'odebraneTenTydzien'    # Wiadomosci z calego tygodnia
]

folder = wiadomosci[1]  # <----- Wybor folderu wiadomosci do odczytu

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # <----- Tryb bez UI
options.add_argument('--log-level=3')  # Wymagane dla czytelności jeżeli jest --headless

def stronaLogowania():
    while(True):
        os.system(clear)
        driver.get('https://cufs.vulcan.net.pl/bydgoszcz/Account/LogOn?ReturnUrl=%2Fbydgoszcz%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx')

        time.sleep(1)
        if not ifExistsCSS('input[type="submit"]'):
            checkForErrors()
            print('[ERROR] Błąd strony logowania')
            time.sleep(5)
        else:
            break

    logowanie()

def logowanie():
    time.sleep(1)
    print('[OK] Logowanie')

    getElementByCSS('#LoginName').send_keys(usr)
    time.sleep(0.5)

    getElementByCSS('#Password').send_keys(pwd)
    time.sleep(0.5)

    login_button = getElementByCSS('.center input')
    try:
        driver.set_page_load_timeout(10)
        login_button.submit()
    except:
        stronaLogowania()

    time.sleep(1)
    while not ifExistsCSS('.panel'):
        checkForErrors()
        time.sleep(3)

    print('[OK] Ładowanie wiadomości')
    while(True):
        try:
            driver.get('https://uonetplus-uzytkownik.vulcan.net.pl/bydgoszcz/')
            break
        except:
            checkForErrors()
            time.sleep(1)

    time.sleep(1)
    petla()

def petla():
    while(True):
        while(True):
            try:
                # x = getElementByXPATH("//*[contains(@id, 'loadmask')]")
                getElementByXPATH(f'//*[contains(@id, {folder})]').click()
                break
            except:
                checkForErrors()
                os.system(clear)
                print('[OK] Ładowanie . . .')
                time.sleep(3)

        try:
            os.system(clear)
            currTime = datetime.now().strftime("%H:%M:%S")
            print(f'\n\nWiadomości: [ostatnie odświeżenie: {currTime}]\n')

            time.sleep(2)

            mails = driver.find_elements_by_xpath('//*[contains(@data-boundview, "gridview-")]')
            topics = getElementsByCSS('.x-grid-cell-inner')

            i=1
            for mail in mails:
                checkForErrors()
                print(f'{topics[i].text} ## {topics[i+1].text}')
                time.sleep(0.5)
                mail.click()
                i=i+5
                while(True):
                    try:
                        getElementByXPATH(f'//*[contains(@id, {folder})]').click()
                        break
                    except:
                        time.sleep(2)

            time.sleep(300)
            getElementByCSS('#wiadomosci').click()

        except:
            print('[ERROR] Błąd serwerów // ponowne próbowanie')
            checkForErrors()

def checkForErrors():
    while(True):
        try:
            if not ifExistsXPATH('//*[contains(@id, "ribbon-logout-btn")]'):
                stronaLogowania()

            xx = getElementsByCSS('.x-component')
            for x in xx:
                if(x.text == "Brak komunikacji z serwerem."):
                    stronaLogowania()

            x = getElementByCSS('.loginButton')
            stronaLogowania()

            x = getElementByCSS('.neterror')
            stronaLogowania()
        except:
            break

####

def getElementByCSS(selector):
    return driver.find_element_by_css_selector(selector)

def getElementsByCSS(selector):
    return driver.find_elements_by_css_selector(selector)

def getElementByXPATH(selector):
    return driver.find_element_by_xpath(selector)

def ifExistsXPATH(selector):
    try:
        getElementByXPATH(selector)
        return True
    except:
        return False

def ifExistsCSS(selector):
    try:
        getElementByCSS(selector)
        return True
    except:
        return False

###

OS = platform.system()
if OS == 'Windows':
    clear = 'cls'

os.system(clear)
usr = '' # <----- EMAIL
pwd = getpass('> Haslo: ')

driver = webdriver.Chrome(options=options)
stronaLogowania()
