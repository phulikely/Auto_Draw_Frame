from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome(executable_path='../../ChromeDriver/chromedriver.exe')
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

	def test_search_automation(self):
		self.driver.get('https://google.com')
		self.driver.find_element_by_name('q').send_keys('Automation Testing')
		self.driver.find_element_by_name('btnK').click()
		assert 'Automation Testing' in self.driver.page_source

	def test_search_python_for_new_bie(self):
		self.driver.get('https://google.com')
		self.driver.find_element_by_name('q').send_keys('Python for beginner')
		self.driver.find_element_by_name('btnK').click()
		assert 'Python for beginner' in self.driver.page_source

	@classmethod
	def tearDownClass(self):
		self.driver.close()
		self.driver.quit()
		print("Test Completed")

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Phu/Python/Selenium/Report'))