# Этот вариант решения, базовый 
# Для взаимодействия с выпадашкой или уже раскрытым используем одни и те же методы селениума.

# https://erikdark.github.io/QA_autotests_08/

# import time


# from selenium import webdriver


# from selenium.webdriver.common.by import By


# import re


# #вы пишите свой код
# try:
#     #инициализирую драйвер
#     driver = webdriver.Chrome()


#     # путь до страницы
#     driver.get('https://erikdark.github.io/QA_autotests_08/')




#     # ниже пишем свой код
#     driver.find_element(By.CSS_SELECTOR,'.container select').click()
#     driver.find_element(By.CSS_SELECTOR,'.container option:nth-child(3)').click()


#     driver.find_element(By.CSS_SELECTOR,'.container-main select').click()
#     driver.find_element(By.CSS_SELECTOR,'.container-main [value="3"]').click()

#     # конец блока с моим кодом





# Импортировать класс Select из вебдрайвера и использовать команду , метод select_by_value(значение)



import time

from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # импортируем класс Select




import re


#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_08/')




    # ниже пишем свой код

    select =  Select(driver.find_element(By.CSS_SELECTOR,'.container select'))#обращаемся к выпадашке (select), которая нах-ся в div class="container"


    select.select_by_value('3') # выбираем по умолчанию значение 3




    select_2  = Select(driver.find_element(By.CSS_SELECTOR,'.container-main select')) #обращаемся к выпадашке (select), которая нах-ся в div class="container-main"
    select_2.select_by_value('2') # выбираем по умолчанию значение 2



    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()


