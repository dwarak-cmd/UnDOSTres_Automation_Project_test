# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:21:26 2021

@author: Admin
"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
# from selenium.webdriver import ActionChains
# import pandas as pd
# import glob
# import os
import pyautogui

#chrome driver path
web_link=r"E:\chromedriver_win32\chromedriver.exe"

#Invoke browser
options = Options()
driver = webdriver.Chrome(chrome_options = options, executable_path=web_link)
driver.get('http://sanbox.undostres.com.mx')
print("Chrome Browser Invoked")

#find xpath for each element and proceed to click
# driver.find_element_by_xpath("//*[@id='suggested']").click()
# time.sleep(2)

#Below code for typing 
search = driver.find_element_by_xpath('//html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/input').click()
# driver.find_element_by_xpath('xpath').clear()
# search.send_keys('Telcel')
driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/div/ul/li[1]/a').click()
time.sleep(2)


number = driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[2]/div/div/input')
number.send_keys('8465433546')


driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/input').click()
driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/div/ul[1]/li[1]/a/div[2]').click()


driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[3]/div/button').click()

driver.find_element_by_xpath('//*[@id="new-card-toggle"]/div/div').click()

time.sleep(2)
driver.find_element_by_xpath('/html/body/div[32]/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr[1]/td/label').click()
time.sleep(2)

card = driver.find_element_by_xpath('//*[@id="cardnumberunique"]')
card.send_keys('4111111111111111')

month = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[1]/div/div[1]/input')
month.send_keys('11')

date = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[1]/div/div[3]/input')
date.send_keys('25')

cvv = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[2]/div/input')
cvv.send_keys('111')

mail = driver.find_element_by_xpath('//*[@id="payment-form"]/div[4]/div/div/input')
mail.send_keys('test@test.com')

driver.find_element_by_xpath('//*[@id="paylimit"]/span').click()

time.sleep(2)

mailid = driver.find_element_by_xpath('//*[@id="usrname"]').click()
mailid = driver.find_element_by_xpath('//*[@id="usrname"]')
mailid.send_keys('automationUDT1@gmail.com')

pwd = driver.find_element_by_xpath('//*[@id="psw"]')
pwd.send_keys('automationUDT123')

pyautogui.position()
time.sleep(5)
pyautogui.moveTo(786,891)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(1044,1007)
pyautogui.click()
