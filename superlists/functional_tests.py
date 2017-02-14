from selenium import webdriver

browser = webdriver.Firefox(fireFox_binary import FirefoxBinary(
         firefox_path='/Users/chesterbeard/downloads/firefox45/firefox'
 )
browser = webdriver.Firefox()
browser.get('http://localhost:3000')

assert  'Django' in browser.title
