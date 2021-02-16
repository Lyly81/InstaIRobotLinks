from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

class PopupFollowers:

	def __init__(self, driver):
		self.driver = driver

	"""This method is for click on the button followers for open popup.
	"""
	def btnFollowers(self):
		# Select followers' button
		try:
			flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')))
			flw_btn.click()
			time.sleep(random.uniform(2, 10))
		except:
			pass
