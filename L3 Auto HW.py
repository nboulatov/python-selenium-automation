from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26pf_rd_p%3D8b17d5d4-f780-4476-bbb4-5d216813632d%26pd_rd_wg%3DEQNBF%26pf_rd_r%3DJKPZCDKRGQMFJATTCCHR%26content-id%3Damzn1.sym.8b17d5d4-f780-4476-bbb4-5d216813632d%26pd_rd_w%3DmCCtv%26pd_rd_r%3D33a50662-fd12-4ede-9577-44d263e00c57&openid.assoc_handle=anywhere_v2_us")
driver.maximize_window()

amazon_logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo")
create_account_text = driver.find_element(By.XPATH, "//a[@id='register_accordion_header']/h5/div/span[text()='Create account']")
first_last_name = driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
email_phone = driver.find_element(By.CSS_SELECTOR, "#ap_email")
password = driver.find_element(By.CSS_SELECTOR, "#ap_password")
# There is no re-enter password element on the webpage
continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
conditions_of_use_link = driver.find_element(By.XPATH, "//div[@id='legal-section']/div/a[text()='Conditions of Use']")
privacy_notice_link = driver.find_element(By.XPATH, "//div[@id='legal-section']/div/a[text()='Privacy Notice']")
sign_in_link = driver.find_element(By.XPATH, "//a[@id='login_accordion_header']/h5/div/span[text()='Sign in']")

driver.quit()
