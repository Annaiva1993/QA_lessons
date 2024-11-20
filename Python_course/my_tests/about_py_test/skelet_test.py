import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_your_name_1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/Qa_autotest_15/')

    finally:
        time.sleep(3)
        driver.quit()
