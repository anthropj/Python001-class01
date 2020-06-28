import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import random

url = 'https://maoyan.com/films?showType=3'
USER_AGENT_LIST=[
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
USER_AGENT = random.choice(USER_AGENT_LIST)
headers = {'User-Agent' : USER_AGENT}

response = requests.get(url = url, headers = headers)
# print(response.text)
soup = bs(response.text, 'html.parser')

first_ten_items = soup.find_all('div', attrs={'class' : 'movie-hover-info'})[:10]
# print(first_ten_items)

movies = []
for item in first_ten_items:
    name = item.find_all('div')[0].text.strip().split('\n')[0]
    type = item.find_all('div')[1].text.split(':')[1].strip()
    time = item.find_all('div')[3].text.split(':')[1].strip()
    # print(name,type,time)
    movies.append([name,type,time])

movie_file = pd.DataFrame(data = movies)
movie_file.to_csv('./movie_file.csv', encoding = 'utf-8', index = False, header = False)