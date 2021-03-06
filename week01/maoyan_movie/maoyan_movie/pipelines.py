# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MaoyanMoviePipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        time = item['time']
        output = [name, type, time]

        movie = pd.DataFrame(data = output)
        movie.to_csv('./maoyan.csv', mode='a+',encoding = 'utf-8', index = False, header = False)
