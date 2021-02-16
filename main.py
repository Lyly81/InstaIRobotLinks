from selenium import webdriver
import database
import loginInsta
import getLinks
from datetime import date

userInsta = open('C:/Users/lydia/Desktop/Docs_RNCP_CDA_2020/i_robot_insta_links/sources/username.txt').readline().strip()
pwdInsta = open('C:/Users/lydia/Desktop/Docs_RNCP_CDA_2020/i_robot_insta_links/sources/password.txt').readline().strip()
driver = webdriver.Chrome("C:/Users/lydia/Desktop/Docs_RNCP_CDA_2020/i_robot_insta_links/sources/chromedriver.exe")
sql_links = """
	SELECT *
	FROM links
"""

def main():
	# Connect database
	connDB = database.Database()

	# Select all links from database
	data_links = connDB.queryFetchall(sql_links)

	# Connection Instagram account
	logInsta = loginInsta.LoginInsta(driver, userInsta, pwdInsta)
	logInsta.cookies()
	logInsta.signing()
	logInsta.later1()
	logInsta.later2()

	# Get links
	gl = getLinks.GetLinks(driver)
	gl.getLinksFollowers()


if __name__ == '__main__':
	main()