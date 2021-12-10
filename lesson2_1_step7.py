from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    
    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)

    check_box_ = browser.find_element_by_css_selector("[id='robotCheckbox']")
    check_box_.click()    


    radio_ = browser.find_element_by_css_selector("[id='robotsRule']")
    radio_.click()


    # Отправляем заполненную форму
    button_ = browser.find_element_by_css_selector("button.btn-default")
    button_.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()







