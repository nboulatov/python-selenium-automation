import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


@given('I navigate to site: Target.com')
def open_target_main(context):
  context.app.main_page.open_main()


@when('I click icon: cart')
def click_cart(context):
    context.app.header.click_cart_icon(context)


@when('I click button: Sign in')
def click_sign_in_button(context):
    context.app.header.click_sign_in_button()


@when('I click link: Sign in')
def click_sign_in_link(context):
    context.app.main_page.click_sign_in_link()


@when('I search: {product}')
def search_product(context, product):
    context.app.header.search_product()


@then('I verify: header')
def verify_header(context):
    context.app.header.verify_header(context)