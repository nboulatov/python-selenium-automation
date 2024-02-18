from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')

    def search_product(self):
        self.input_text('coffee',*self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_cart_icon(self, context):
        self.wait_for_clickable_element_and_click(*self.CART_ICON)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def verify_header(self, context):
        header = context.wait.until(EC.visibility_of_element_located((self.HEADER)), message='Header not found').text
