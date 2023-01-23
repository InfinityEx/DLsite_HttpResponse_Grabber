# DLwebsite_HttpResponse_Grabber

<p align="center">
	<a href="/readme.md">English</a>
	•
	<a href="/readme_cn.md">简体中文</a>
</p>

### **仓库简介:**

本仓库只是个简单的通过python脚本来获取和保存龙约官网DragaliaLost.com/api/index.php的参数和响应数据的保存点。

目前仓库的文件同时也包括了获取图片资源部分的数据(图片数据会逐步上传到另一个仓库)

下面简单介绍下各个文件夹用于存放哪些东西：

**origin** 主要是获取原始的响应数据，这些数据将以原本的形式(json)保存

**decode** 是经过分类转码的原始响应，已经不再是原本的形式，这些数据将以txt文档的形式保存

**decodejson** 是仅将获得的原始数据转码后保存，这些数据依然以原本的形式(json)保存

------

### 响应数据解析：

##### **龙约新闻中心**：

现在已知的新闻中心的查询API有两种形式：

```php+html
//形式1：在主页和新闻中心页获取新闻列表
https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_list&article_id=&lang=jp&td=%2B08%3A00
//注意，当在新闻中心点击一次加载更多后，priority_lower_than参数会开始带一个下标，例如
https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=3796&action=information_list&article_id=&lang=jp&td=%2B08%3A00

//形式2：查询具体新闻的页面数据
https://dragalialost.com/api/index.php?format=json&type=information&category_id=&priority_lower_than=&action=information_detail&article_id=2945&lang=lang=jp&td=%2B08%3A00
```

接下来，我们简单分析下出现的参数：

**`type`**:即从服务器接收何种请求，目前只知道可以向服务器请求information，也就是新闻

**`category_id`**:未知参数，也无法确定用途

**`priority_lower_than`**:当请求新闻列表时，回传的json会从服务器查询新闻列表和下标ID，当再次请求时会从该下标ID开始，以该ID向服务器请求从该ID开始的新闻列表(默认加载更多请求的新闻都是6个)

**`action`**:用于区分客户端现在的动作,当action为 `information_list` 时获取新闻中心的新闻列表,当action为  `information_detail` 则从服务器获取具体新闻的网页数据

**`article_id`**:当action为 `information_detail` 才使用，该参数必须有具体的新闻文章的ID号，不同语言的页面中，同一个 `article_id` 的内容是相同的(现已知的新闻ID是从2开始，到3732结束**(但日语页面的新闻ID是到4000才结束)**)

**`lang`**:字面意义，指客户端页面是哪种语言，新闻页面包括漫画站支持 `zh_cn`(简体中文)， `zh_tw`(繁体中文)， `en_us`(美式英语)， `en_eu`(欧式英语?但是两种英语页面内容看上去又是完全相同的), `ja_jp`(日语)。官方列出的语言中只有法语是没有任何页面的。

**`td`**:即time delta，指客户端时区，但是暂时没有发现该参数对于获取到的数据有什么影响，不属于客户端或者错误的time delta值不会影响返回的结果

------

### 下载进度：

<table>
	<tr align="center">
		<th rowspan="2">新闻数据类型</th>
        <th rowspan="2">平台</th>
		<th colspan="6">语种</th>
	</tr>
	<tr align="center">
		<td>简体中文</td>
        <td>繁体中文</td>
        <td>美式英语</td>
        <td>欧式英语？</td>
		<td>日语</td>
	</tr>
    <tr align="center">
        <td rowspan=2"">新闻Banner图</td>
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
        <td rowspan="2">新闻页面内图片</td>
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
        <td rowspan=2"">新闻加载列表json数据</td>
        <td>PC</td>
        <td>√</td>
        <td>√</td>
        <td>√</td>
	<td>√</td>
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
		<th rowspan="2">漫画数据类型</th>
        <th rowspan="2">平台</th>
		<th colspan="5" width="100">语种</th>
	</tr>
	<tr align="center">
		<td>简体中文</td>
        <td>繁体中文</td>
        <td>英语</td>
        <td>欧式英语？</td>
		<td>日语</td>
	</tr>
    <tr align="center">
    	<td rowspan="2">轻松龙约</td>
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
    	<td rowspan="2">失落的龙约上手方法！</td>
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
    	<td rowspan="2">娜姆的波澜冒险记</td>
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



### **更新记录:**

**20221221**：ID为1943的新闻存在错误.(在英语及繁中页面找不到图片，简中页面显示无关的错误图片，日语页面该新闻没有配图)