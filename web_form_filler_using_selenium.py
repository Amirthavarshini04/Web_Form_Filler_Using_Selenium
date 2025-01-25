import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# User data
user_data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@example.com',
    'password': 'SecurePassword123'
}

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get('https://example.com/form')

# Fill out the form fields
driver.find_element(By.NAME, 'firstName').send_keys(user_data['first_name'])
driver.find_element(By.NAME, 'lastName').send_keys(user_data['last_name'])
driver.find_element(By.NAME, 'email').send_keys(user_data['email'])
driver.find_element(By.NAME, 'password').send_keys(user_data['password'])

# Submit the form
driver.find_element(By.NAME, 'submit').click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Close the browser
driver.quit()
