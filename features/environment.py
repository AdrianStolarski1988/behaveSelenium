from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def browser_config(browser_options):
    # browser_options.add_argument('--headless')
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--disable-dev-shm-usage')
    return browser_options


def before_all(context):
    browser_options = ChromeOptions()

    browser_config(browser_options)
    context.driver = webdriver.Chrome(options=browser_options)
    # context.driver.set_window_size(1920, 1080)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.close()
