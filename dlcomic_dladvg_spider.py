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

clist = []


# adventurersguide
# parts: index, detail
def index(lang, ctype):
    data = {'lang': lang, 'type': ctype}
    iresponse = rqs.post(url=f'https://comic.dragalialost.com/api/index', headers=headers, data=data)
    ijson = iresponse.json()

    idlen = len(ijson['items'])
    for x in range(0, idlen):
        clist.append(int(ijson['items'][x]['id']))

        # item in json
        idata = ijson['items'][x]
        pmain = idata['main']
        pts = idata['thumbnail_s']
        ptl = idata['thumbnail_l']

        with open(f'{path}/res_list/comic_dladvg/dlcomic_advg_{lang}_main.txt', 'a+', encoding='utf-8') as ma:
            ma.write(f'{pmain}\n')
            ma.close()
        with open(f'{path}/res_list/comic_dladvg/dlcomic_advg_{lang}_thumbnail_s.txt', 'a+', encoding='utf-8') as ths:
            ths.write(f'{pts}\n')
            ths.close()
        with open(f'{path}/res_list/comic_dladvg/dlcomic_advg_{lang}_thumbnail_l.txt', 'a+', encoding='utf-8') as thl:
            thl.write(f'{ptl}\n')
            thl.close()

    with open(f'{path}/origin/comic_dladvg/{lang}/index.json', 'w', encoding='utf-8') as idx:
        idx.write(str(iresponse.content))
        idx.close()

    with open(f'{path}/decodejson/comic_dladvg/{lang}/index.json', 'w', encoding='utf-8') as ids:
        dect = bytes(iresponse.content).decode('unicode_escape').replace("\/", "/")
        ids.write(str(dect))
        ids.close()

    time.sleep(random.randint(0, 2))
    print(f'{lang} index json saved.')


def detail(lang, ctype, cid):
    # print(f'{lang},{ctype},{cid}')
    data = {'lang': lang, 'type': ctype}
    dresponse = rqs.post(url=f'https://comic.dragalialost.com/api/detail/{cid}', headers=headers, data=data)

    with open(f'{path}/origin/comic_dladvg/{lang}/{cid}.json', 'w', encoding='utf-8') as ddt:
        ddt.write(str(dresponse.content))
        ddt.close()

    with open(f'{path}/decodejson/comic_dladvg/{lang}/{cid}.json', 'w', encoding='utf-8') as dds:
        decd = bytes(dresponse.content).decode('unicode_escape').replace("\/", "/")
        dds.write(str(decd))
        dds.close()

    time.sleep(random.randint(0, 2))


if __name__ == '__main__':
    for a in lang:
        index(a, type[1])
        for b in range(0, len(clist)):
            detail(a, type[1], clist[b])
        clist.clear()
        print(f'{a} details saved.')
