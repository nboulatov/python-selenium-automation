import time

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class Header(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')
    USER_GREETING = (By.XPATH, "//a[@data-test='@web/AccountLink']/span[contains(text(), 'Hi')]")
    CHEVRON_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")

    def search_product(self, product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_cart_button(self):
        self.wait_for_clickable_element_and_click(*self.CART_ICON)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def hover_over_sign_in_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.SIGN_IN_BUTTON)).perform()

    def verify_chevron_arrow(self):
        self.wait.until(EC.visibility_of_element_located((self.CHEVRON_ARROW)), message='Chevron arrow is not visible')

    def verify_header(self):
        self.wait.until(EC.visibility_of_element_located((self.HEADER)), message='Header not visible')

    def verify_login(self, username):
        self.verify_text(username, *self.USER_GREETING)

