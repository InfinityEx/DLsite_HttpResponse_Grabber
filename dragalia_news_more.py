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

# webpage address
for a in range(0,1):
    lang=lang[0]
    priority=3742
    while(priority!='null'):
        if priority==3742:
            # priority_lower_than=None is equivalent to priority_lower_than=3742
            mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang={lang}&td={td}"
        else:
            mainhp=f"https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than={priority}&action=information_list&article_id=&lang={lang}&td={td}"