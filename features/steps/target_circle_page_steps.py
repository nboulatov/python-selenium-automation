from selenium.webdriver.common.by import By
from behave import given, when, then


@given('I navigate to site: Target.com/circle')
def open_target_circle(context):
    context.app.target_circle_page.open_target_circle()


@then('I verify number of benefits: {expected_amount} benefits')
def verify_circle_benefits(context, expected_amount):
    context.app.target_circle_page.verify_circle_benefits(expected_amount)