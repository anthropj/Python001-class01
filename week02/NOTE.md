学习笔记

pymysql连接Mysql数据库

```python
# 步骤
# 连接-获得游标-数据库操作-关闭游标-关闭数据库
import pymysql

# 针对不同的数据库要正确指定字符编码格式
conn = pymysql.connect(
					host = '',port=?,user = '',
					password='',database='',charset='')
cursor1 = conn.cursor()

cursor1.execute('')		# 返回的结果为查询到的结果数量
# cursor.fetchone()/fetchall()

cursor1.close()
conn.close()
```



模拟头部信息： 运用第三方库 fake_userageent

```python
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl = False)
# ua.Chrome, ua.FireFox...
# 可以模拟出不同浏览器的头部信息
```



采取requests.Session()可以保持连接状态，保留传递信息

```python
import requests

s = requests.Session()
# s.get(url),以GET方式请求传递的信息已保留在此次会话中
# 以同样的Session进行的操作可以共享该信息

# 可以采用上下文管理器进行会话的连接,不需要手动关闭会话
with requests.Session() as s:
    # s.get(url)
```



使用WebDriver模拟浏览器行为

```python
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # browser.get(url)
    # browser.find_element_by_id/xpath(...).click()/send_keys()
    # 模拟浏览器的点击和输入行为
    # browser.get_cookies()		获取cookies信息很重要
except Exception as e:
    pass
finally:
    browser.close()				# 最后一定要关闭浏览器
```



文件下载：

```python
# 文件要以二进制形式写入
import requests
with open(file_name, 'wb') as f:
    f.write(requests.get(url_name).content)
    
# 对于大文件来说，得进行分块下载
r = requests.get(file_url, stream = True)
with open(file_name, 'wb') as pdf:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            pdf.write(chunk)
```



自定义中间件

```python
# middlewares.py结构
# from_crawler把值返回给__init__方法
class ClassName(HttpProxyMiddleware):
    def __init__(self,auth_encoding='utf-8',proxy_list=None):
        # 处理从from_crawler方法中返回的结果
        # proxies为dict
        pass
    
    @classmethod
    def from_crawler(cls,crawler):
        # 从settings文件中获取配置信息
        pass
    
    def _set_proxy(self,request,scheme):
        pass
```

