# -*- coding: utf-8 -*-
import redis
from huhua.const import *
import json

class RedisClassificationPipeline(object):
    def __init__(self):
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def process_item(self, item, spider):
        self.redis_cli.rpush(CLASSIFICATION_KEY, json.dumps(dict(item)))
        # 将需要爬取的分类url保存到redis
        self.redis_cli.lpush(CLASSIFICATION_START_URL, 'http://www.aihuhua.com' + item['href'] + 'page-1.html')

        return item

class RedisClassificationAllPipeline(object):
    def __init__(self):
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def process_item(self, item, spider):
        print(item)
        self.redis_cli.rpush(CLASSIFICATION_ALL_KEY, json.dumps(dict(item)))

        return item

class RedisCategoryPipeline(object):
    def __init__(self):
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def process_item(self, item, spider):
        self.redis_cli.rpush(CATEGORY_KEY, json.dumps(dict(item)))
        # 将需要爬取的大类url保存到redis
        if not item.get('parent'):
            print(item)
            self.redis_cli.lpush(FLOWERS_LIST_START_URL, item['href'] + 'page-1.html')

        return item

class RedisFlowersListPipeline(object):
    def __init__(self):
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def process_item(self, item, spider):
        print(item)
        self.redis_cli.lpush(FLOWERS_DETAIL_START_URL, item['href'])
        # 把花卉对应的图片地址存进去，不管有没有
        self.redis_cli.lpush(FLOWERS_IMAGE_START_URL, item['href'].replace('huahui', 'tu'))

        return item

class RedisFlowersDetailPipeline(object):
    def __init__(self):
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def process_item(self, item, spider):
        print(item['name'])
        self.redis_cli.rpush(FLOWERS_DETAIL_KEY, json.dumps(dict(item)))
        # http://pic1.huashichang.com/2018/0829/15/5b86486608c9f_140_120.jpg 如果不需要下载的话可以省略
        self.redis_cli.lpush(FLOWERS_AVATAR_KEY, json.dumps({'name': item['name'], 'path': item['pic'].replace('_140_120', '')}))

        return item
