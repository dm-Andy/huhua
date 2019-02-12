# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from huhua.items import FlowersListItem

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from huhua.const import FLOWERS_LIST_START_URL


class FlowersListSpider(RedisCrawlSpider):
    name = 'flowers_list'
    redis_key = FLOWERS_LIST_START_URL

    custom_settings = {'ITEM_PIPELINES': {
            'huhua.pipelines.RedisFlowersListPipeline': 301},
            'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
            'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter"
        }

    rules = [
            Rule(LinkExtractor(
                allow=(r'page-\d+.html', r'http://www.aihuhua.com/baike/diyi/', r'http://www.aihuhua.com/baike/taixian/', r'http://www.aihuhua.com/baike/zaolei/')), 
                follow=True, callback='parse_flowers_list')
    ]

    def parse_flowers_list(self, response):
        items = response.xpath('//div[@class="cate_list"]//ul[@class="list"]/li/label//a')

        for item in items:
            obj = FlowersListItem()
            name = item.xpath('./text()').extract_first()
            href = item.xpath('./@href').extract_first()

            obj['name'] = name
            obj['href'] = href

            yield obj