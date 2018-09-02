#! python3

# pip install selenium
# https://chromedriver.storage.googleapis.com/index.html?path=2.40/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import os

browser = webdriver.Chrome(executable_path=os.path.abspath("/Users/Keita/Desktop/src/python/退屈なことはPythonにやらせよう/Web Scraping/chromedriver"))
browser.get('http://104.197.206.76/redmine/')
sleep(1)

elem_id = browser.find_element_by_id('username')
elem_id.send_keys('45008')

elem_pass = browser.find_element_by_id('password')
elem_pass.send_keys('keita1020')
elem_pass.send_keys(Keys.ENTER)

elem_test = browser.find_element_by_id('loggedas')
test = elem_test.text
print(test)

# チケットを作成してみる
browser.get('http://104.197.206.76/redmine/projects/test2/issues/new')
elem_title = browser.find_element_by_id('issue_subject')
elem_title.send_keys('test ticket : ' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

elem_create = browser.find_element_by_name('commit')
elem_create.submit()
