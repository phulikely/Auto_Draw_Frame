import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Selenium Testing")
time.sleep(1)
#driver.find_element_by_name("btnK").click()
driver.find_element_by_name("btnK").click()
#element.click() 
time.sleep(1)
driver.close()