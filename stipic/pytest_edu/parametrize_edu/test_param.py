from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium import webdriver
import time
import math
import pytest
import json

uncorrected_results = []

# # Задаем путь к драйверу Microsoft Edge
# edge_driver_path = 'path/to/edge/driver'
# # Создаем экземпляр драйвера Microsoft Edge
# driver = webdriver.Edge(executable_path=edge_driver_path)
# # Переходим на страницу очистки кеша
# driver.get('edge://settings/clearBrowserData')
# # Устанавливаем флаги для очистки кеша и нажимаем кнопку "Очистить данные"
# driver.find_element_by_css_selector('#clearBrowsingDataConfirm').click()


# открываем браузер и авторизуемся, затем после окончания теста выходим и закрываем окно браузера
@pytest.fixture(scope="function")
def browser(load_config):  # вписать потом load_config когда буду пробовать с авторизацией
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(55)
    yield browser
    print("\nquit browser..")

    browser.quit()
    print(''.join(uncorrected_results))


@pytest.fixture()
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


@pytest.mark.parametrize('link_task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, link_task, load_config):
    link = f"https://stepik.org/lesson/{link_task}/step/1"
    browser.get(link)
    data_dict = load_config
    login = data_dict['login_stepik']
    password = data_dict['password_stepik']
    browser.find_element(By.CLASS_NAME, "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    login_field = browser.find_element(By.NAME, 'login')
    login_field.send_keys(login)
    pass_field = browser.find_element(By.NAME, 'password')
    pass_field.send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    # time.sleep(20)

    # button_again = WebDriverWait(browser, 55) \
    #     .until(e_c.visibility_of_element_located((By.CLASS_NAME, 'again-btn.white')))
    # button_again.click()

    answer_place = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
    answer_place.send_keys(str(math.log(int(time.time()))))

    submit_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()

    option_text = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'
