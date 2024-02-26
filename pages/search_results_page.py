from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC


class SearchResultsPage(BasePage):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    VIEW_CART_AND_CHECK_OUT_BUTTON = (By.XPATH, '//a[text()="View cart & check out"]')
    ALL_PRODUCT_IMAGES = (By.XPATH, "//section[contains(@class, 'StyledRowWrapper')]//*/h3//picture[@data-test='@web/ProductCard/ProductCardImage/primary']/img")
    ALL_PRODUCT_TITLES = (By.XPATH, "//*[@data-test='@web/ProductCard/body']//*[@title]")
    ORDER_PICKUP_BUTTON = (By.XPATH, '(//button[@data-test="orderPickupButton"])[1]')

    def click_on_product(self):
        locator = (By.XPATH, '(//div[@data-test="@web/site-top-of-funnel/ProductCardWrapper"])[1]')
        self.scroll_to(*locator)
        self.wait_for_clickable_element_and_click(*locator)

    def click_add_to_cart_button(self):
        self.scroll_to(*self.ORDER_PICKUP_BUTTON)
        self.wait_for_clickable_element_and_click(*self.ORDER_PICKUP_BUTTON)

    def click_view_cart_check_out_button(self):
        self.wait_for_clickable_element_and_click(*self.VIEW_CART_AND_CHECK_OUT_BUTTON)

    def verify_search_results(self, product):
        self.verify_text(product, *self.SEARCH_RESULTS_HEADER)

    def verify_search_results_page_url(self, expected_text_in_url):
        self.verify_url(expected_text_in_url)

    def verify_products_name_image(self):
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 2):
            self.driver.execute_script(f"window.scrollTo(0, {i});")

        all_titles = self.driver.find_elements(*self.ALL_PRODUCT_TITLES)
        all_images = self.driver.find_elements(*self.ALL_PRODUCT_IMAGES)
        expected_titles = [title.get_attribute("title") for title in all_titles]
        expected_images = [image.get_attribute("alt") for image in all_images]
        assert len(expected_titles) == len(expected_images),\
            f'\nExpected: {len(expected_titles)}.\nActual: {len(expected_images)}.'
        assert expected_titles == expected_images,\
            f'\nExpected: {expected_titles}.\nActual: {expected_images}.'


