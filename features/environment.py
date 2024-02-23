from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context 
    """
    # user_name = 'nikitaboulatov_3aQief'
    # access_key = 'dzYRgSkNqt4AZvzTfKDF'
    # browser_stack_url = f'http://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # browser_stack_options = {
    #     'os': 'Windows',
    #     'osVersion': 10,
    #     'browserName': 'Chrome',
    #     'sessionName': 'Target Search'
    # }
    # options.set_capability('bstack:options', browser_stack_options)
    # context.driver = webdriver.Remote(command_executor=browser_stack_url, options=options)

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step.name)

def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f"{step.name}_test.png")
        print('\nStep failed: ', step.name)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
