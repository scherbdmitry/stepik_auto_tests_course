from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def sum_(x,y):
  num1 = int(x)
  num2 = int(y)
  return  str(num1 + num2)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("[id='num1']")
    x = x_element.text
    
    y_element = browser.find_element_by_css_selector("[id='num2']")
    y = y_element.text

    z = sum_(x,y)

    sel = Select(browser.find_element_by_tag_name("select"))
    sel.select_by_value(z)
    

    # Отправляем заполненную форму
    button_ = browser.find_element_by_css_selector("button.btn-default")
    button_.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()