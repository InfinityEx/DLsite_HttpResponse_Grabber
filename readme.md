# DLwebsite_HttpResponse_Grabber

A python script for grabbing the DragaliaLost.com/api/index.php parameter's response.

Now the repository has included the part of img resources.

There has three folders about the response :

**origin** is the source response from index.php, It saved as json file.

**decode** is the source response has been decoded to Unicode_Escape. It's saved as txt file.

**decodejson** is the source response has been decode to Unicode_Escape and saved as json file(But it was not formatting json)

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
		<td>jp</td>
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
		<th colspan="5">Languages</th>
	</tr>
	<tr align="center">
		<td>chs</td>
        <td>cht</td>
        <td>en</td>
        <td>en-gb</td>
		<td>ja_jp</td>
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



**Update Infomation:**

**20221221**：News 1943 has been found a mistake.(Image not found in en/en-gb/zh_tw page, wrong image in zh_cn page, Non image in jp page)
