from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# defining the url
url = "http://dhtmlgoodies.com/scripts/drag-and-drop-custom/demo-drag-drop-3.html"

# instantiate webdriver and open a chrome tab
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(url)

# find the source
source = driver.find_element(By.XPATH, '//*[@id="box3"]')

# find the destination
destination = driver.find_element(By.XPATH, '//*[@id="box103"]')

# instantiate actionchains
actions = ActionChains(driver)

# perform drag and drop - dragging from source and dropping to destination
actions.drag_and_drop(source, destination).perform()

# pause the program
sleep(5)

driver.quit()


