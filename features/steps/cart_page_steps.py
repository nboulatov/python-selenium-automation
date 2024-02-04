from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@then('I verify message: Your cart is empty')
def verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    actual_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test="boxEmptyMsg"] h1'))).text
    assert 'Your cart is empty' in actual_text, f'Expected word "Your cart is empty" not in {actual_text}'
    print('Test passed.')


@then('I verify number of items in cart: 1 item')
def verify_results(context):
    wait = WebDriverWait(context.driver, 10)
    actual_text = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[@id="cart-summary-heading"]/../div/span[text()="1 item"]'))).text
    assert '1 item' in actual_text, f'Expected word "1 item" not in {actual_text}'
    print('Test passed.')