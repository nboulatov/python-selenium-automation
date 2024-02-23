from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class CartPage(Page):
    CART_MESSAGE = (By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"] h1')
    CART_ITEMS = (By.XPATH, '//h1[@id="cart-summary-heading"]/following-sibling::div/span[contains(., "item")]')

    def verify_empty_cart(self):
        self.verify_text('Your cart is empty',*self.CART_MESSAGE)

    def verify_number_of_items_in_cart(self, items):
        self.verify_text(items, *self.CART_ITEMS)
