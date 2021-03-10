from Functions.Base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    login_url = "logowanie?back=my-account"

    email_field = (By.NAME, "email")
    password_field = (By.NAME, 'password')
    elements_founded = (By.XPATH, 'div[@class="autocomplete-products-all-link"]')
    submit_btn = (By.ID, 'submit-login')

    def enter_email(self, email_name):
        self.send_text(self.email_field, email_name)

    def enter_password(self, password):
        self.send_text(self.password_field, password)

    def click_on_sign_up_btn(self):
        self.find_element(*self.submit_btn).click()
