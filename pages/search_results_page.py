from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
import time


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    VIEW_CART_AND_CHECK_OUT_BUTTON = (By.XPATH, '//a[text()="View cart & check out"]')
    ALL_PRODUCT_IMAGES = (By.XPATH, "//section[contains(@class, 'StyledRowWrapper')]//*/h3//picture[@data-test='@web/ProductCard/ProductCardImage/primary']/img")
    ALL_PRODUCT_TITLES = (By.XPATH, "//*[@data-test='@web/ProductCard/body']//*[@title]")

    def click_on_product(self, context):
        element_to_scroll_to = context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@data-test="@web/site-top-of-funnel/ProductCardWrapper"])[1]')
                                       ))
        context.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
        element_to_scroll_to.click()


    def click_add_to_cart_button(self, context):
        element_to_scroll_to = context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@data-test="orderPickupButton"])[1]')
                                       ), message='Add to cart button not found')
        context.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
        element_to_scroll_to.click()


    def click_view_cart_check_out_button(self, context):
        context.wait.until(
            EC.element_to_be_clickable(self.VIEW_CART_AND_CHECK_OUT_BUTTON)
            , message='View cart & check out button not found').click()


    def verify_search_results(self, context, product):
        actual_text = context.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_HEADER)).text
        assert product in actual_text, f'Expected {product} not in actual "{actual_text}"'


    def verify_search_results_page_url(self, expected_text_in_url):
        url = self.driver.current_url
        assert expected_text_in_url in url, f'Expected {expected_text_in_url} not in {url}'


    def verify_products_name_image(self, context):
        total_height = int(context.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 3):
            context.driver.execute_script(f"window.scrollTo(0, {i});")

        all_titles = context.driver.find_elements(*self.ALL_PRODUCT_TITLES)
        all_images = context.driver.find_elements(*self.ALL_PRODUCT_IMAGES)
        expected_titles = [title.get_attribute("title") for title in all_titles]
        expected_images = [image.get_attribute("alt") for image in all_images]
        assert len(expected_titles) == len(
            expected_images), f'Expected {len(expected_titles)} titles, got {len(expected_images)} images'
        assert expected_titles == expected_images, f'Expected {expected_titles} titles, got {expected_images} images'


