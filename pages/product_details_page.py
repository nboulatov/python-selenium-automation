from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

class ProductDetailsPage(BasePage):
    PRODUCT_COLORS = (By.CSS_SELECTOR, ".children img[alt='Black'], .children img[alt='Deep Olive'], .children img[alt='White']")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

    def open_product(self, product):
        self.open(f'https://www.target.com/p/{product}')

    def verify_product_colors(self):
        colors = self.driver.find_elements(*self.PRODUCT_COLORS)
        expected_colors = [color.get_attribute("alt") for color in colors]
        print(expected_colors)
        actual_colors = []
        for color in colors:
            color.click()
            selected_color = self.wait.until(EC.visibility_of_element_located(self.SELECTED_COLOR)).text.split('\n')[1]
            actual_colors.append(selected_color)
        assert expected_colors == actual_colors, f'\nExpected: {expected_colors}.\nActual: {actual_colors}.'

