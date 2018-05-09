# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import csv
class WangyiyunPipeline(object):
    def process_item(self, item, spider):

        return item


class WangyiyunPipeline(object):

    collection = 'wangyiyun'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_RUI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    # 爬虫启动将会自动执行下面的方法
    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 爬虫项目关闭调用的方法
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.update({'id': item['id']},data,True)
        #self.db[self.collection_name].update({'id': item['id']}, dict(item), True)
        return "OK!"

class WangyinPipeline(object):

    def __init__(self):
        self.f = open("wangyiyun.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['歌曲名称', '歌手', '专辑', '评论总数'])


    def process_item(self, item, spider):
        wangyiyun_list =  [item['name'], item['singer'], item['album'], item['comment_total']]

        self.writer.writerow(wangyiyun_list)
        return item
    def close_spider(self, spider):#关闭
        self.writer.close()
        self.f.close()