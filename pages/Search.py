from Functions.Base import Base
from selenium.webdriver.common.by import By



class SearchPage(Base):
    header_desc = (By.XPATH, "//*[@class='page-header page-header--search']/h1")
    product_box = (By.XPATH, '//div[@class="card card-product"]')
    elements_founded = (By.XPATH, 'div[@class="autocomplete-products-all-link"]')
    search_btn = '.search-widget__button'

    def search_word_is_displayed_in_search_header(self):
        return self.find_element(*self.header_desc).text

    def list_of_products(self):
        return len(self.driver.find_elements(*self.product_box))
