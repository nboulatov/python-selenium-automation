from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


VIEW_CART_AND_CHECK_OUT_BUTTON = (By.XPATH, '//a[text()="View cart & check out"]')


@when('I click on product: {product}')
def click_on_product(context, product):
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
    wait.until(EC.element_to_be_clickable(VIEW_CART_AND_CHECK_OUT_BUTTON)).click()
    time.sleep(2)
