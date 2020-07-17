import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")

browser = webdriver.Chrome(executable_path = "./chromedriver", options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")


with open('message.txt', 'r') as msg:
    message = msg.read()
    
    
with open('links.txt') as links:
    links_array = links.readlines()

for link in links_array:
    browser.get(link)
    msg = browser.find_element_by_id("composerInput")
    msg.send_keys(message + "\n\nTimestamp: " + str(time.ctime()))
    button = browser.find_element_by_xpath("//*[@value='Send']")
    button.click()
    time.sleep(5)
