from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode

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
    "This block of code will check for the dynamic controls"

    # click on the dynamic controls link
    driver.find_element(
        By.LINK_TEXT, "Dynamic Controls").click()
    time.sleep(2)

    # check checkbox
    driver.find_element(
        By.XPATH, "//div[@id='checkbox']/input").click()
    time.sleep(2)

    # Click on remove button
    driver.find_element(
        By.XPATH, "//form[@id='checkbox-example']/button").click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, "//form[@id='checkbox-example']/p").text == "It's gone!"

    # Click on the enable button
    driver.find_element(
        By.XPATH, "//form[@id='input-example']/button").click()
    time.sleep(2)

    # assert enable text after clicking on enable button
    assert driver.find_element(By.XPATH, "//form[@id='input-example']/p").text == "It's enabled!"

    # click on the textbox
    TextBox = driver.find_element(
        By.XPATH, "//form[@id='input-example']/input")
    TextBox.send_keys("James Bond")
    TextBox.send_keys(Keys.RETURN)

except:
    driver.close()

print("Success")