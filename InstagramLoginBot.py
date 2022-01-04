# Selenium Tutorial #1
# https://sites.google.com/a/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

ser = Service("C:\Program Files (x86)\chromedriver.exe")
op = webdriver.ChromeOptions()

username = input("Enter Instagram Username: ")
pw = input("Enter Instagram Password: ")

class GoogleBot:

	def __init__(self, r, username, pw):
		self.s = webdriver.Chrome(service=ser, options=op)
		self.s.get("https://www.google.com/search?q=" + r + "&start")
		self.s.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a/h3')\
		.click()
		sleep(2)
		self.s.find_element_by_xpath("//input[@type=\"text\"]")\
		.send_keys(username)
		self.s.find_element_by_xpath("//input[@type=\"password\"]")\
		.send_keys(pw)
		self.s.find_element_by_xpath("//button[@type=\"submit\"]")\
		.click()


GoogleBot('instagram',username,pw)
