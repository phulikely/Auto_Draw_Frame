import pyautogui
import PIL
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageDraw
from io import BytesIO

OFFSET_ELEMENT = 10

def snap_shot():
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'C:\Users\VMO-PHUCH\Desktop\screenshot1.png')
	

def search_python():
	# Create new Chrome
	driver = webdriver.Chrome()
	# Navigate to Python homepage
	driver.get('https://www.python.org/')
	# Set maximum screen
	driver.maximize_window()
	time.sleep(3)
	# Determine search box
	search_box = driver.find_element_by_id('id-search-field')
	# Send key which want to search
	search_box.send_keys('pytest')
	# Determine search button
	search_btn = driver.find_element_by_id('submit')
	time.sleep(1)

	# Get location
	location = search_box.location
	# Get size
	size = search_box.size
	# Screenshot
	png = driver.get_screenshot_as_png()
	driver.quit()

	# Open image
	img = Image.open(BytesIO(png))
	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']

	#img = img.crop((left, top, right, bottom))
	img1 = ImageDraw.Draw(img)
	img1 = img1.rectangle((left - OFFSET_ELEMENT, top - OFFSET_ELEMENT, right + OFFSET_ELEMENT, bottom + OFFSET_ELEMENT), outline ="red", width=4)
	img.save(r'C:\Users\VMO-PHUCH\Desktop\screenshot1.png')


if __name__ == "__main__":
	search_python()