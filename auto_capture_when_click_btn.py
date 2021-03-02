import pyautogui
import PIL
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageDraw
from io import BytesIO
from datetime import datetime
import pytest

OFFSET_ELEMENT = 10
# Create new Chrome
driver = webdriver.Chrome()
base_path = 'C:\\Users\\VMO-PHUCH\\Desktop\\Evidence\\'


def screenshot():
	return driver.get_screenshot_as_png()
	

def draw_rectangle(element):
	# Get location
	location = element.location
	# Get size
	size = element.size
	# Screenshot
	png = screenshot()
	# Open image
	img = Image.open(BytesIO(png))
	# Find coordinates of element
	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']
	# Draw red rectangle
	red_frame = ImageDraw.Draw(img)
	red_frame = red_frame.rectangle((left - OFFSET_ELEMENT, top - OFFSET_ELEMENT, right + OFFSET_ELEMENT, bottom + OFFSET_ELEMENT), outline ="red", width=4)
	# img.save(file_name)
	return img

def get_file_name_by_time():
	timestr = time.strftime("%Y%m%d%H%M%S")
	return base_path + 'screenshot_' + timestr + '.png'

def test_search_python():
	# Get path
	path = get_file_name_by_time()
	# Navigate to Python homepage
	driver.get('https://www.python.org/')
	# Check result
	assert "Python" in driver.title
	# Set maximum screen
	driver.maximize_window()
	time.sleep(3)
	# Determine search box
	search_box = driver.find_element_by_id('id-search-field')
	# Send key which want to search
	search_box.send_keys('pytest')
	time.sleep(1)
	# Draw red rectangle arround search box
	draw_rectangle(search_box).save(path)
	# Determine search button
	search_btn = driver.find_element_by_id('submit')
	time.sleep(1)
	# Get path
	path = get_file_name_by_time()
	# Draw red rectangle arround search button
	draw_rectangle(search_btn).save(path)
	# Click button search
	search_btn.click()
	# assert that result is found
	assert "No results found." not in driver.page_source
	# Make avidence
	path = get_file_name_by_time()
	png = screenshot()
	img = Image.open(BytesIO(png))
	img.save(path)
	# Quit Chrome
	driver.quit()




# if __name__ == "__main__":
# 	search_python()