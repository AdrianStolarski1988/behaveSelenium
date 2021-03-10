import time

from behave import given, when, then, fixture
from selenium.webdriver.support import expected_conditions as ec
from pages.Login import LoginPage
from pages.MyAccount import MyAccountPage



@given('the user go to login site')
def step_impl(context):
    site = LoginPage(context.driver)
    site.go_to(site.BASE_URL + site.login_url)


@when('customer log in with email "{email}" and password "{password}"')
def step_impl(context, email, password):
    driver = LoginPage(context.driver)
    driver.enter_email(email)
    driver.enter_password(password)
    driver.click_on_sign_up_btn()

@then('customer is on "{url}" site')
def step(context, url):
    assert ec.url_contains(url)


