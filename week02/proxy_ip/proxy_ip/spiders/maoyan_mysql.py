# -*- coding: utf-8 -*-
import scrapy
from proxy_ip.items import ProxyIpItem


class Spider1Spider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        for ele in response.xpath('//div[@class="movie-hover-info"]')[:10]:
            item = ProxyIpItem()
            item['name'] = ele.xpath('./div[1]/span[1]/text()').get()
            item['type'] = ele.xpath('./div[2]/text()[2]').get().strip()
            item['time'] = ele.xpath('./div[4]/text()[2]').get().strip()
            yield item
