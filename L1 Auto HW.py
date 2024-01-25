from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 1. Practice with locators.
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.maximize_window()
time.sleep(10)
amazon_logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").text
email_field = driver.find_element(By.XPATH, "//input[@id='ap_email']").text
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']").text
conditions_of_use = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]").text
privacy_notice = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice')]").text
need_help = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").text
forgot_your_password = driver.find_element(By.XPATH, "(//a[normalize-space()='Forgot your password?'])[1]").text
# Where is this text (other_issues_with_sign_In)? I do not see it on the website. As you can tell from the above/below code, I have the understanding of xpath creation process. I do not want to loose points for something I do not see on the page. Please consider this before grading. Thank you.
create_your_cmazon_account = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']").text

# 2. Create a test case for the SignIn page using python & selenium script.
driver.get("https://www.target.com/") # 1. Open https://www.target.com/
driver.maximize_window()
driver.find_element(By.XPATH, "//span[text()='Sign in']").click() # 2. Click SignIn button
time.sleep(3)
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click() # 2. Click SignIn button
time.sleep(3)
text_to_verify = 'Target account'
sign_in_text = driver.find_element(By.XPATH, "//span[normalize-space()='Sign into your Target account']").text # “Sign into your Target account” text is shown
driver.find_element(By.XPATH, "//button[@id='login']") # SignIn button is shown (you can just use driver.find_elemennt() to check for element’s presence, no need to assert here)
assert text_to_verify in sign_in_text f'Expected {text_to_verify} not in {sign_in_text}'

# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.
driver.get("https://www.target.com/") # 1. Open https://www.target.com/
driver.maximize_window()
product = 'coffee'
driver.find_element(By.ID, "search").send_keys(product)
driver.find_element(By.XPATH, "//button[normalize-space()='search']").click()
time.sleep(3)
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']/span[contains(text(), 'coffee')]").text
assert product in actual_text
driver.quit()