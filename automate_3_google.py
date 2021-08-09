import selenium
import googletrans
from googletrans import Translator
thisdict=googletrans.LANGUAGES
print(len(thisdict))

# to get  the x and y values
for x,y in thisdict.items():
    print(x)
import time
#from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
search=driver.find_element_by_name("q")
search.send_keys("google translator" + Keys.ENTER)
input_language = driver.find_element_by_class_name("source-language")
input_language.click()
inp_xpath = '//div[@class="language_list_item"]'
wait = WebDriverWait(driver, 600)
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
for i in input_box.text:
    print(i)
driver.quit() '''