from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("a user is in the SGME platform login page")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/final-activity/question-02/login/features/steps/drivers/chromedriver.exe")
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()


@when("the user insert they valid credentials")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victor.alves@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("a20021709")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()


@then("system redirects the user to the homepage")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/ul/li[2]/button')))
    context.driver.quit()
