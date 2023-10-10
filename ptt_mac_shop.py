import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from product import Product

def get_product():
    product_list = get_product_page()
    get_product_detail(product_list)


def get_product_page():
    crawler_url = "https://www.ptt.cc"
    mac_shop_path = "/bbs/MacShop"
    page = requests.get(crawler_url + mac_shop_path)
    product_list = []
    is_last = False
    # Get all data
    while not is_last:
        bs_obj = BeautifulSoup(page.content, "html.parser")
        upper_page_url = bs_obj.find('a', string=['‹ 上頁']).get('href')
        tr_list = bs_obj.findAll('div', {'class': 'r-ent'})
        for i in range(len(tr_list) - 1, -1, -1):
            tr = tr_list[i]
            post_date = tr.find('div', {'class', 'meta'}).find('div', {'class', 'date'}).get_text()
            tr_title = tr.find('div', {'class', 'title'}).get_text()
            if '[販售]' not in tr_title:
                continue
            if datetime.today().strftime('%m/%d') != post_date:
                is_last = True
                break
            tr_link = tr.find('div', {'class', 'title'}).find('a').get('href')
            product_list.append(Product(tr_title, crawler_url + tr_link, post_date))
        page = requests.get(crawler_url + upper_page_url)
    return product_list


def get_product_detail(product_list):
    # for product in product_list:
    page = requests.get(product_list[0].url)
    bs_obj = BeautifulSoup(page.content, "html.parser")
    detail = bs_obj.find(id='main-content').getText()
    print(detail)
    # detail = '[型號]123123[規格]'
    # world = detail[detail.index('[型號]'):detail.index('[保固]')]
    model_match = re.search(r'\[型號\] (.+)', detail)
    # print(world)
    # world = detail[detail.index('[型號]'):detail.index('[保固]')]
    print(model_match)

    if model_match:
        model = model_match.group(1)
    else:
        model = "未提供型號"
    print("型號:", model)