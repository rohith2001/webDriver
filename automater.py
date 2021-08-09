import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.get("https://www.google.com/")
#search=driver.find_element_by_name("q")
#search.send_keys("whatsapp web")
#search.send_keys(Keys.RETURN)
#a= driver.find_element_by_class_name("LC20lb DKV0Md")
#a.click()
#search = driver.find_element_by_name("q")
#search.send_keys("whatsapp web")
#search.send_keys(Keys.RETURN)

'''try:
   main= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"fld")))
    articles = main.find_elements_by_tag_name("article")
except:
    driver.quit() 

print(main.text) '''

driver.get("https://web.whatsapp.com/")


name = input("enter name")
msg = input("type msg")
count = int(input("Enter count"))

input("Enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name("_3FRCZ copyable-text selectable-text")
for i in range(count):
    msg_box.send_keys(msg)
    msg.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()