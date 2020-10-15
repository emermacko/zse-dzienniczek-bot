# Bot do vulcanowego dziennika
Automatyczne wyświetlanie wiadomości na e-dzienniku na czas koronaferii

<br><br>

<p align="center">
  <a href="http://bit.ly/BuyMeACoffee-GitHub" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-black.png" alt="Buy Me A Coffee" height="50px"></a>
</p>

<br><br>


## Demo
<p align="center">
  <img width="auto" height="auto" src="https://user-images.githubusercontent.com/25122875/85282951-d890a280-b48c-11ea-9756-1bdea499dd6b.png">
</p>

<br>

## Wymagania:
* Python 3.7+
* Selenium - `pip install selenium`
* Przeglądarka w zależności od użytego `WebDrivera`

<br>

## Uruchamianie:
* `double-clickiem`
<br> lub
* `python bot.py`

<br>
 
## Konwertowanie na .exe:
* Wymagany **pyinstaller** - `pip install pyinstaller`
* `pyinstaller --onefile bot.py` •• To samo działanie ma plik `py2exe.bat`

**Po przekonwertowaniu python nie jest juz wymagany**

<br>

## WebDriver:
* Wybór przeglądarki - https://pypi.org/project/selenium/#drivers
* Adekwatnie do tego trzeba zmienic w kodzie linijkę: `driver = webdriver.Chrome('ścieżka_do_webdrivera')`
