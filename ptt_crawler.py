import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

crawler_url = "https://www.ptt.cc/bbs/MacShop/index4005.html"
html = requests.get(crawler_url)
bsObj = BeautifulSoup(html.content, "html.parser")
base_url = urlparse(crawler_url).scheme+'://'+urlparse(crawler_url).netloc
# 取得title
title = bsObj.title
print(title)

tr_list = bsObj.findAll('div', {'class': 'r-ent'})
for tr in tr_list:
    tr_title = tr.find('div', {'class', 'title'}).get_text()
    if '[販售]' in tr_title:
        print(tr_title)
        tr_link = tr.find('div', {'class', 'title'}).find('a').get('href')
        print(base_url+tr_link)

