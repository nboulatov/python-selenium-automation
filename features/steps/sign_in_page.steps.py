from behave import given, when, then


@when('I input username: {username}')
def input_password(context, username):
    context.app.sign_in_page.input_username(username)

@when('I input password: {password}')
def input_password(context, password):
    context.app.sign_in_page.input_password(password)

@when('I click button: Sign in with password')
def click_sign_in_with_password_button(context):
    context.app.sign_in_page.click_sign_in_with_password_button()

@when('I click link: Skip')
def click_skip_link(context):
    context.app.sign_in_page.click_skip_link()

@when('I click link: Target terms and conditions')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_terms_and_conditions_link()

@when('I click button: Maybe later')
def click_maybe_later_button(context):
    context.app.sign_in_page.click_maybe_later_button()

@then('I verify message: {message}')
def verify_sign_in_page(context, message):
    context.app.sign_in_page.verify_sign_in_page(message)

