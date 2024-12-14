import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# Set up Chrome options
options = Options()
# options.add_argument("--headless")        # This will run program in headless mode

service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)

# Setup maximize window and implicit wait
driver.implicitly_wait(10)
driver.maximize_window()

# Get mentioned url
driver.get("https://the-internet.herokuapp.com/")

# Click on the Frames linktext
driver.find_element(
    By.LINK_TEXT, "Frames").click()

wait = WebDriverWait(driver, 10)

# click on the nested frames
wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "Nested Frames"))).click()
driver.back()

# Click on iFrame
wait.until(
    EC.presence_of_element_located((By.LINK_TEXT, "iFrame"))).click()
time.sleep(2)

# Find frames
time.sleep(4)
driver.switch_to.frame("mce_0_ifr")

# select textbox and enter new text to it
driver.find_element(By.XPATH, "//p").clear()
time.sleep(3)
#driver.find_element(By.ID, "tinymce").send_keys("Hey, here automation tester is availabe for your help!")

# Close driver
driver.close()

print("Good work, keep it up!")