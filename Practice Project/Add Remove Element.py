import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
# options = Options()
# options.add_argument('--headless')  # Run in headless mode

# setting up driver object
service_obj = Service(executable_path=
                      "D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# maximaxe window and apply implicit wait
driver.maximize_window()
driver.implicitly_wait(10)

# get the url
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

try:
    "This block will check the web element of the internet page"

    # Click on the add remove elements page
    driver.find_element(
        By.LINK_TEXT, "Add/Remove Elements").click()
    time.sleep(5)

    # Click on the add element button
    driver.find_element(
        By.XPATH, "//div[@id='content']/div/button").click()
    time.sleep(3)

    # Verify that delete button is present or not
    assert driver.find_element(By.XPATH, "//button[@class='added-manually']").text == "Delete"

    # Click on the delete button
    driver.find_element(
        By.XPATH, "//button[@class='added-manually']").click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, "//button[@class='added-manually']").text != "Delete"
    time.sleep(2)

except:
    driver.close()

print("success")