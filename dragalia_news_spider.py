#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dragalia_news_spider.py
#Version:1.0

import requests as rqs
import random
import time
import os
import urllib.parse as uri
import pandas as pd

# Running path
path=os.path.split(os.path.realpath(__file__))[0]
# languages
# lang: zh_cn, zh_tw, en_us, en_eu, ja_jp
lang='en_eu'
# time delta
timelist={"zh_cn":"+08:00",
    "zh_tw":"+08:00",
    "en_us":"+00:00",
    "en_eu":"+01:00",
    "ja_jp":"+09:00",
}
news_idlist=[]
timedelta=uri.quote(timelist[lang])

# news homepage list
url_hplist=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang={lang}&td={timedelta}"

# news information
url_news_info="https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_detail&article_id=2945&lang=lang={lang}&td={timedelta}"

# fake UA headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

# response=rqs.get(url,headers=headers)
# print(response)
# print(response.content.decode("unicode_escape"))
# sssa="%2B08%3A00"

# collect all news info
for i in range(0,4500):
    id=i
    url_hplist=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_detail&article_id={id}&lang={lang}&td={timedelta}"
    response=rqs.post(url_hplist,headers=headers)
    contents=response.json()

    # print(str(response.content))
    if 'data_headers' not in contents:
        print(contents,f'error page, page id {i}')
        time.sleep(random.randint(1,3))
        continue

    # result_code
    recode=pd.json_normalize(contents['data_headers'])['result_code'][0]
    imgsrc=''
    # download json
    if recode==1:
        print(f"now page id: {i}")

        # src
        artid=pd.json_normalize(contents['data']['information'])['article_id'][0]
        catname=pd.json_normalize(contents['data']['information'])['category_name'][0]
        img=pd.json_normalize(contents['data']['information'])['image_path'][0]
        msg=pd.json_normalize(contents['data']['information'])['message'][0]
        startt=pd.json_normalize(contents['data']['information'])['start_time'][0]
        title=pd.json_normalize(contents['data']['information'])['title_name'][0]
        updatet=pd.json_normalize(contents['data']['information'])['update_time'][0]

        with open(f"{path}/origin/{lang}/dl_news/{id}.json",'w',encoding='utf-8') as nl:
            nl.write(str(response.content).replace("\/","/"))
            nl.close()
        with open(f"{path}/decode/{lang}/dl_news/{id}.txt",'w',encoding='utf-8') as nt:
            nt.write(f"article_id:{artid}\ncategory_name:{catname}\ntitle_name:{title}\nimage_path:{img}\n\nmessage:{msg}\n\nstart_time:{startt}; update_time{updatet}")
            nt.close()
        with open(f"{path}/decodejson/{lang}/dl_news/{id}.json",'w',encoding='utf-8') as nj:
            nj.write(f"article_id:{artid},category_name:{catname},title_name:{title},image_path:{img},message:{msg},start_time:{startt},update_time{updatet}")
            nj.close()
        with open(f"{path}/dlnews_picres_{lang}.txt",'a+') as pic:
            if img!="":
                pic.write(f"{img}\n")
            pic.close()
    
    # sleep random seconds
    time.sleep(random.randint(1,7))