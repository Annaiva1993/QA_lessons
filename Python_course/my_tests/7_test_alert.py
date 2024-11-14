import time


from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import re


#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_12/')




    # ниже пишем свой код

    driver.find_element(By.ID,'startTaskBtn').click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.alert.send_keys('50')
    time.sleep(1)
    driver.switch_to.alert.accept()

    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)

