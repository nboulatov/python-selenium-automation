from behave import given, when, then


@when('I input username: {username}')
def input_password(context, username):
    context.app.sign_in_page.input_username(username, context)

@when('I input password: {password}')
def input_password(context, password):
    context.app.sign_in_page.input_password(password, context)

@when('I click button: Sign in with password')
def click_sign_in_with_password_button(context):
    context.app.sign_in_page.click_sign_in_with_password_button(context)

@when('I click link: Skip')
def click_skip_link(context):
    context.app.sign_in_page.click_skip_link(context)

@when('I click button: Maybe later')
def click_maybe_later_button(context):
    context.app.sign_in_page.click_maybe_later_button(context)

@then('I verify message: Sign into your Target account')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page(context)

