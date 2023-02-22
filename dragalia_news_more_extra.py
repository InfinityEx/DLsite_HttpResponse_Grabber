#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:Untitled-1
#Version:1.0

import requests as rqs
import random
import time
import os
import urllib.parse as uri

# Running path
path=os.path.split(os.path.realpath(__file__))[0]

# languages
languages=['zh_cn','zh_tw','en_us','en_eu','ja_jp']
lang=''
# category_id
cateid=['All','News','Updates','Maintenance','Events','Important']

# timedelta
td=uri.quote('+08:00')

# fake UA headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}

s=0

def json2file(pid,la,rescont,resjson,pltm):
    tid=cateid[pid]

    # plt means priority_lower_than
    try:
        plta=resjson['data']['category']['priority_lower_than']
    except KeyError:
        plta=-5
        print('KeyError! Check response.')

    if plta==-5 or plta==None:
        plt=-1
    else:
        with open(f"{path}/origin/dl_news_ex/{la}/{tid}/{pltm}.json",'w',encoding='utf-8') as nl:
            nl.write(str(rescont).replace("\/","/"))
            nl.close()

        with open(f"{path}/decodejson/dl_news_ex/{la}/{tid}/{pltm}.json",'w',encoding='utf-8') as kl:
            ktx=bytes(rescont).decode('unicode_escape').replace("\/","/")
            kl.write(str(ktx))
            kl.close()
            
        plt=resjson['data']['category']['priority_lower_than']
    # print(f'File saved. lang:{la}, priority:{pltm}')
    msg_update(la,tid,pltm)
    return plt

def category(nid):
    for a in range(0,5):
        lang=languages[a]
        # ntype=cateid[nid]
        # print(f'languages:{lang}, Type:{ntype}')
        # webpage address
        priority_m=3742
        while True:
            if priority_m==3742:
                # &priority_lower_than= is equivalent to &priority_lower_than=3742
                mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id={nid}&priority_lower_than=&action=information_list&article_id=&lang={lang}&td={td}"
                response=rqs.post(url=mainhp,headers=headers)
                defrt=json2file(nid,lang,response.content,response.json(),priority_m)
                priority_m=int(defrt)
                time.sleep(random.randrange(0,1))
            elif priority_m==-1:
                break
            else:
                mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id={nid}&priority_lower_than={priority_m}&action=information_list&article_id=&lang={lang}&td={td}"
                response=rqs.post(url=mainhp,headers=headers)
                defrt=json2file(nid,lang,response.content,response.json(),priority_m)
                priority_m=int(defrt)
                time.sleep(random.randrange(0,1))

def msg_update(lang,type,pri):
    print(f'\rLanguages:{lang}, Type:{type}, Priority:{pri}',end='')
    
if __name__=='__main__':
    for zx in range(1,6):
        category(zx)
    print(f'Download Complete.')