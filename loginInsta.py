from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

"""This the class for connect to Instagram account.
"""
class LoginInsta:

	def __init__(self, driver, userInsta, pwdInsta):
		self.driver = driver
		self.userInsta = userInsta
		self.pwdInsta = pwdInsta

	"""This method is for accept cookies.
	"""
	def cookies(self):
		self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
		
		try:
			btncookies = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[1]')))
			time.sleep(random.uniform(2, 10))
			btncookies.click()
		except:
			pass

	"""This method is for login to Instagram account.
	"""
	def signing(self):
		user = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
		user.click()
		user.send_keys(self.userInsta)
		time.sleep(random.uniform(2, 10))

		pwd = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
		pwd.click()
		pwd.send_keys(self.pwdInsta)
		time.sleep(random.uniform(2, 10))

		btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
		btn.click()
		time.sleep(random.uniform(2, 10))

	"""This method is for click on the first button later.
	"""
	def later1(self):
		btnlater1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')))
		btnlater1.click()
		time.sleep(random.uniform(2, 10))

	"""This method is for click on the second button later.
	"""
	def later2(self):
		time.sleep(random.uniform(2, 10))
		btnlater2 = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]/div/div/div[3]/button[2]')))
		btnlater2.click()
		time.sleep(random.uniform(2, 10))
