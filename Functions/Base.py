import logging
from seleniumpagefactory import PageFactory

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.BASE_URL = "https://tortytorty.pl/"

    def find_element(self, locator, element):
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((locator, element)))
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshot("screenshots/not_find_expected_element.png")
            return False
        finally:
            pass

    def find_elementy(self, locator, element):
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((locator, element)))
        except (TimeoutException, NoSuchElementException):
            # self.driver.save_screenshot("screenshots/not_find_expected_element.png")
            return False
        finally:
            pass

    def check_element_is_displayed(self, locator, element):
        try:
            return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((locator, element)))
        except NoSuchElementException as e:
            logging.error(e)
            logging.warning(f'not found {element}')
            return False

    def check_element_is_visible(self, locator, element):
        try:
            return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((locator, element)))
        except NoSuchElementException as e:
            logging.error(e)
            logging.warning(f'not found {element}')
            return False
        finally:
            pass

    def if_element_exist(self, locator, element):
        try:
            WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((locator, element)))
            return True
        except TimeoutException:
            return False
        except NoSuchElementException as e:
            logging.error(e)
            logging.warning(f'not found {element}')
            return False

    def send_text(self, locator, message):
        self.find_element(*locator).send_keys(message)

    def go_to(self, website):
        self.driver.get(website)


def screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TimeoutException, NoSuchElementException) as e:
            args[0].driver.save_screenshot("screenshots/error.png")
            logging.error(e)
            return False

    return wrapper