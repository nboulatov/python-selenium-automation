from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.target_circle_page import TargetCirclePage
from pages.target_help_page import TargetHelpPage
from pages.product_details_page import ProductDetailsPage


class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.target_circle_page = TargetCirclePage(driver)
        self.target_help_page = TargetHelpPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.search_results_page = SearchResultsPage(driver)
