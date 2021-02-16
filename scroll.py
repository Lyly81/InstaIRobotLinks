from selenium import webdriver
import time
import random
from datetime import date

"""This is the class for scrolling.
"""
class Scroll():

    def __init__(self, driver):
        self.driver = driver
        self.scrollScript = """
			document.getElementsByClassName('isgrP')[0].scroll(0, 85000)
        """
        self.scroll = 0

    """This method is for scrolling in the popup.
    """
    def scrolling(self, nbScroll):
        while (self.scroll != nbScroll):
            self.driver.execute_script(self.scrollScript)
            time.sleep(random.uniform(2, 10))
            self.scroll += 1
