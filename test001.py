# -*- coding: UTF-8 -*-
import urllib.request

import requests
import codecs
import re
from bs4 import BeautifulSoup


def _init1_(pages):
    main_url = 'https://www.qiushibaike.com/text/page/'
    res = get_html(main_url, pages)
    zz_save(res)

def _init2_(pages):
    main_url = 'https://www.qiushibaike.com/text/page/'
    res = get_html(main_url, pages)
    bs_save(res)

def get_html(url, page):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    real_url =url + str(page)

    request = requests.Request(real_url, headers=headers)
    response = urllib.request.urlopen(request)
    return response

def bs_save(response):
    soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='ut-8')
    contents = soup.find_all('div', class_='content')

    for content in contents:
        text = content.get_text()
        print(text)
        f = codecs.open(u'BS爬取.txt', 'a', 'utf-8')
        f.write(text + '\r\n' + '\r\n' + '\r\n')
        f.close()

def zz_save(response):
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?clearfix">.*?<a.*?<h2>.*?</a>.*?<div.*?content.*?<span>(.*?)</span>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print(item)
        print()
        print()
        text = item
        f = codecs.open(u'正则爬取.txt', 'a', 'utf-8')
        f.write(text + '\r\n' + '\r\n' + '\r\n')
        f.close()


i = 1
print(u'1.正则表达式爬取')
print(u'2.BeautifulSoup爬取')
choose = input(u'请选择:')

if choose == 1:
    while 1:
        _init1_(i)
        if i == 35:
            break
        i += 1
if choose == 2:
    while 1:
        _init2_(i)
        if i == 35:
            break
        i += 1
