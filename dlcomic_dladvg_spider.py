#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dlcomic_dladvg_spider.py
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

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

