import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

# Goto below URL
driver.get("https://the-internet.herokuapp.com/")

try:
    # Click on the Entry Ad link
    driver.find_element(
        By.LINK_TEXT, "Entry Ad").click()

    # Explicit wait
    wait = WebDriverWait(driver, 10)

    # Click on the close button of appeared popup
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='modal']/div[3]"))).click()
    time.sleep(2)

    print("alert accepted")

    # Click on the click here button
    driver.find_element(By.LINK_TEXT, "click here").click()

    assert driver.find_element(By.LINK_TEXT, "click here").text == "click here"

except:
    # Click on close button
    driver.close()

print("Program executed successfully!")