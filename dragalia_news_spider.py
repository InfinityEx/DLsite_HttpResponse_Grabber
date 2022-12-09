#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dragalia_news_spider.py
#Version:1.0

import requests as rqs
import time
import os
import urllib.parse as uri

# Running path
path=os.path.split(os.path.realpath(__file__))[0]
# languages
lang='zh_cn'
# time delta
timelist={"zh_cn":"+08:00",
    "zh_tw":"xx",
    "en":"xx",
    "en-gb":"xx",
    "jp":"xx",
}

timedelta=uri.quote(timelist[lang])

# news homepage list
url_hplist=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang={lang}&td={timedelta}"

# news information
url_news_info="https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_detail&article_id=2945&lang=zh_cn&td=%2B08%3A00"

# fake UA headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

# response=rqs.get(url,headers=headers)
# print(response)
# print(response.content.decode("unicode_escape"))

sssa="%2B08%3A00"

response=rqs.post(url_hplist,headers=headers)

with open(f"{path}/origin/news_list.txt",'w') as nl:
    nl.write(str(response.content.decode('unicode_escape')).replace("\/","/"))
    nl.close()