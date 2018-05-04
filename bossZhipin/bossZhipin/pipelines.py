# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

client = pymongo.MongoClient("localhost",27017)

bossJob = client["bossJob"]

class BosszhipinPipeline(object):
    def __init__(self):
        self.nlp = bossJob["自然语言处理"]
    def process_item(self, item, spider):
        #content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.nlp.insert_one(item)
        return item


