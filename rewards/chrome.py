from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Prompt the user to enter their email and password
email = "saikr2005@gmail.com"
password = input('Enter your password: ')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Bing Rewards login page
driver.get('https://login.live.com')

# Wait for the page to load
time.sleep(2)

# Find the email input element and enter the email
email_input = driver.find_element_by_name('loginfmt')
email_input.send_keys(email)

# Click the Next button
email_input.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Find the password input element and enter the password
password_input = driver.find_element_by_name('passwd')
password_input.send_keys(password)

# Click the Sign in button
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Navigate to the Bing Rewards dashboard
driver.get('https://rewards.microsoft.com/dashboard')

# Wait for the page to load
time.sleep(2)

# Find the Points Breakdown link and click it
points_breakdown_link = driver.find_element_by_link_text('Points breakdown')
points_breakdown_link.click()

# Wait for the Points Breakdown page to load
time.sleep(2)

# Find the points breakdown table and print its contents
points_breakdown_table = driver.find_element_by_class_name('details-list')
print(points_breakdown_table.text)

# Close the browser
driver.quit()
