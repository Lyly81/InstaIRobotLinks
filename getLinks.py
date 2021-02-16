from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import random
from datetime import date
import database
import scroll
import popupFollowers

""" This class is for get followers'links on the profile account.
"""
class GetLinks():
	
	def __init__(self, driver):
		self.driver = driver
		self.sql_links = """
			SELECT * FROM links
		"""
		self.sql_insert_link = """
			INSERT INTO links (link, created_at) 
			VALUES (%s, %s)
		"""

	"""This method is for get the links of instagram account when the database is not empty.
	"""
	def getLinksFollowers(self):
		# Get links in database
		connDB = database.Database()
		sqll = connDB.queryFetchall(self.sql_links)
		data_links = list(sqll)

		# Put the link in list for compare
		list_link = []

		# Get all links of database and put in the list
		for y in data_links:
			list_link.append(y[1])

		for linky in data_links:
			# Select public account
			if linky[3] == 'Public':
				# Select link for open page web
				try:
					self.driver.get(linky[1])
				except:
					continue
				time.sleep(random.uniform(2, 10))

				try:
					# Select followers' button
					popupFollows = popupFollowers.PopupFollowers(self.driver)
					popupFollows.btnFollowers()
				except:
					err = self.driver.find_elements_by_xpath('/html/body/div/div[1]/div/div/p').text
					if err == 'Veuillez patienter quelques minutes avant de réessayer.':
						time.sleep(random.uniform(300, 600))

				# Execute scroll on the followers' popup
				try:
					scrolly = scroll.Scroll(self.driver)
					scrolly.scrolling(70)
				except:
					continue

				try:
					a = self.driver.find_elements_by_xpath('.//div[@role="dialog"]//a[@style="width: 30px; height: 30px;"]')
				except:
					a = self.driver.find_elements_by_xpath('.//div[@role="dialog"]//a')

				for l in a:
					try:
						link = l.get_attribute('href')
					except:
						pass			
					# time.sleep(random.uniform(3, 10))

					if link not in list_link:
						data_links.append(link)
						# Prepare request
						link_dict = (link, date.today())

						# Request for insert new link
						reqAddLink = database.Database()
						reqAddLink.queryInsert(self.sql_insert_link, link_dict)
					else:
						continue
				else:
					continue
		self.getLinksFollowers()
