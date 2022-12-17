#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dragalia_comic_spider.py
#Version:1.0

import requests as rqs
import random
import time,os
import pandas as pd

# Running path
path=os.path.split(os.path.realpath(__file__))[0]

# languages
# lang:chs, cht, en, en-gb, jp
lang=['chs','cht','en','en-gb','jp']
# type(jp):ゆるがりあ, ドラガリのはじめかた！, ナームのわくわく冒険記
# type(chs):轻松龙约, 失落的龙约上手方法！, 娜姆的波澜冒险记
type=['dragalialife','adventurersguide','plotsynopsis']

test_ly={'lang':'chs','type':'dragalialife'}
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

# dragalialife
# page response(0-23)
for x in range(-1,24):
    for a in lang:
        # a instead of lang
        params={'lang':f'{a}','type':'dragalialife'}
        
        # x==-1 means index, else means 
        if(x==-1):
            # index
            lresponse=rqs.post(f'https://comic.dragalialost.com/api/index',headers=headers,data=params)
            ljson=lresponse.json()
            ljdata=pd.json_normalize(ljson)['items'][0]
            ljdata=pd.json_normalize(ljdata)

            # item in json
            pid=ljdata['id']
            pepnum=ljdata['episode_num']
            ptitle=ljdata['title']
            pmain=ljdata['main']
            pts=ljdata['thumbnail_s']
            ptl=ljdata['thumbnail_l']
            plen=len(ljdata['id'])

            # write index data
            with open(f'{path}/origin/dl_comic/{a}/index.json','w',encoding='utf-8') as origin:
                origin.write(str(lresponse.content).replace("\/","/"))
                origin.close()
            with open(f'{path}/decode/dl_comic/{a}/index.txt','w',encoding='utf-8') as dec:
                for l in range(0,plen):
                    d1=pid[l]
                    d2=pepnum[l]
                    d3=ptitle[l]
                    d4=pmain[l]
                    d5=pts[l]
                    d6=ptl[l]
                    dec.write(f'id:{d1}  episode_num:{d2}\ntitle:{d3}\n\nmain:{d4}\nthumbnail_s:{d5}\nthumbnail_l:{d6}\n\n')
                dec.close()
            with open(f'{path}/decodejson/dl_comic/{a}/index.json','w',encoding='utf-8') as decjs:
                decjs.write('{')
                for j in range(0,plen):
                    if j==plen-1:
                        d1=pid[l]
                        d2=pepnum[l]
                        d3=ptitle[l]
                        d4=pmain[l]
                        d5=pts[l]
                        d6=ptl[l]
                        decjs.write('{'+f'id:{d1},episode_num:{d2},title:{d3},main:{d4},thumbnail_s:{d5},thumbnail_l:{d6}'+'}')
                    else:
                        decjs.write('{'+f'id:{d1},episode_num:{d2},title:{d3},main:{d4},thumbnail_s:{d5},thumbnail_l:{d6}'+'},')
                decjs.write('}')
                decjs.close()
        elif x>=0:
            lresponse=rqs.post(f'https://comic.dragalialost.com/api/thumbnail_list/{x}',headers=headers,data=test_ly)
            ljson=lresponse.json()
            ljdata=pd.json_normalize(ljson)['items'][0]
            ljdata=pd.json_normalize(ljdata)

            # item in json
            pid=ljdata['id']
            pepnum=ljdata['episode_num']
            ptitle=ljdata['title']
            pmain=ljdata['main']
            pts=ljdata['thumbnail_s']
            ptl=ljdata['thumbnail_l']
            plen=len(ljdata['id'])

            # write data
            with open(f'{path}/origin/dl_comic/{a}/{x}.json','w',encoding='utf-8') as origin:
                origin.write(str(lresponse.content).replace("\/","/"))
                origin.close()
            with open(f'{path}/decode/dl_comic/{a}/{x}.txt','w',encoding='utf-8') as dec:
                for l in range(0,plen):
                    d1=pid[l]
                    d2=pepnum[l]
                    d3=ptitle[l]
                    d4=pmain[l]
                    d5=pts[l]
                    d6=ptl[l]
                    dec.write(f'id:{d1}  episode_num:{d2}\ntitle:{d3}\n\nmain:{d4}\nthumbnail_s:{d5}\nthumbnail_l:{d6}\n\n')
                dec.close()
            with open(f'{path}/decodejson/dl_comic/{a}/{x}.json','w',encoding='utf-8') as decjs:
                decjs.write('{')
                for j in range(0,plen):
                    if j==plen-1:
                        d1=pid[l]
                        d2=pepnum[l]
                        d3=ptitle[l]
                        d4=pmain[l]
                        d5=pts[l]
                        d6=ptl[l]
                        decjs.write('{'+f'id:{d1},episode_num:{d2},title:{d3},main:{d4},thumbnail_s:{d5},thumbnail_l:{d6}'+'}')
                    else:
                        decjs.write('{'+f'id:{d1},episode_num:{d2},title:{d3},main:{d4},thumbnail_s:{d5},thumbnail_l:{d6}'+'},')
                decjs.write('}')
                decjs.close()
            with open(f'{path}/res_list/dl_comic/dlcomic_dllife_{a}_main.txt','a+',encoding='utf-8') as ma:
                for k in range(0,plen):
                    if pmain[k]!="":
                        ma.write(pmain[k]+'\n')
                ma.close()
            with open(f'{path}/res_list/dl_comic/dlcomic_dllife_{a}_thumbnail_s.txt','a+',encoding='utf-8') as ts:
                for m in range(0,plen):
                    if pts[m]!="":
                        ts.write(pts[m]+'\n')
                ts.close()
            with open(f'{path}/res_list/dl_comic/dlcomic_dllife_{a}_thumbnail_l.txt','a+',encoding='utf-8') as tl:
                for n in range(0,plen):
                    if ptl[n]!="":
                        tl.write(ptl[n]+'\n')
                tl.close()
        time.sleep(random.randint(1,3))
    print(f"page {x}'s Response Saved.")

# page sequence(0-7)
for y in range(0,8):
    for b in lang:
        params={'lang':f'{b}','type':'dragalialife'}
        
        lresponse=rqs.post(f'https://comic.dragalialost.com/api/pager/0/0/{y}',headers=headers,data=params)
        ljson=lresponse.json()

        with open(f'{path}/origin/dl_comic_pager/{b}/{y}.json','w',encoding='utf-8') as origin:
            origin.write(str(lresponse.content).replace("\/","/"))
            origin.close()

# comic pager
for z in range(0,2000):
    for c in lang:
        params={'lang':f'{c}','type':'dragalialife'}

        lresponse=rqs.post(f'https://comic.dragalialost.com/api/detail/{z}',headers=headers,data=params)
        ljson=lresponse.json()
        if 'error' in lresponse:
            print(f'error comic detail')
            continue
        else:
            ljdata=pd.json_normalize(ljson)

            # write data
            with open(f'{path}/origin/dl_comic_detail/{c}/{x}.json','w',encoding='utf-8') as dt:
                dt.write(str(lresponse.content).replace("\/","/"))
                dt.close()

            # write detail img list
            with open(f'{path}/res_list/dl_comic/dlcomic_dllife_{c}_detail.txt','a+',encoding='utf-8') as dtl:
                ndetail=ljdata['cartoon'][0]
                dtl.write(f'{ndetail}\n')
                dtl.close()
