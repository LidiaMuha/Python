from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    button1 = browser.find_element(By.TAG_NAME, "button")  # ищем кнопку
    button1.click()  # и нажимаем на неё

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")  # ищем элемент, где указан x
    x = x_element.text  # выводим x
    y = calc(x)  # результат выражения с x

    # записываем результат выражения в новую переменную
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
