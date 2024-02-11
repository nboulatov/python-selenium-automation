from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC

SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
SEARCH_ICON = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartIcon"]')
HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')
SIGN_IN_ICON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
SIGN_IN_LINK = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


@given('I navigate to site: Target.com')
def open_target_main(context):
  context.driver.get('https://www.target.com/')


@given('I navigate to product: {product}')
def open_product(context, product):
  context.driver.get(f'https://www.target.com/p/{product}')


@when('I click icon: cart')
def click_cart(context):
    context.wait.until(
        EC.element_to_be_clickable(CART_ICON), message='Cart Icon not found').click()


@when('I click button: Sign in')
def click_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_ICON).click()


@when('I click link: Sign in')
def click_sign_in_link(context):
    context.wait.until(EC.element_to_be_clickable(SIGN_IN_LINK), message='Sign in link not found').click()


@when('I search: {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys({product})
    context.driver.find_element(*SEARCH_ICON).click()


@then('I verify: header')
def verify_results(context):
    header = context.wait.until(EC.visibility_of_element_located((HEADER)), message='Header not found').text
    print(header)
