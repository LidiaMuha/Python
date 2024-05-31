from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "input_value")  # ищем элемент, где указан x
x = x_element.text  # выводим x
y = calc(x)  # результат выражения с x

# записываем результат выражения в новую переменную
input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys(y)


option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
option2.click()


button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
