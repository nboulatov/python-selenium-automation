from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class CartPage(Page):


    def verify_empty_cart(self, context):
        actual_text = context.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"] h1')
                                             ), message='Cart is not empty').text
        assert 'Your cart is empty' in actual_text, f'Expected word "Your cart is empty" not in {actual_text}'
        print('Test passed.')


    def verify_number_of_items_in_cart(self, context):
        actual_text = context.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//h1[@id="cart-summary-heading"]/../div/span[text()="1 item"]')
                                             ), message='Cart has a different number of items').text
        assert '1 item' in actual_text, f'Expected word "1 item" not in {actual_text}'
        print('Test passed.')