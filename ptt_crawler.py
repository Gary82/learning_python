import requests
from bs4 import BeautifulSoup
from datetime import datetime

crawler_url = "https://www.ptt.cc"
mac_shop_path = "/bbs/MacShop"
html = requests.get(crawler_url+mac_shop_path)
bsObj = BeautifulSoup(html.content, "html.parser")
upper_page_url = bsObj.find('a', string=['‹ 上頁']).get('href')
post_date = datetime.today().strftime('%m/%d')
today = datetime.today().strftime('%m/%d')

# Get page data
tr_list = bsObj.findAll('div', {'class': 'r-ent'})
while True: # post_date == today:
    tr_list = bsObj.findAll('div', {'class': 'r-ent'})
    for i in range(len(tr_list) - 1, -1, -1):
        tr = tr_list[i]
        post_date = tr.find('div', {'class', 'meta'}).find('div',{'class', 'date'}).get_text()
        if datetime.today().strftime('%m/%d') == post_date:
            tr_title = tr.find('div', {'class', 'title'}).get_text()
            if '[販售]' in tr_title:
                print(tr_title)
                tr_link = tr.find('div', {'class', 'title'}).find('a').get('href')
                print(crawler_url+tr_link)
        else:
            break