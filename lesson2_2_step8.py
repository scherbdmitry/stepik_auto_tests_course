from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys('Donald')  

    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys('Trump')

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys('D@trump.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_lesson2_2_step8.txt')

    file_button = browser.find_element_by_css_selector("[type='file']")
    file_button.send_keys(file_path)
       
    
    
# Отправляем заполненную форму
    button_ = browser.find_element_by_css_selector("[type='submit']") 
    button_.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()