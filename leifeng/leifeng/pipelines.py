# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json

client = pymongo.MongoClient("localhost",27017)
leifengWang = client["leifengWang"]
leifeng = leifengWang["新闻信息"]
#
# class LeifengPipeline(object):
#     def __init__(self):
#         self.file = open("news.json","w",encoding="utf-8")
#
#     def process_item(self, item, spider):
#         leifeng.insert_one(item)
#         return item

class LeifengPipeline(object):

    def __init__(self):
        self.file = open('news.json', 'w',encoding="utf-8")
        self.ciyun = open("ciyun.text","w",encoding="utf-8")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        titles = json.dumps(dict(item)["title"], ensure_ascii=False) + "\n"
        self.file.write(content)
        self.ciyun.write(titles)
        return item

    def close_spider(self, spider):
        self.file.close()