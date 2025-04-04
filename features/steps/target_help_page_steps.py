from selenium.webdriver.common.by import By
from behave import given, when, then


@given('I navigate to site: https://help.target.com/help')
def open_target_help(context):
    context.app.target_help_page.open_target_help()

@then('I verify UI elements on Target Help page')
def verify_target_help_ui(context):
    context.app.target_help_page.verify_target_help_ui()