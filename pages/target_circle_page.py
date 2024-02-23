from pages.base_page import Page
from selenium.webdriver.common.by import By


class TargetCirclePage(Page):
    CIRCLE_BENEFITS = (By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")
    def open_target_circle(self):
        self.open('https://www.target.com/circle')

    def verify_circle_benefits(self, expected_amount):
        number_of_benefits = self.driver.find_elements(*self.CIRCLE_BENEFITS)
        assert len(number_of_benefits) == int(expected_amount),\
            f'\nExpected: {expected_amount}.\nActual: {len(number_of_benefits)}.'
