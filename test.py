import pandas as pd
import json
import requests
bdata=b'{"result_code":122,"message":null}'.decode('unicode_escape').replace('null',"'null'")
fdata=b'{"data_headers":{"result_code":1},"data":{"category":{"pr_category_id":"","more_posts":true,"priority_lower_than":"3736","contents":[{"article_id":2975,"priority":3741,"category_name":"\\u6d3b\\u52a8","pr_category_id":"4","caption_type":"event","pr_thumb_type":null,"title_name":"\\u56e2\\u961f\\u6d3b\\u52a8\\u3010\\u590d\\u523b\\u3011\\u201c\\u514b\\u6d1b\\u8bfa\\u65af\\u4e4b\\u6012\\u201d\\u7ec8\\u7ae0\\u8ffd\\u52a0\\uff01","image_path":"https:\/\/dragalialost.akamaized.net\/attached\/information\/images\/0798f9df9fae5f9ee6ef6605da4dacc7.png","date":1669701600,"is_new":false,"is_update":false,"update_time":1664761580},{"article_id":2947,"priority":3740,"category_name":"\\u516c\\u544a","pr_category_id":"1","caption_type":"none","pr_thumb_type":null,"title_name":"\\u201c\\u56e2\\u961f\\u6d3b\\u52a8 \\u767b\\u5f55\\u5956\\u52b1\\u201d\\u6d3b\\u52a8\\u5f00\\u59cb\\uff01","image_path":"https:\/\/dragalialost.akamaized.net\/attached\/information\/images\/c3d579dfda29fd9194cd20578f201bf1.png","date":1669010400,"is_new":false,"is_update":false,"update_time":1646378982},{"article_id":2972,"priority":3739,"category_name":"\\u6d3b\\u52a8","pr_category_id":"4","caption_type":"event","pr_thumb_type":null,"title_name":"\\u56e2\\u961f\\u6d3b\\u52a8\\u3010\\u590d\\u523b\\u3011\\u201c\\u521d\\u9633\\uff01\\u65e5\\u51fa\\u51b3\\u6218\\u201d\\u7ec8\\u7ae0\\u8ffd\\u52a0\\uff01","image_path":"https:\/\/dragalialost.akamaized.net\/attached\/information\/images\/d00dd9592bca43f00bc5684d823f4ee6.png","date":1669010400,"is_new":false,"is_update":false,"update_time":1646728606},{"article_id":2974,"priority":3738,"category_name":"\\u6d3b\\u52a8","pr_category_id":"4","caption_type":"event","pr_thumb_type":null,"title_name":"\\u56e2\\u961f\\u6d3b\\u52a8\\u3010\\u590d\\u523b\\u3011\\u201c\\u514b\\u6d1b\\u8bfa\\u65af\\u4e4b\\u6012\\u201d\\u5f00\\u59cb\\uff01","image_path":"https:\/\/dragalialost.akamaized.net\/attached\/information\/images\/0798f9df9fae5f9ee6ef6605da4dacc7.png","date":1669010400,"is_new":false,"is_update":false,"update_time":1664520097},{"article_id":3233,"priority":3737,"category_name":"\\u516c\\u544a","pr_category_id":"1","caption_type":"summon","pr_thumb_type":"6","title_name":"\\u6697\\u5c5e\\u6027\\u26055\\u89d2\\u8272\\u786e\\u5b9a\\uff01\\u201c\\u767d\\u91d1\\u4f20\\u8bf4\\u53ec\\u5524\\u201d\\u5f00\\u653e\\uff01","image_path":"","date":1668751200,"is_new":false,"is_update":false,"update_time":1652841612},{"article_id":3109,"priority":3736,"category_name":"\\u516c\\u544a","pr_category_id":"1","caption_type":"summon","pr_thumb_type":"6","title_name":"\\u706b\\u5c5e\\u6027\\u26055\\u89d2\\u8272\\u786e\\u5b9a\\uff01\\u201c\\u767d\\u91d1\\u4f20\\u8bf4\\u53ec\\u5524\\u201d\\u5f00\\u653e\\uff01","image_path":"","date":1668751200,"is_new":false,"is_update":false,"update_time":1652841894}]},"category_id":"","new_article_list":[],"update_article_list":[]}}'
print(bdata,type(bdata))
bdata=eval(bdata)
jsa=pd.json_normalize(bdata)
print(jsa['result_code'][0])
# fdata=fdata.decode('unicode_escape').replace("\/",'/')
# fdata=eval(fdata)
# print(fdata)
fdata=requests.post('https://dragaliahp.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang=zh_cn&td=%2B08%3A00',verify=False)
print(fdata)
gdata=fdata.json()
jsf=pd.json_normalize(gdata['data']['category']['contents'])['image_path'][1]
print(jsf,type(jsf))
jsg=pd.json_normalize(gdata['data_headers'])['result_code'][0]
print(jsg,type(jsg),jsg==1)
# print(len(jsf['data']['category']['contents']))
# print(jsf['data']['category']['contents'][0]['image_path'])