import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from product import Product


def get_product():
    product_list = get_product_page()
    get_product_detail(product_list)
    return product_list


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
        page = requests.get(crawler_url + upper_page_url)
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
    return product_list


def get_product_detail(product_list):
    for product in product_list:
        set_product_information(product)
        # model_match = re.search(r'[［,\[]型號[］,\]]((.*|\n)+?)[［,\[]', detail)

        # model_match = re.search(r'[［,\[](.*)[］,\]]', detail)

        # model = model_match.group(1).replace("\n", "").strip() if model_match else None
        # product.model = model
        # print(product.model + ':' + product.url)


def set_product_information(product):
    print(product.url)
    page = requests.get(product.url)
    bs_obj = BeautifulSoup(page.content, "html.parser")
    detail = bs_obj.find(id='main-content').getText()
    titles = re.findall(r'[［,\[](.*)[］,\]]', detail)
    print(titles)
    for i in range(0, len(titles)-1):
    #     reg = r'\'[［,\[]' + titles[i] + '[］,\]]((.*|\\n)+?)[［,\[]\''
    #     print('reg: '+reg)
    #     model_match = re.search(reg, detail)
    #     print(titles[i])
    #     print(model_match)
        print(titles[i])
        print(detail.split(titles[i])[1].split(titles[i+1])[0])
        print('----------------------------------------')
        if i == len(titles):
            print(detail.split(titles[i])[1])
        