from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys(y)

    field1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[1]")
    field1.send_keys("Лидия")

    field2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[2]")
    field2.send_keys("Павловна")

    field3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[3]")
    field3.send_keys("lida@mail.ru")

    my_file = os.path.abspath((os.path.dirname(__file__)))  # получаем путь к директории исп-ого файла
    put_file = os.path.abspath(my_file, 'my_file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(put_file)

    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button/font/fontn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла