import time


from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By




#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5) # говорим webdriver искать каждый элемент 5 сек


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_14/')




    # ниже пишем свой код
    # time.sleep(1)
    # driver.find_element(By.ID, 'verify').click()
    
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click()
    #говорим selenium проверять, в течении 5 секунд, пока кнопка не станет доступной


    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
