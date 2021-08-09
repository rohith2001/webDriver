from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import emoji
#print(emoji.emojize(":red_heart:"))

import googletrans
from googletrans import Translator
translator = Translator()
#thisdict=googletrans.LANGUAGES

#new_list = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'fil', 'he']
#lang_list = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Filipino', 'Hebrew']
#total_list=[['af', 'afrikaans'], ['sq', 'albanian'], ['am', 'amharic'], ['ar', 'arabic'], ['hy', 'armenian'], ['az', 'azerbaijani'], ['eu', 'basque'], ['be', 'belarusian'], ['bn', 'bengali'], ['bs', 'bosnian'], ['bg', 'bulgarian'], ['ca', 'catalan'], ['ceb', 'cebuano'], ['ny', 'chichewa'], ['zh-cn', 'chinese (simplified)'], ['zh-tw', 'chinese (traditional)'], ['co', 'corsican'], ['hr', 'croatian'], ['cs', 'czech'], ['da', 'danish'], ['nl', 'dutch'], ['en', 'english'], ['eo', 'esperanto'], ['et', 'estonian'], ['tl', 'filipino'], ['fi', 'finnish'], ['fr', 'french'], ['fy', 'frisian'], ['gl', 'galician'], ['ka', 'georgian'], ['de', 'german'], ['el', 'greek'], ['gu', 'gujarati'], ['ht', 'haitian creole'], ['ha', 'hausa'], ['haw', 'hawaiian'], ['iw', 'hebrew'], ['hi', 'hindi'], ['hmn', 'hmong'], ['hu', 'hungarian'], ['is', 'icelandic'], ['ig', 'igbo'], ['id', 'indonesian'], ['ga', 'irish'], ['it', 'italian'], ['ja', 'japanese'], ['jw', 'javanese'], ['kn', 'kannada'], ['kk', 'kazakh'], ['km', 'khmer'], ['ko', 'korean'], ['ku', 'kurdish (kurmanji)'], ['ky', 'kyrgyz'], ['lo', 'lao'], ['la', 'latin'], ['lv', 'latvian'], ['lt', 'lithuanian'], ['lb', 'luxembourgish'], ['mk', 'macedonian'], ['mg', 'malagasy'], ['ms', 'malay'], ['ml', 'malayalam'], ['mt', 'maltese'], ['mi', 'maori'], ['mr', 'marathi'], ['mn', 'mongolian'], ['my', 'myanmar (burmese)'], ['ne', 'nepali'], ['no', 'norwegian'], ['ps', 'pashto'], ['fa', 'persian'], ['pl', 'polish'], ['pt', 'portuguese'], ['pa', 'punjabi'], ['ro', 'romanian'], ['ru', 'russian'], ['sm', 'samoan'], ['gd', 'scots gaelic'], ['sr', 'serbian'], ['st', 'sesotho'], ['sn', 'shona'], ['sd', 'sindhi'], ['si', 'sinhala'], ['sk', 'slovak'], ['sl', 'slovenian'], ['so', 'somali'], ['es', 'spanish'], ['su', 'sundanese'], ['sw', 'swahili'], ['sv', 'swedish'], ['tg', 'tajik'], ['ta', 'tamil'], ['te', 'telugu'], ['th', 'thai'], ['tr', 'turkish'], ['uk', 'ukrainian'], ['ur', 'urdu'], ['uz', 'uzbek'], ['vi', 'vietnamese'], ['cy', 'welsh'], ['xh', 'xhosa'], ['yi', 'yiddish'], ['yo', 'yoruba'], ['zu', 'zulu'], ['fil', 'Filipino'], ['he', 'Hebrew']]


PATH = "C:\Program Files (x86)\chromedriver.exe"
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Rahul"'

# Replace the below string with your own message
string = ""

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))


'''
for i in range(100):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1) 

'''
#new_list=[]
#lang_list=[]
# to get new_list and lang_list
'''
for x,y in thisdict.items():
	new_list.append(x)
	lang_list.append(y)
print(lang_list)
'''
'''
for listz in total_list:
	translated = translator.translate("Hii", src="en", dest=listz[0])
	input_box.send_keys(translated.text+
	str(emoji.emojize(":victory_hand:"))+
	str(" ->"+listz[1])+Keys.ENTER)
#print(emoji.emojize(":victory_hand:")) '''
for count in range(100):
	input_box.send_keys("hii "+"❤"+" "+str(count+1)+Keys.ENTER)
'''
total_list=[]
for x,y in thisdict.items():
	s=[x,y]
	total_list.append(s)
print(total_list)
'''

#testing
#print(total_list[0][0]+total_list[0][1])
#Testing our data
#print(new_list[0]+" "+lang_list[0])
#translated = translator.translate("i love you",src="en",dest=new_list[0])
#print(translated)
time.sleep(3)
driver.quit()