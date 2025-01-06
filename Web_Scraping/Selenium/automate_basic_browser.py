from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# defining the url
url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

# instantiate webdriver and open a chrome browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(url)

# find the first name field
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
#fill out the first_name field
first_name.send_keys("Avishek")

# find the last name field
last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
last_name.send_keys("Khatiwada")

# email
email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
email.send_keys("avishek@gmail.com")

# telephone
telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
telephone.send_keys("984343433")

# password
password = driver.find_element(By.XPATH, '//*[@id="input-password"]')
password.send_keys("avishek")

# confirm-password
confirm_password = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
confirm_password.send_keys("avishek")

# newsletter subscribe disagree
newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')
newsletter_subscribe.click()

# newsletter subscribe agree
agree = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div/label')
agree.click()

# continue button
continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')
continue_button.click()

# scroll down by 200 units to view the lower parts of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 secs to view the results
sleep(5)

#close the driver
driver.quit()


