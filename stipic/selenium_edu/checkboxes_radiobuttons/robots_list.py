from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x, y):
        return x + y


    num_1 = browser.find_element(By.ID, "num1")  # ищем элемент, где указано число 1
    num_1_int = int(num_1.text)  # выводим число
    print(num_1_int)
    num_2 = browser.find_element(By.ID, "num2")  # ищем элемент, где указано число 1
    num_2_int = int(num_2.text)  # выводим число
    print(num_2_int)
    num_sum = calc(num_1_int, num_2_int)  # результат суммы
    print(num_sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num_sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
