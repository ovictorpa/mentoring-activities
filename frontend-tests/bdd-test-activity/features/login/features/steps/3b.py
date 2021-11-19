from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("user in the login page")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/frontend-tests/bdd-test-activity/features/login/features/steps/utils/drivers/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()


@when("user insert they invalid credentials")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victoralunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd123")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()


@then("system returns that the credentials are not valid")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/app-root/app-login/html/body/form/div[1]'),
        "Usuário e/ou senha inválidos. Verifique o usuário e senha e tente novamente."))
    context.driver.quit()
