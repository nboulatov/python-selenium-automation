from behave import given, when, then


@then('I verify message: Sign into your Target account')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page(context)