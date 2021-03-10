import time

from behave import given, when, then, fixture
from selenium.webdriver.support import expected_conditions as ec

from pages import Main, Search



@given('the user go to main site')
def step_impl(context):
    site = Main.MainSite(context.driver)
    site.go_to(site.BASE_URL)


@when('the user enter to search bar words "{product}" and see hint')
def step_impl(context, product):
    driver = Main.MainSite(context.driver)
    driver.search_product_by_name(product)
    driver.hint_is_displayed()
    amount = driver.amount_of_find_products_is_displayed()
    print(amount)
    context.amount_from_hint = amount


#
@when('the user click on search button')
def step_impl(context):
    driver = Main.MainSite(context.driver)
    driver.click_on_search_button()


@then('the user is on search site with url "{url}"')
def step_impl(context, url):
    assert ec.url_contains(url)


@then('the text in header of search is "{word}"')
def step_impl(context, word):
    driver = Search.SearchPage(context.driver)
    assert word in driver.search_word_is_displayed_in_search_header()

@then('the user see list of products after click on search button')
def check_display_list_of_products(context):
    driver = Search.SearchPage(context.driver)
    amount2 = driver.list_of_products()
    context.amount_from_list = str(amount2)
    assert amount2 > 0


@then('amount displayed product is equal with amount in hint')
def compare_amount_of_products(context):
    assert context.amount_from_hint == context.amount_from_list