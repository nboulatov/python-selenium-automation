from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@given('I navigate to site: https://help.target.com/help')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')


@then('I verify UI elements on Target Help page')
def verify_benefits(context):
    target_help_text = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]").text.strip()
    assert 'Target Help' in target_help_text, f'Expected "Target Help" not in {target_help_text}'
    assert context.driver.find_element(By.CSS_SELECTOR, ".search-input").is_displayed()
    assert context.driver.find_element(By.XPATH, "//input[@class='search-input']/following-sibling::input[@alt='search']").is_displayed()
    assert context.driver.find_element(By.CSS_SELECTOR, ".box-column").is_displayed()
    assert context.driver.find_element(By.CSS_SELECTOR, ".salesforceBox").is_displayed()
    contact_recalls = context.driver.find_elements(By.CSS_SELECTOR, ".boxSmallr")
    assert len(contact_recalls) == 2, f'Expected 2 does not equal {len(contact_recalls)}'
    assert context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']").is_displayed()
