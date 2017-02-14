from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:3000')

assert  'Djnago' in browser.title

