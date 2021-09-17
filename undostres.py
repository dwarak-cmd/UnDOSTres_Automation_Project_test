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

#Below code for typing 
search = driver.find_element_by_xpath('//html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/input').click()
driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/div/ul/li[1]/a').click()
time.sleep(2)

#Entering mobile number 
number = driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[2]/div/div/input')
number.send_keys('8465433546')

#selecting $10 from drop down
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/input').click()
driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/div/ul[1]/li[1]/a/div[2]').click()

#clicking on button
driver.find_element_by_xpath('//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[3]/div/button').click()

#clicking on tarjeta
driver.find_element_by_xpath('//*[@id="new-card-toggle"]/div/div').click()

time.sleep(2)
#clicking on Usar nueva tarjeta
driver.find_element_by_xpath('/html/body/div[32]/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr[1]/td/label').click()
time.sleep(2)

#inputting card number
card = driver.find_element_by_xpath('//*[@id="cardnumberunique"]')
card.send_keys('4111111111111111')

#inputting month
month = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[1]/div/div[1]/input')
month.send_keys('11')

#inputting date
date = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[1]/div/div[3]/input')
date.send_keys('25')

#inputting cvv number
cvv = driver.find_element_by_xpath('//*[@id="payment-form"]/div[3]/div[2]/div/input')
cvv.send_keys('111')

#inputting mail We will send your receipt to this email
mail = driver.find_element_by_xpath('//*[@id="payment-form"]/div[4]/div/div/input')
mail.send_keys('test@test.com')

#clicking on Pagar con tarjeta
driver.find_element_by_xpath('//*[@id="paylimit"]/span').click()

time.sleep(2)

#inputting on correo electronico
mailid = driver.find_element_by_xpath('//*[@id="usrname"]').click()
mailid = driver.find_element_by_xpath('//*[@id="usrname"]')
mailid.send_keys('automationUDT1@gmail.com')

#inputting on contrasena
pwd = driver.find_element_by_xpath('//*[@id="psw"]')
pwd.send_keys('automationUDT123')

#positioning for captcha check box click
pyautogui.position()
time.sleep(5)
pyautogui.moveTo(786,891)

#positioning for access button click
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(1044,1007)
pyautogui.click()
