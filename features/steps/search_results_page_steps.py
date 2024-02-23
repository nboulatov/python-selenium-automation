from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

@when('I click on product: {product}')
def click_on_product(context, product):
    context.app.search_results_page.click_on_product()


@when('I click button: Add to cart')
def click_add_to_cart_button(context):
    context.app.search_results_page.click_add_to_cart_button()


@when('I click button: View cart & check out')
def click_view_cart_check_out_button(context):
    context.app.search_results_page.click_view_cart_check_out_button()


@then('I see search results for: {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)


@then('I see URL contains text: {expected_text_in_url}')
def verify_search_results_page_url(context, expected_text_in_url):
    context.app.search_results_page.verify_search_results_page_url(expected_text_in_url)


@then('I verify that every product has a name and image')
def verify_products_name_image(context):
    context.app.search_results_page.verify_products_name_image()