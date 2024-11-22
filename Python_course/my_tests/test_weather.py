# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import requests

# def get_weather_from_api():
#     api_url = 'https://openweathermap.org/data/2.5/weather'

#     response = requests.get(api_url)
#     if response.status_code == 200:
#         data = response.json()
#         return 
    
#     else:
#         print('Ошибка в запросе.')


# def get_exchange_rate_from_site():
#     driver  = webdriver.Chrome()
#     driver.get('https://openweathermap.org/ ')


#     try:


#     finally:
#         driver.quit()


#         return euro_rate





#     if __name__ == "__main__":
#     import pytest
#     pytest.main()

 def test_recept(api_params): 
    response = requests.get(API_URL, params=api_params) 
    data = response.json() 
 
    
    assert len(data) > 0 
 
    recipe = data[0] 
 
   
    assert "title" in recipe 
 
    title = recipe["title"] 
 
    if "image" in recipe: 
        image_url = recipe["image"] 
    else: 
         print(f"Изображение не найдено") 
 
    print(f"Название рецепта: {title}") 
    print(f"Ссылка на изображение: {image_url}")
