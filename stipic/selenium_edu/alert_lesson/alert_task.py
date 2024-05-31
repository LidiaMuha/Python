from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert  # переключаемся на окно алерта
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")  # ищем элемент, где указан x
    x = x_element.text  # выводим x
    y = calc(x)  # результат выражения с x

    # записываем результат выражения в новую переменную
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
