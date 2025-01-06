from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://the-internet.herokuapp.com/dynamic_controls"

# instantiate webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(url)

#defining a wait
wait = WebDriverWait(driver, 10)

# find the enable button
enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
enable_button.click()
sleep(3)

# find the disable button
disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
disable_button.click()
sleep(3)

# find the remove button
remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
remove_button.click()
sleep(3)

# find the add button
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
add_button.click()
sleep(3)

# find the checkbox
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox"]')))
checkbox.click()
sleep(3)

driver.quit()