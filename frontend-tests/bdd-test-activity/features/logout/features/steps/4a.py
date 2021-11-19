from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("user be logged in the platform")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/frontend-tests/bdd-test-activity/features/logout/features/steps/utils/drivers/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victoralunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, "avatar")))


@when("they click in Sign Out")
def when(context):
    avatar_icon = context.driver.find_element_by_id("avatar")
    avatar_icon.click()

    logout_button = context.driver.find_element_by_id("logout")
    logout_button.click()

    confirm_button = context.driver.find_element_by_id("confirm")
    confirm_button.click()


@then("Then the user should be redirected for login page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.ID, "login")))
    context.driver.quit()