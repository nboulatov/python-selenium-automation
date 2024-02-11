from selenium.webdriver.common.by import By
from behave import given, when, then


@given('I navigate to site: Target.com/circle')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('I verify number of benefits: {expected_amount} benefits')
def verify_benefits(context, expected_amount):
    number_of_benefits = context.driver.find_elements(
        By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")
    assert len(number_of_benefits) == int(expected_amount), f'Expected {expected_amount} benefits does not equal {len(number_of_benefits)} actual'