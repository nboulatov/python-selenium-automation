from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SIGN_IN_LINK = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def open_target(self):
        self.open('https://www.target.com/')

    def click_sign_in_link(self):
        self.click(*self.SIGN_IN_LINK)
