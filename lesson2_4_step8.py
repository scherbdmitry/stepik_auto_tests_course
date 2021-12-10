from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	
	button_ = browser.find_element_by_css_selector("[id='book']")

	
	WebDriverWait(browser, 12).until(
        		EC.text_to_be_present_in_element((By.ID, "price"), "100")
    		)
	
	button_.click()

	x_element = browser.find_element_by_css_selector("[id='input_value']")
	x = x_element.text
	y = calc(x)

	browser.execute_script("window.scrollBy(0, 150)", "")

	answer = browser.find_element_by_css_selector("[id='answer']")
	answer.send_keys(y)

	button_ = browser.find_element_by_css_selector("[type='submit']")
	button_.click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    	time.sleep(10)
    	# закрываем браузер после всех манипуляций
    	browser.quit()



