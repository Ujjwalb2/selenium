import selenium
import os
import time
import csv
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
option_ = webdriver.Chrome()

url = 'https://opstra.definedge.com/'
option_.get(url)
time.sleep(4)
searching_element = option_.find_element(By.XPATH, '//*[@id="app"]/div[2]/nav/div/div[4]/button/div')
searching_element.click()
searching_element1 = option_.find_element(By.XPATH, '//*[@id="username"]')
searching_element1.send_keys("Email id")
searching_element2 = option_.find_element(By.XPATH, '//*[@id="password"]')
searching_element2.send_keys("Password")
searching_element3 = option_.find_element(By.XPATH, '//*[@id="kc-login"]')
searching_element3.click()
option_.get('https://opstra.definedge.com/strategy-builder')
time.sleep(4)
searching_element4 = option_.find_element(By.XPATH, '//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[1]/div[1]')
time.sleep(4)
searching_element4.click()
searching_element5 = option_.find_element(By.XPATH, '//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[1]/div[2]/button/div')
searching_element5.click()

option_chain = option_.find_elements(By.CLASS_NAME, 'v-btn__content')
option_data = []
for chain in option_chain:
    Call_Ltp = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[1]')
    ITM_prob = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[2]')
    Call_IV = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[3]')
    Call_delta = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[4]')
    Strike_price = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[5]')
    Put_delta = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[6]')
    Put_IV = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[7]')
    ITM_probs = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[8]')
    Put_LTP = chain.find_element(By.XPATH,'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[2]/div/div/div/div[1]/table/thead/tr[1]/th[9]')
    option_item = {
        'StrikePrice': Strike_price.text,
        'Call_Ltp': CallLtp.text,
        'ITM_Prob': ITM_prob.text,
        'Call_IV': CallIV.text,
        'Call_Delta': Call_delta.text,
        'Put_Delta': Put_delta.text,
        'Put_IV': PutIV.text,
        'ITM_Prob.': ITM_probs.text,
        'Put_Ltp': PutLTP.text

    }
    option_data.append(option_item)

data = pd.DataFrame(option_data)
print(data)
file = 'data.csv'
df.to_csv(file, index=False)
option_.close()
