```python
import requests

url = 'https://movie.douban.com/top250'
# 传递给get方法，模拟浏览器请求
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like  Gecko) Chrome/83.0.4103.106 Safari/537.36'

header = {'User-Agent':user_agent}

response = requests.get(url, headers = header)        # 传递的headers类型为dict

print(f'返回的码为： {response.status_code}')
print(response.text)
```

```python
response = requests.get(url, headers = header)
# 调用BeautifulSoup库来解析网页内容
bs_info = bs(response.text, 'html.parser')

# find以及find_all用来查找标签元素，attrs参数用来缩小查找范围
for tags in bs_info.find_all('div', attrs={'class':'hd'}):
    a_tag = tags.find('a',)
    print(a_tag.get('href'))            # get用来提取标签的属性值
    print(a_tag.find('span',).text)     # .text用来提取标签包含的文本信息
```

```python
import requests
import lxml.etree

...
# 换另一个库来解析网页内容
selector = lxml.etree.HTML(response.text)

# 可以通过xpath定向提取内容，注意最后的text()参数
movie_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称： {movie_name}')

plan_data = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映时间： {plan_data}')

rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分： {rating}')

movie_item = [movie_name, plan_data, rating]

# 调用pandas库将爬取到的内容保存为csv文件
import pandas as pd
movie = pd.DataFrame(data = movie_item)
# windows保存的编码格式为gbk，mac和linux编码格式为utf-8
movie.to_csv('./movie.csv', encoding = 'gbk', index = False, header = False)
```

Anaconda使用

```
# 更改下载源(清华源)
# 按 https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/ 方式进行

# 创建新环境
conda create --name env_name python=version_number
# 激活环境
conda activate env_name
# 查看当前环境
conda info --envs

# 搜索包名
conda search package_name
# 安装包
conda insall package_name
# 查看当前环境安装的包
conda list
```

Scrapy框架初使用

```python
# 其中涉及到四个文件的编写
# spider.py：爬虫逻辑的实现，包括start_request, parse等
# settings.py: 各种优化参数，包括头部信息，请求间隔等
# items.py: 保存爬取得到的数据，并用来传递给管道进行不同介质的永久存储
# pipelines.py: 通过传递的item参数得到爬取的数据，并选择存储方式进行存储，例如文件，数据库等。最后的返回值为item

# spider.py代码逻辑
# -*- coding: utf-8 -*-
import scrapy
from maoyan_movie.items import MaoyanMovieItem
from scrapy.selector import Selector	# 通过scrapy框架自带的解析器，效率更高

# User-Defined Spider Class need to inherit from scrapy.Spider
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'		# 唯一标识爬虫的指示符
    allowed_domains = ['maoyan.com']	# 限制爬虫爬取的范围
    start_urls = ['https://maoyan.com/films?showType=3']	# 开始爬取的发动机

    # 解析函数
    def parse(self, response):
        # 涉及到的xpath语法规则看官方文档就够了
        for ele in Selector(response = response).xpath('//div[@class="movie-hover-info"]')[:10]:
            item = MaoyanMovieItem()
            item['name'] = ele.xpath('./div[1]/span[1]/text()').get()
            item['type'] = ele.xpath('./div[2]/text()[2]').get().strip()
            item['time'] = ele.xpath('./div[4]/text()[2]').get().strip()
            print(item['name'],item['type'],item['time'])
            # 通过yield传递特定的对象
            yield item

# items.py
class MaoyanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    time = scrapy.Field()
   
# pipelines.py
import pandas as pd

class MaoyanMoviePipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        time = item['time']
        output = [name, type, time]

        movie = pd.DataFrame(data = output)
        # mode参数要进行填入
        movie.to_csv('./maoyan.csv', mode='a+',encoding = 'utf-8', index = False, header = False)
```

