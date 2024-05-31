from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, "input_value")  # ищем элемент, где указан x
    x = x_element.text  # выводим x
    y = calc(x)  # результат выражения с x

    # записываем результат выражения в новую переменную
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(120)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
