from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("a user in the Glossary page")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/frontend-tests/bdd-test-activity/features/glossary/features/steps/utils/drivers/chromedriver.exe")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victoralunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    WebDriverWait(context.driver, 40).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner')))
    while context.driver.find_element_by_xpath(
            '/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed():
        pass

    glossary_button = context.driver.find_element_by_id("nav-item-6")
    glossary_button.click()

@when("they inserts the existent word and clicks in Search")
def when(context):
    search_input = context.driver.find_element_by_id("search")
    search_input.send_keys("Customer")
    search_button = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-glossary/div/app-small-header/div[2]/div[1]/div/button')
    search_button.click()


@then("the system shows the word and the concept")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-glossary/div/app-small-header/div[2]/div[5]'),
        "Customer"))

    context.driver.quit()
