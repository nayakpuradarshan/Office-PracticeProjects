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

# click on the checkboxes
driver.find_element(
    By.LINK_TEXT, "Checkboxes").click()
time.sleep(5)

# click on the checkbox
driver.find_element(
    By.XPATH, "//div[@id='content']/div/form/input[1]").click()
driver.find_element(
    By.XPATH, "//div[@id='content']/div/form/input[2]").is_selected()
    
time.sleep(4)

driver.close()
print("\nsucccess")