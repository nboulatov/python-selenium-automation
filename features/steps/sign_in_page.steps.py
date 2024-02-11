from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


@then('I verify message: Sign into your Target account')
def verify_results(context):
    actual_text = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Sign into your Target account")]')
                                         )
    , message='Sign into your Target account text not found').text
    assert 'Sign into your Target account' in actual_text, f'Expected word "Sign into your Target account" not in {actual_text}'
    print('Test passed.')
