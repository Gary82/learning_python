import requests
from bs4 import BeautifulSoup

crawler_url = "https://www.ptt.cc"
mac_shop_path = "/bbs/MacShop"
html = requests.get(crawler_url+mac_shop_path)
bsObj = BeautifulSoup(html.content, "html.parser")
# 取得title
title = bsObj.title
print(title)

tr_list = bsObj.findAll('div', {'class': 'r-ent'})
for tr in tr_list:
    tr_title = tr.find('div', {'class', 'title'}).get_text()
    if '[販售]' in tr_title:
        print(tr_title)
        tr_link = tr.find('div', {'class', 'title'}).find('a').get('href')
        print(crawler_url+tr_link)

