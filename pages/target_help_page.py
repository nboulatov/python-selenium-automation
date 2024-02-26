from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TargetHelpPage(BasePage):

    def open_target_help(self):
        self.open('https://help.target.com/help')

    def verify_target_help_ui(self):
        target_help_text = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]").text.strip()
        assert 'Target Help' in target_help_text, f'\nExpected: Target Help.\nActual: {target_help_text}.'
        assert self.driver.find_element(By.CSS_SELECTOR, ".search-input").is_displayed()
        assert self.driver.find_element(By.XPATH,
                                           "//input[@class='search-input']/following-sibling::input[@alt='search']").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, ".box-column").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, ".salesforceBox").is_displayed()
        contact_recalls = self.driver.find_elements(By.CSS_SELECTOR, ".boxSmallr")
        assert len(contact_recalls) == 2, f'\nExpected: 2.\nActual: {len(contact_recalls)}'
        assert self.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']").is_displayed()
