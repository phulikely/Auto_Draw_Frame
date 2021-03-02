#pip install chromedriver-binary-auto
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Vi la co class nen phai co method __init__
# Vi la co class nen param phai co self
class Get_Weather():

	def __init__(self):
		pass

	def get_city_weather(self,city):
		dict_weather = {}
		driver = webdriver.Chrome()
		driver.get("https://weather.com/vi-VN/weather/today/l/VMXX0006:1:VM")
		time.sleep(3)
		search_box = driver.find_element_by_id('LocationSearch_input')
		search_box.send_keys(city)
		time.sleep(3)
		search_box.send_keys(Keys.ENTER)
		time.sleep(5)
		not_found = driver.find_element_by_xpath('//header/div/div[2]/div/div/div[2]/div')
		if not_found.text != 'Không tìm thấy kết quả nào':
			name = driver.find_element_by_xpath('//a[2]/span')
			print(name.text)
			dict_weather['name'] = name.text
			temp = driver.find_element_by_xpath('//a[1]/span')
			print(temp.text)
			dict_weather['temp'] = temp.text
			humidity = driver.find_element_by_xpath('//div[3]/div[2]/span')
			print(humidity.text)
			dict_weather['humidity'] = humidity.text
			time.sleep(5)
			driver.quit()
		else:dict_weather = None

		return dict_weather

# if __name__ == "__main__":
# 	print(get_city_weather('Hưng Yên'))