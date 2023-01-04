# DLwebsite_HttpResponse_Grabber

### **Introduction:**

A python script for grabbing the DragaliaLost.com/api/index.php parameter's response.

Now the repository has included the part of img resources.

There has three folders about the response :

**origin** is the source response from index.php, It saved as json file.

**decode** is the source response has been decoded to Unicode_Escape. It's saved as txt file.

**decodejson** is the source response has been decode to Unicode_Escape and saved as json file(But it was not formatting json)

------

### **Response:**

##### Dragalia_News:

There have two types requests founded:

```php+HTML
//Type 1:Get newest news list in Homepage
https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang=jp&td=%2B08%3A00

//Type 2:Get detail news page
https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_detail&article_id=2945&lang=lang=jp&td=%2B08%3A00
```

Now,Let's analyze these parameters next:

**`type`**:which type request to server,there's only know one type is information.

**`category_id`**:Unknow parameters, No usage found.

**`priority_lower_than`**:It will be used in News Page "More", for check newsid in head of next 6 news list.

**`action`**:Differentiate of which type client action, `information_list` means get news list, `information_detail` means get detail page data from server

**`article_id`**:Detail article id number. The same news is the same in different languages.(It is known that news id may begin with 2 and end with 3732**(But jp news is end with 4000)**)

**`lang`**:Languages, the news page supports `zh_cn`(Chinese Simplified), `zh_tw`(Chinese Traditional), `en_us`(American English), `en_eu`(Euro-English?), `ja_jp`(Japanese)

**`time_delta`**:It seems likely to distinguish time zones, but the wrong time delta has no sense to result in error.

------

### **Download Progress:**

<table>
	<tr align="center">
		<th rowspan="2">News Items</th>
        <th rowspan="2">Platform</th>
		<th colspan="6">Languages</th>
	</tr>
	<tr align="center">
		<td>zh_cn</td>
        <td>zh_tw</td>
        <td>en-us</td>
        <td>en-eu</td>
		<td>ja_jp</td>
	</tr>
    <tr align="center">
        <td rowspan=2"">News_Banners</td>
        <td>PC</td>
        <td>√</td>
        <td>√</td>
        <td colspan="2">√</td>
        <td>√</td>
    </tr>
    <tr align="center">
    	<td>Mobile</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
        <td rowspan="2">NewsPage_Images</td>
        <td>PC</td>
        <td>√</td>
        <td>√</td>
        <td colspan="2">√</td>
        <td>√</td>
    </tr>
    <tr align="center">
    	<td>Mobile</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>



<table>
    <tr align="center">
		<th rowspan="2">Comic Items</th>
        <th rowspan="2">Platform</th>
		<th colspan="5" width="100">Languages</th>
	</tr>
	<tr align="center">
		<td>chs</td>
        <td>cht</td>
        <td>en</td>
        <td>en-gb</td>
		<td>jp</td>
	</tr>
    <tr align="center">
    	<td rowspan="2">DragaliaLife</td>
        <td>PC</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
    	<td>Mobile</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
    	<td rowspan="2">AdventurersGuide</td>
        <td>PC</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
    	<td>Mobile</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
    	<td rowspan="2">Plotsynopsis</td>
        <td>PC</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr align="center">
    	<td>Mobile</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>




### **Update Infomation:**

**20221221**：News 1943 has been found a mistake.(Image not found in en/en-gb/zh_tw page, wrong image in zh_cn page, Non image in jp page)
