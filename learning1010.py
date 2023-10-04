# -*- coding: utf-8 -*-
"""
Created on 2023/09/22

@author: Gary
"""

#%%
import requests
from bs4 import BeautifulSoup
#import csv
from time import localtime, strftime
from os.path import exists
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html.text, "html.parser")
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]

    currency_name = currency_name.replace("\r", "")
    currency_name = currency_name.replace("\n", "")
    currency_name = currency_name.replace(" ", "")
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)
    file_name = "C:\\Users\\User\\Desktop\\bkt_rate"+currency_name+".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
#    f = open(file_name, 'a')
#    w = csv.writer(f)
#    w.writerows(data)
#    f.close()
#%%