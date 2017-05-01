# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from items import PaperItem

class PaperhubMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["paperSpider"]
        self.PhyRev = db["PhyRev"]

    def process_item(self, item, spider):
        print 'MongoDBItem',item
        """ 判断类型 存入MongoDB """
        if isinstance(item, PaperItem):
            print 'PaperItem True'
            try:
                self.PhyRev.insert(dict(item))
            except Exception:
                pass
        return item
