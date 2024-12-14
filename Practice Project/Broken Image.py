from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

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

try:
    # click on the broken image
    driver.find_element(
        By.LINK_TEXT, "Broken Images").click()
    time.sleep(7)

    # verificaiton that broken image text is present or not on webpage
    assert driver.find_element(By.TAG_NAME, "h3").text == "Broken Images"

    # Verify that below elements are present or not
    driver.find_element(
        By.XPATH, "//div[@id='content']/div/img[1]").is_displayed()
    driver.find_element(
        By.XPATH, "//div[@id='content']/div/img[2]").is_displayed()
    driver.find_element(
        By.XPATH, "//div[@id='content']/div/img[3]").is_displayed()

    driver.back()

except:
    driver.close()

print("Success")


