import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
wait=WebDriverWait(driver, 4)

element_to_scroll_to = wait.until(EC.visibility_of_element_located((By.XPATH, '//legend[text()="iFrame Example"]')))
driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)
driver.switch_to.frame(driver.find_element(By.ID,'courses-iframe'))
wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="new-navbar-highlighter"]'))).click()
time.sleep(3)


driver.quit()