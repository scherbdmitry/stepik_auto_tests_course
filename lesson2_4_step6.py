from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_id("button")
    

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()