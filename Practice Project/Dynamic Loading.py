from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
# options.add_argument('--headless')  # Run in headless mode

# setting up driver object
service_obj = Service(executable_path=
                      "D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)

# maximaxe window and apply implicit wait
driver.maximize_window()
driver.implicitly_wait(10)

# get the url
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

wait = WebDriverWait(driver, 10)

try:
    # Click on the Dynamic Loading link
    driver.find_element(
        By.LINK_TEXT, "Dynamic Loading").click()
    time.selep(2)

    # Click on the Element 1
    driver.find_element(
        By.LINK_TEXT, "Example 1: Element on page that is hidden").click()
    time.sleep(2)

    # Click on the start button
    driver.find_element(
        By.XPATH, "//div[@id='start']/button").click()
    time.sleep(5)

    # verify the text after cliking on the start button
    assert driver.find_element(By.XPATH, "//div[@id='finish']/h4").text == "Hello World!"

    # click on back button
    driver.back()
    # Click the Element 2 link
    driver.find_element(
        By.LINK_TEXT, "Example 2: Element rendered after the fact").click()
    time.sleep(2)

    # Click on hte start button
    driver.find_element(
        By.XPATH, "//div[@id='start']/button").click()
    time.sleep(5)

    # Verify text
    assert driver.find_element(By.XPATH, "//div[@id='finish']/h4").text == "Hello World!"
    time.sleep(2)

except:
    driver.close()

print("Success!")