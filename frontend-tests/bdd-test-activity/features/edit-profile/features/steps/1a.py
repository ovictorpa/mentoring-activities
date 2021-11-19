from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("user in the Edit Profile page")
def given(context):
    context.driver = webdriver.Chrome(
        "C:/Users/Victor/PycharmProjects/mentoring-activities/frontend-tests/bdd-test-activity/features/edit-profile/features/steps/1a.py")
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("victoralunoaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    WebDriverWait(context.driver, 40).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner')))
    while context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed():
        pass

    avatar_button = context.driver.find_element_by_id("avatar")
    avatar_button.click()

    editprofile_button = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/button')
    editprofile_button.click()

    WebDriverWait(context.driver, 40).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner')))
    while context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed():
        pass

@when("fills out all the required informations and clicks in Save Profile")
def when(context):
    saveprofile_button = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[11]/button')
    saveprofile_button.click()


@then("system updates the informations")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/div/app-alert/div/div')))
    context.driver.quit()
