from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select

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
    "This block will check the web element of the internet page"

    # open dropdown manu
    driver.find_element(
        By.LINK_TEXT, "Dropdown").click()
    time.sleep(3)

    # click on the dropdown menu
    select = Select(
        driver.find_element(By.ID, "dropdown"))

    select.select_by_visible_text("Option 2")                     # you may find web element using the webtext
    time.sleep(3)

    select.select_by_index(1)                                     # you may find web element using the index value
    time.sleep(3)

except:
    driver.close()

print("success")