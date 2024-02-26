import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

class SignInPage(BasePage):
    LOCATORS = {
        "Sign into your Target account": (By.XPATH, '//span[contains(text(), "Sign into your Target account")]'),
        "We can't find your account": (By.XPATH, '//div[@data-test="authAlertDisplay"]//div[text()="We can\'t find your account."]'),
        "That password is incorrect": (By.XPATH, "//div[@data-test='authAlertDisplay']//div[text()='That password is incorrect.']"),
    }
    USERNAME_FIELD = (By.CSS_SELECTOR, '#username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')
    SKIP_LINK = (By.XPATH, "//a[text()='Skip']")
    MAYBE_LATER_BUTTON = (By.XPATH, "//button[text()='Maybe later']")
    TARGET_TERMS_AND_CONDITIONS = (By.XPATH, "//a[text()='Target terms and conditions']")

    def verify_sign_in_page(self, message):
        locator = self.LOCATORS.get(message)
        self.wait_for_visible_element(*locator)

    def input_username(self, username):
        self.input_text(username, *self.USERNAME_FIELD)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_sign_in_with_password_button(self):
        self.wait_for_clickable_element_and_click(*self.LOGIN_BUTTON)

    def click_target_terms_and_conditions_link(self):
        self.wait_for_clickable_element_and_click(*self.TARGET_TERMS_AND_CONDITIONS)

    def click_skip_link(self):
        self.wait_for_clickable_element_and_click(*self.SKIP_LINK)

    def click_maybe_later_button(self):
        self.wait_for_clickable_element_and_click(*self.SKIP_LINK)
