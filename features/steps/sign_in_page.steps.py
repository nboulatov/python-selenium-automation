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

@when('I click link: Target terms and conditions')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_terms_and_conditions_link(context)

@when('I click button: Maybe later')
def click_maybe_later_button(context):
    context.app.sign_in_page.click_maybe_later_button(context)

@when('I store tab: original')
def store_sign_in_tab(context):
    context.app.sign_in_page.store_original_tab(context)

@when('I switch to tab: new')
def switch_to_new_tab(context):
    context.app.sign_in_page.switch_to_new_tab()

@when('I close tab: current')
def close_current_tab(context):
    context.app.sign_in_page.close_current_tab()

@when('I switch to tab: original')
def switch_to_original_tab(context):
    context.app.sign_in_page.switch_to_original_tab(context)

@then('I verify message: Sign into your Target account')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page(context)

