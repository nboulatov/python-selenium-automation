from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

@given('I navigate to site: Target.com')
def open_target_main(context):
  context.driver.get('https://www.target.com/')

# @when('I wait 2 seconds')
# def wait(context):
#     time.sleep(2)

@when('I click icon: cart')
def click_cart(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="@web/CartIcon"]'))).click()

@when('I click button: Sign in')
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()

@when('I click link: Sign in')
def click_sign_in_link(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="accountNav-signIn"]'))).click()

@when('I search: coffee')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()

@when('I click on product: coffee')
def click_on_product(context):
    wait = WebDriverWait(context.driver, 10)
    element_to_scroll_to = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@data-test="@web/site-top-of-funnel/ProductCardWrapper"])[1]')))
    context.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
    element_to_scroll_to.click()

@when('I click button: Add to cart')
def click_add_to_cart(context):
    wait = WebDriverWait(context.driver, 10)
    element_to_scroll_to = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@data-test="orderPickupButton"])[1]')))
    context.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
    element_to_scroll_to.click()

@when('I click button: View cart & check out')
def click_view_cart_check_out(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="View cart & check out"]'))).click()
    time.sleep(2)

@then('I verify message: Your cart is empty')
def verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    actual_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"] h1'))).text
    assert 'Your cart is empty' in actual_text, f'Expected word "Your cart is empty" not in {actual_text}'
    print('Test passed.')

@then('I verify message: Sign into your Target account')
def verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    actual_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Sign into your Target account")]'))).text
    assert 'Sign into your Target account' in actual_text, f'Expected word "Sign into your Target account" not in {actual_text}'
    print('Test passed.')

@then('I verify number of items in cart: 1 item')
def verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    actual_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[@id="cart-summary-heading"]/../div/span[text()="1 item"]'))).text
    assert '1 item' in actual_text, f'Expected word "1 item" not in {actual_text}'
    print('Test passed.')