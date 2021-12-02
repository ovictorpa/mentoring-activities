from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("a user is in the Editions page")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/final-activity/question-02/tests_editions/features/steps/drivers/chromedriver.exe")
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victor.alves@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("a20021709")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/ul/li[2]/button')))

    editions_button = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[2]/a')
    editions_button.click()


@when("the user inserts the existent edition name and clicks in Search")
def when(context):

    WebDriverWait(context.driver, 40).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/ng-http-loader')))
    while context.driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed():
        pass

    input_edition_name = context.driver.find_element_by_id("name")
    input_edition_name.send_keys("test")

    search_button = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-editions/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/div[2]/button[1]')
    search_button.click()


@then("the system shows the edition")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]')))
    context.driver.quit()
