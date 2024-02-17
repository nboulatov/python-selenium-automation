from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class TargetCirclePage(Page):

    def open_target_circle(self, context):
        context.driver.get('https://www.target.com/circle')

    def verify_benefits(self, context, expected_amount):
        number_of_benefits = context.driver.find_elements(
            By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")
        assert len(number_of_benefits) == int(
            expected_amount), f'Expected {expected_amount} benefits does not equal {len(number_of_benefits)} actual'
