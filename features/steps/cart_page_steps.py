from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


@then('I verify message: Your cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()

@then('I verify number of items in cart: {items}')
def verify_number_of_items_in_cart(context, items):
    context.app.cart_page.verify_number_of_items_in_cart(items)