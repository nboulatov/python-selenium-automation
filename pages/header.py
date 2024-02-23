from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')
    USER_GREETING = (By.XPATH, "//a[@data-test='@web/AccountLink']/span[contains(text(), 'Hi')]")

    def search_product(self, product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_cart_button(self):
        self.wait_for_clickable_element_and_click(*self.CART_ICON)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def verify_header(self):
        self.wait.until(EC.visibility_of_element_located((self.HEADER)), message='Header not found')

    def verify_login(self, context, username):
        self.verify_text(username, *self.USER_GREETING)

