import time


from selenium import webdriver


from selenium.webdriver.common.by import By




#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()


    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotests_13/')




    # ниже пишем свой код

    driver.find_element(By.ID,'openNewPageBtn').click()
    time.sleep(1)
    #2 вкалдка

    driver.switch_to.window (driver.window_handles[1])
    driver.find_element(By.ID,'displayTextBtn').click()
    if driver.find_element(By.ID, 'displayText').text == 'Я СДЕЛАЛ':
        print('da')
    else:
        print('nope')



    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()
