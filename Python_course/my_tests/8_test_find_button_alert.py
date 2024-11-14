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
    driver.get('https://erikdark.github.io/Qa_autotest_01/')




    # ниже пишем свой код

    input_text  = 'Hello World'
    driver.find_element(By.ID,'inputField').send_keys(input_text)


    buttons = driver.find_elements(By.CLASS_NAME,'btn')


    for button in buttons:
        button.click()
        time.sleep(1)
        try:
            driver.switch_to.alert.accept()

        except: # после нахождения нужной кнопки проверку останавливаем, чтобы алерт не выводил
            pass


        output = driver.find_element(By.ID,'output').text
        if output == input_text:
            break




    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
