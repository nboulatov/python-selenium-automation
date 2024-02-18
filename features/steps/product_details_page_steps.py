from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


@given('I navigate to product: {product}')
def open_product(context, product):
    context.app.product_details_page.open_product(product)


@then('I verify product colors')
def verify_product_colors(context):
    context.app.product_details_page.verify_product_colors(context)