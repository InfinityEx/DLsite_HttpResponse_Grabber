#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dragalia_news_more.py
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
lang=['zh_cn','zh_tw','en_us','en-eu','ja_jp']

# timedelta
td=uri.quote('+08:00')

# fake UA headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def json2file(recont,rejson):
    # contents: original response data
    # djson: original json data
    contents=recont
    djson=rejson
    # plt means priority_lower_than
    if djson['data']['category']['priority_lower_than']==None:
        plt=-1
    else:
        plt=djson['data']['category']['priority_lower_than']
        jslen=len(djson['data']['category']['contents'])
        jsdata=djson['data']['category']['contents']
        for a in range (0,jslen):
            article_id=jsdata[a]['article_id']
            priority=jsdata[a]['priority']
            category_name=jsdata[a]['category_name']
            pr_category_id=jsdata[a]['pr_category_id']
            caption_type=jsdata[a]['caption_type']
            pr_thumb_type=jsdata[a]['pr_thumb_type']
            title_name=jsdata[a]['title_name']
            image_path=jsdata[a]['image_path']
            date=jsdata[a]['date']
            is_new=jsdata[a]['is_new']
            is_update=jsdata[a]['is_update']
            update_time=jsdata[a]['update_time']

            # save data
            with open(f"{path}/origin/dl_news_more/{lang}/{priority_m}.json",'w',encoding='utf-8') as nl:
                nl.write(str(contents).replace("\/","/"))
                nl.close()
            with open(f"{path}/decode/dl_news_more/{lang}/{priority_m}.txt",'a+',encoding='utf-8') as nt:
                nt.write(f"contents_order:{a}\narticle_id:{article_id}\npriority:{priority}\ncategory_name:{category_name}\npr_category_id:{pr_category_id}\ncaption_type:{caption_type}\npr_thumb_type:{pr_thumb_type}\ntitle_name:{title_name}\nimage_path:{image_path}\ndate:{date}\nis_new:{is_new}\nis_update:{is_update}\nupdate_time:{update_time}\n\n")
                nt.close()
            with open(f"{path}/res_list/dlnewsmore/newsm_img_{lang}.txt",'a+') as pic:
                if image_path!="":
                    pic.write(f"{image_path}\n")
                pic.close()
            print('File saved. lang:{lang}, priority:{priority_m}')
    return plt

if __name__=='__main__':
    # webpage address
    priority_m=3742
    for a in range(0,5):
        lang=lang[0]
        while(priority_m!=-1):
            if priority_m==3742:
                # &priority_lower_than= is equivalent to &priority_lower_than=3742
                mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang={lang}&td={td}"
                response=rqs.post(url=mainhp,headers=headers)
                defrt=json2file(response.content,response.json())
                priority_m=defrt
            else:
                mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than={priority_m}&action=information_list&article_id=&lang={lang}&td={td}"
                response=rqs.post(url=mainhp,headers=headers)
                defrt=json2file(response.content,response.json())
                priority_m=defrt