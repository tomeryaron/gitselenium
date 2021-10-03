##########################################
####   Devops Course 4th Assignment   ####
##########################################
from time import sleep
# Task 1
# Write a script which will open the following:
from selenium import webdriver
chrome_driver = webdriver.Chrome(executable_path="/Users/tomeryaron/Downloads/chromedriver")
ynet = chrome_driver.get("https://ynet.co.il")

# Task 2
# Create a variable with the website’s title
ynettitle = chrome_driver.title
# Refresh website
chrome_driver.refresh()
# Get website name and compare it to the variable you created in clause 1.
if ynettitle == chrome_driver.title:
    print("equal")

# Task 3
# couldnt work with firefox from mac

# Task 4
translate = chrome_driver.get("https://translate.google.com")
chrome_driver.find_element_by_xpath('//*[@aria-label="Source text"]').send_keys("dsf")

# Task 5
# open youtube web page type song name click on search
youtube = chrome_driver.get("https://youtube.com")
sleep(5)
chrome_driver.find_element_by_xpath('//*[@title="Explore"]').click()
chrome_driver.find_element_by_xpath('//input[@id="search"]').send_keys("coldplay viva la vida")
chrome_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()

# Task 7
# Facebook Login
facebook = chrome_driver.get("https://facebook.com/login/")
chrome_driver.find_element_by_xpath('//input[@id="email"]').send_keys("stammail@gmail.com")
chrome_driver.find_element_by_xpath('//input[@id="pass"]').send_keys("sismashona")
#chrome_driver.find_element_by_xpath('//button[@id="loginbutton"]').click()

# Task 8
# Cookies challenge
facebook = chrome_driver.get("https://facebook.com/login/")
chrome_driver.delete_all_cookies()
print(chrome_driver.get_cookies())
