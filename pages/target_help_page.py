from pages.base_page import Page
from selenium.webdriver.common.by import By


class TargetHelpPage(Page):

    def open_target_help(self, context):
        context.driver.get('https://help.target.com/help')

    def verify_benefits(self, context):
        target_help_text = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]").text.strip()
        assert 'Target Help' in target_help_text, f'Expected "Target Help" not in {target_help_text}'
        assert context.driver.find_element(By.CSS_SELECTOR, ".search-input").is_displayed()
        assert context.driver.find_element(By.XPATH,
                                           "//input[@class='search-input']/following-sibling::input[@alt='search']").is_displayed()
        assert context.driver.find_element(By.CSS_SELECTOR, ".box-column").is_displayed()
        assert context.driver.find_element(By.CSS_SELECTOR, ".salesforceBox").is_displayed()
        contact_recalls = context.driver.find_elements(By.CSS_SELECTOR, ".boxSmallr")
        assert len(contact_recalls) == 2, f'Expected 2 does not equal {len(contact_recalls)}'
        assert context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']").is_displayed()
