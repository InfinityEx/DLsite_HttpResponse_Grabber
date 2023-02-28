#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dlcomic_dlplsy_spider.py
#Version:1.0

import requests as rqs
import random
import time, os
import pandas as pd

# Running path
path = os.path.split(os.path.realpath(__file__))[0]

# languages
# lang:chs, cht, en, en-gb, jp
lang = ['chs', 'cht', 'en', 'en-gb', 'jp']
# type(jp):ゆるがりあ, ドラガリのはじめかた！, ナームのわくわく冒険記
# type(chs):轻松龙约, 失落的龙约上手方法！, 娜姆的波澜冒险记
type = ['dragalialife', 'adventurersguide', 'plotsynopsis']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36'}

clist = []

def index(lang,ctype):
    data={'lang':lang,'type':ctype}
    iresponse = rqs.post(url=f'https://comic.dragalialost.com/api/index', headers=headers, data=data)

    with open(f'{path}/origin/comic_dlplsy/{lang}/index.json', 'w', encoding='utf-8') as idx:
        idx.write(str(iresponse.content))
        idx.close()

    with open(f'{path}/decodejson/comic_dlplsy/{lang}/index.json', 'w', encoding='utf-8') as ids:
        inda = bytes(iresponse.content).decode('unicode_escape').replace("\/", "/")
        ids.write(str(inda))
        ids.close()

    time.sleep(random.randint(0,1))

def pager(lang,ctype):
    data={'lang':lang,'type':ctype}
    for page in range(1,-1,-1):
        presponse = rqs.post(url=f'https://comic.dragalialost.com/api/thumbnail_list/{page}', headers=headers, data=data)
        pjson=presponse.json()

        plen=len(pjson)
        for x in range(0,plen):
            clist.append(int(pjson[x]['id']))

            # item in json
            pmain=pjson[x]['main']
            pts=pjson[x]['thumbnail_s']
            ptl=pjson[x]['thumbnail_l']

            with open(f'{path}/res_list/comic_dlplsy/dlcomic_plsy_{lang}_main.txt', 'a+', encoding='utf-8') as ma:
                ma.write(f'{pmain}\n')
                ma.close()
            with open(f'{path}/res_list/comic_dlplsy/dlcomic_plsy_{lang}_thumbnail_s.txt', 'a+', encoding='utf-8') as ths:
                ths.write(f'{pts}\n')
                ths.close()
            with open(f'{path}/res_list/comic_dlplsy/dlcomic_plsy_{lang}_thumbnail_l.txt', 'a+', encoding='utf-8') as thl:
                thl.write(f'{ptl}\n')
                thl.close()
     
        with open(f'{path}/origin/comic_dlplsy/{lang}/page{page}.json', 'w', encoding='utf-8') as pgo:
            pgo.write(str(presponse.content))
            pgo.close()

        with open(f'{path}/decodejson/comic_dlplsy/{lang}/page{page}.json', 'w', encoding='utf-8') as pgd:
            dect = bytes(presponse.content).decode('unicode_escape').replace("\/", "/")
            pgd.write(str(dect))
            pgd.close()
        
        time.sleep(random.randint(0,1))

def detail(lang,ctype):
    data={'lang':lang,'type':ctype}
    for cid in clist:
        dresponse=rqs.post(url=f'https://comic.dragalialost.com/api/detail/{cid}', headers=headers, data=data)

        

if __name__ == '__main__':
    a=lang[0]
    # index(a,type[2])
    pager(a,type[2])