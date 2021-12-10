from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text

    y = calc(x)

   

    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)

    check_box_ = browser.find_element_by_css_selector("[id='robotCheckbox']")
    check_box_.click()

    button_ = browser.find_element_by_css_selector("[type='submit']") 
    browser.execute_script("window.scrollBy(0, 150)", "")
    
    radio_ = browser.find_element_by_css_selector("[id='robotsRule']")
    radio_.click()    

# Отправляем заполненную форму
     
    button_.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()