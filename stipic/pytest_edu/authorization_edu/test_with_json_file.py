import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config


class TestLogin:
    def test_authorization(self, browser, load_config):
        link = "https://stepik.org/lesson/236895/step/1"
        browser.implicitly_wait(15)
        data_dict = load_config
        login = data_dict['login_stepik']
        password = data_dict['password_stepik']
        browser.get(link)
        browser.find_element(By.CLASS_NAME,
                             "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
        login_field = browser.find_element(By.NAME, 'login')
        login_field.send_keys(login)
        pass_field = browser.find_element(By.NAME, 'password')
        pass_field.send_keys(password)
        browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    # @pytest.mark.parametrize('login, password', test_authorization(browser, 15, load_config))
    # def test_guest_should_see_login_link(browser, login, password):
        # link = "https://stepik.org/lesson/236895/step/1"
        # browser.implicitly_wait(15)
        # browser.get(link)
        # browser.find_element(By.CLASS_NAME,"ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
        # login_field = browser.find_element(By.NAME, 'login')
        # login_field.send_keys(login)
        # pass_field = browser.find_element(By.NAME, 'password')
        # pass_field.send_keys(password)
        # browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
