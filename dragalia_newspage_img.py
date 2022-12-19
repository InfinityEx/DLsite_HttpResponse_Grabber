#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:时无ShiWu
#Filename:dragalia_newspage_img.py
#Version:1.0

import re
import os

# languages
lang=['zh_cn', 'zh_tw', 'en_us', 'en_eu', 'ja_jp']
# path
path=os.path.split(os.path.realpath(__file__))[0]

for i in lang:
    curlang=i
    tximg=f'{path}/decode/dl_news/{curlang}'
    txlist=os.listdir(tximg)

    for txif in txlist:
        tf=open(os.path.join(tximg,txif),encoding='utf-8')
        temptx=''
        while tf.readline()!="":
            tf_text=tf.readline()
            # print(tf_text)
            tf_text=tf_text.strip('\n')
            temptx+=tf_text
        # print(temptx)
        findimg=re.findall(r'<img src="(.*?)"',temptx)

        for j in findimg:
            ss=j
            with open(f'{path}/res_list/dlh5img/h5img_Unfiltered_{i}_.txt','a+',encoding='utf-8') as wi:
                wi.write(ss+'\n')
            wi.close()
        print(f'Processing: Languages:{i}, Filename:{txif}')
        tf.close()
    print(f'Language {i} imgsrc has been exported.')
        
