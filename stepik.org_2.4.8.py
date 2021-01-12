from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calculate(x):
    return str(math.log(abs(12*math.sin(x))))

try: 

    browser = webdriver.Chrome()
    browser.get(link)

    #price = browser.find_element_by_id("price").text
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button.click()
    
    x = int(browser.find_element_by_id('input_value').text)
    result = calculate(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(result)
    
    button_form = browser.find_element_by_css_selector("button[type='submit']")
    button_form.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = str(alert_text.split(': ')[-1])
    print(f'addToClipBoard: {addToClipBoard}')
  

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #print(f'Answer: {addToClipBoard}')

