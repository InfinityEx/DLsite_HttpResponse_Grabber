#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:时无ShiWu
# Filename:dlcomic_dladvg_spider.py
# Version:1.0

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

clist=[]

# adventurersguide
# parts: index, detail
def index(lang, ctype):
    data = {'lang': lang, 'type': ctype}
    iresponse = rqs.post(url=f'https://comic.dragalialost.com/api/index', headers=headers, data=data)
    ijson = iresponse.json()

    idlen=len(ijson['items'])
    for x in idlen:
        clist[x]=ijson['items'][x]['id']

    with open(f'{path}/origin/comic_dladvg/{lang}/index.json') as idx:
        idx.write(iresponse.content)
        idx.close()

    with open(f'{path}/origin/comic_dladvg/{lang}/index.json') as ids:
        dect=bytes(iresponse.content).decode('unicode_escape').replace("\/","/")
        ids.write(str(dect))
        ids.close()

    # item in json
    # pid = idata['id']
    # pepnum = idata['episode_num']
    # ptitle = idata['title']
    # pmain = idata['main']
    # pts = idata['thumbnail_s']
    # ptl = idata['thumbnail_l']
    # plen = len(idata)

def detail(lang,ctype,cid):
    print('')

if __name__ == '__main__':
    # for a in lang:
    a = lang[0]
    print(a, type[1])
    index(a, type[1])
    for b in clist:
        detail(a,type[1],clist[b])
