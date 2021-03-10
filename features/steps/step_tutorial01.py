import time

from behave import given, when, then
from behave import step
import time

@when(u'visit url "{url}"')
def step(context, url):
    context.driver.get(url)

@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.driver.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)

@then('title becomes "{title}"')
def step(context, title):
    assert context.driver.title == title

@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.driver.page_source
