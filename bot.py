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
        try:
            driver.get('https://cufs.vulcan.net.pl/bydgoszcz/Account/LogOn?ReturnUrl=%2Fbydgoszcz%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fbydgoszcz%252fLoginEndpoint.aspx')
        except:
            stronaLogowania()
        try:
            x = driver.find_element_by_xpath("//input[@type='submit']")
            break
        except:
            while(True):
                try:
                    x = driver.find_element_by_class_name('neterror')
                    stronaLogowania()
                except:
                    break
            print('Błąd strony logowania')
            time.sleep(5)
            pass
    logowanie()

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
    print('> Ładowanie strony glownej')
    login_button.submit()

    time.sleep(1)
    while(True):
        try:
            x = driver.find_element_by_class_name('panel')
            break
        except:
            time.sleep(3)
            pass

    print('> Ładowanie wiadomości')
    while(True):
        try:
            driver.get('https://uonetplus-uzytkownik.vulcan.net.pl/bydgoszcz/')
            break
        except:
            time.sleep(1)

    time.sleep(1)
    petla()

def petla():

    while(True):
        while(True):
            try:
                # x = driver.find_element_by_xpath("//*[contains(@id, 'loadmask')]")
                driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
                break
            except:
                os.system('cls')
                print('Ładowanie . . .')
                time.sleep(3)

        try:
            os.system('cls')

            while(True):
                try:
                    # x = driver.find_element_by_xpath("//*[contains(@id, 'loadmask')]")
                    driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()

                    os.system('cls')
                    currTime = datetime.now().strftime("%H:%M:%S")
                    print('\n\n' + 'Wiadomości dzisiaj: [ostatnie odświeżenie: ' + currTime + ']\n')
                    break
                except:
                    os.system('cls')
                    print('Ładowanie . . .')
                    time.sleep(3)

            time.sleep(2)

            mails = driver.find_elements_by_xpath("//*[contains(@data-boundview, 'gridview-')]")
            topics = driver.find_elements_by_class_name('x-grid-cell-inner')

            i=1
            for mail in mails:
                print (topics[i].text + " ## " + topics[i+1].text)
                mail.click()
                i=i+5
                time.sleep(0.5)
                while(True):
                    try:
                        driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
                        break
                    except:
                        time.sleep(2)

            time.sleep(15)
            driver.find_element_by_id('wiadomosci').click()
        except:
            print('Błąd serwerów czy chuj wie co // ponowne próbowanie')
            while(True):
                try:
                    try:
                        x = driver.find_element_by_xpath("//*[contains(@id, 'ribbon-logout-btn')]")
                    except:
                        stronaLogowania()

                    xx = driver.find_elements_by_class_name('x-component')
                    for x in xx:
                        if(x.text() == "Brak komunikacji z serwerem."): stronaLogowania()

                    x = driver.find_element_by_class_name('loginButton')
                    stronaLogowania()

                    x = driver.find_element_by_class_name('neterror')
                    stronaLogowania()
                except:
                    break
            pass

###
stronaLogowania()
###


#driver.find_element_by_xpath("//*[contains(@id, 'odebraneDzisiaj')]").click()
#driver.find_element_by_xpath("//*[contains(@id, 'odebraneTenTydzien')]").click()
