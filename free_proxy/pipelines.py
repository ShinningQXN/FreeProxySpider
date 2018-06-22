# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
from scrapy.conf import settings

class FreeProxyPipeline(object):
    def process_item(self, item, spider):
        return item






class MongoDB_OCTO_Pipeline(object):
    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT'])
        
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_OCTOPART_IP_COLLECTION']]
    
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

class MongoDB_ARROW_Pipeline(object):
    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT'])
        
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_ARROW_IP_COLLECTION']]
    
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item