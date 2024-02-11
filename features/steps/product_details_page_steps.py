from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import  expected_conditions as EC


PRODUCT_COLORS = (By.CSS_SELECTOR, ".children img[alt='Black'], .children img[alt='Deep Olive'], .children img[alt='White']")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@then('I verify product\'s colors')
def verify_product_colors(context):
    colors = context.driver.find_elements(*PRODUCT_COLORS)
    expected_colors = [color.get_attribute("alt") for color in colors]
    actual_colors = []
    for color in colors:
        color.click()
        selected_color = context.wait.until(EC.visibility_of_element_located(SELECTED_COLOR)).text.split('\n')[1]
        actual_colors.append(selected_color)
    assert expected_colors == actual_colors, f'Expected {expected_colors}, got {actual_colors}'
