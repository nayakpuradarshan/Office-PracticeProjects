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

try:
    # Click on the Form Authentication
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    wait = WebDriverWait(driver, 10)

    # wait till username id locate on web browser and once located click on that element
    wait.until(
        EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")

    # Click on the password field
    driver.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")

    # Click on the login button
    time.sleep(1)
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(2)

    # Variable created assigned text to it
    secureText =  wait.until(EC.presence_of_element_located((By.XPATH, "//h4"))).text
    print("secureText:", secureText)

    # assertion to verify text
    assert secureText == "Welcome to the Secure Area. When you are done click logout below."
    print("assertion match!")

    # Click on the logout button
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@class='button secondary radius']").click()
    time.sleep(2)

except:
    # Close browser tab
    driver.close()
    print("Program executed successfully!")
