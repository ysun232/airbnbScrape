#Webscraping for airbnb infinite scrolling

import bs4 as bs
import urllib.request
import ssl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
#import sys
#works, but the chrome driver crashes, and I cant extract the data from the website


driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
#new little addition to maximize window when you open it to get the maximum number of results per page scrolling
driver.maximize_window()
url = "https://www.airbnb.com/s/homes"
#now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
driver.get(url)
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
a = "PLUS"

#defining empty lists so that I can append to the lists through iteration later
title_list = []
descrip_list = []
price_list = []
time_taken = []
#lets the first load be a little longer, more elements, diminishes the chances of not being able to trace an element
time.sleep(40)
#need to add a couple of scrolling through pages since the div we want is not appearing when the page is first loaded
for t in range(0,3) :
    time.sleep(15)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#without scrolling 3 or 4 times, the div[8] is not reacheable, I can probably go even more in detail,
#but div[8] is good enough to find the title of each house.
#the website changes the path from time to time so need to update it.
global_div = driver.find_element_by_xpath('//*[@id="site-content"]/div/div/div[3]/div/div/div/div/div[8]')

descrip_div = global_div.find_elements_by_xpath(".//div[contains(@class, '_36rlri')]")
title_div = global_div.find_elements_by_class_name("_1xxanas2")
#for some reason, if its inside a div, cant find element by class name, had to switch to the more general use
#of find element by xpath, finds the xpath for descrip_div SOMETIMES ONLY - solution
# with slower internet, the element does not load fast enough sometimes, so I cannot track what is not loaded
price_div = global_div.find_elements_by_class_name("_1jlnvra2")

#using an iteration for scrolling through the webpage as to obtain all of the results
for u in range(0,10):
    time.sleep(15)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



    #through each scrolling of webpage, I will append to the list for the different elements.
    for x1 in title_div:
        if x1.text == a or x1.text == '':
            continue
        title_list.append(x1.text)

    for x2 in descrip_div[::2]:
        descrip_list.append(x2.text)

    for x3 in price_div[::2]:
        price_list.append(x3.text)
        time_taken.append(now)

driver.close()

list_of_lists =[title_list, price_list, descrip_list, time_taken]
oldArr = (list_of_lists)
size = len(oldArr[1])
newArr = []
for i in range(size):
    newArr.append([])
for i,val in enumerate(oldArr):
    for index,value in enumerate(val):
        newArr[index].append(value)

newTuple = tuple(newArr)
print (newTuple)