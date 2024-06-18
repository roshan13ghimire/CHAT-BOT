from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup
import os,sys,random,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def stockPrice(shareName):
    l = []
    a = "" 
    

    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://www.nepalstock.com.np/")
    time.sleep(3)
    search = browser.find_element(By.TAG_NAME, "input")
    search.send_keys(shareName)
    search.send_keys(Keys.ENTER) 
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    table = soup.find('table',{'class':'table table-striped'})

    date = table.findAll('tr')[0].findAll('th')[0]

    l.append(date.getText())

    i = 1
    while(True):
        try:
            heading = table.findAll('tr')[i].findAll('th')[0]
            data = table.findAll('tr')[i].findAll('td')[0]
            l.append(heading.getText() + ' :' + data.getText())
            i += 1
        except:
            break
    browser.quit()
    for _ in l:
        a += _ + "\n"
    return a
    