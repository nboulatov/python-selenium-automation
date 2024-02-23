from behave import given, when, then

@given('I navigate to site: Target.com')
def open_target(context):
    context.app.main_page.open_target()

@when('I click button: cart')
def click_cart_button(context):
    context.app.header.click_cart_button(context)

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

@then('I verify login for: {username}')
def verify_login(context, username):
    context.app.header.verify_login(context, username)