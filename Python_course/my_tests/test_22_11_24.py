import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time






API_URL = "https://api.spoonacular.com/recipes/findByIngredients"
API_KEY = "73c4ae0cca6d49908b5244ba13902dd8"
SITE_URL = "https://erikdark.github.io/recept_api/"
ingredients = ['apple','flour','sugar']




def get_recipe_from_api():
   params = {
    "ingredients": ",".join(ingredients),
    "number": 1,
    "apiKey": API_KEY,
}
   response = requests.get(API_URL, params=params)
   assert response.status_code == 200, "Ошибка при запросе API"
   return response.json()[0]




def test_recipe_search():
   api_data = get_recipe_from_api()
   api_title = api_data["title"]
   api_image = api_data["image"]
   api_link = f'https://api.spoonacular.com/recipes/{api_data["title"]}-{api_data["id"]}'




   driver = webdriver.Chrome()
   driver.get(SITE_URL)


   try:
     
      driver.find_element(By.ID,'ingredients').send_keys(", ".join(ingredients))
      driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()




      driver.implicitly_wait(5)


      site_title = driver.find_element(By.TAG_NAME,'h2').text.replace("Recipe: ",'')
      site_image = driver.find_element(By.TAG_NAME,'img').get_attribute("src")
     
      assert api_title == site_title, 'название не совпадает'
      assert api_image == site_image, 'изображение не совпадает'
   




   finally:
    driver.quit()
