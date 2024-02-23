from behave import given, when, then


@when('I switch to tab: new')
def switch_to_new_tab(context):
    context.app.page.switch_to_new_tab()

@when('I store tab: original')
def store_sign_in_tab(context):
    context.original_tab = context.app.page.store_original_tab()

@when('I switch to tab: original')
def switch_to_original_tab(context):
    context.app.page.switch_to_original_tab(context.original_tab)

@when('I close tab: current')
def close_current_tab(context):
    context.app.page.close_current_tab()
