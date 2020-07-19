# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ProxyIpPipeline:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('HOST'),
            port = crawler.settings.get('PORT'),
            user = crawler.settings.get('USER'),
            password = crawler.settings.get('PASSWORD'),
            database = crawler.settings.get('DATABASE'),
            )

    def open_spider(self, spider):
        self.conn = pymysql.connect(host = self.host,
                                    port = self.port,
                                    user = self.root,
                                    password = self.password,
                                    database = self.database)
        self.cursor = self.conn.cursor()

        create_sql = '''
                CREATE TABLE movies(
                name VARCHAR(20) NOT NULL,
                type VARCHAR(20) NOT NULL,
                time DATE NOT NULL);
        '''
        self.cursor.execute(create_sql)

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        inseert_sql = f'''
            INSERT INTO TABLE movies(name,type,time) 
            VALUES({item['name']},{item['type']},{item['time']});'''
        try:
            self.cursor.execute(insert_sql)
        except:
            self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()
        return item