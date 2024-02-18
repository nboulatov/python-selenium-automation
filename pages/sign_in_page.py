from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, '//span[contains(text(), "Sign into your Target account")]')

    def verify_sign_in_page(self, context):
        self.wait_for_clickable_element_and_click(*self.SIGN_IN_TEXT)
