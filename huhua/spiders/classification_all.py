# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from huhua.items import ClassificationAllItem

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from huhua.const import CLASSIFICATION_START_URL

# 爬取所有的分类下的花卉名称，不包含详细信息，只是为了后期加标签
class ClassificationAllSpider(RedisCrawlSpider):
    name = 'classification_all'
    redis_key = CLASSIFICATION_START_URL

    custom_settings = {'ITEM_PIPELINES': {
            'huhua.pipelines.RedisClassificationAllPipeline': 301},
            'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
            'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter"
        }

    rules = [
            Rule(LinkExtractor(allow=(r'page-\d+.html')), follow=True, callback='parse_classification')
    ]

    def parse_classification(self, response):
        classification = response.css('div.catelists a.on::text').extract_first()
        items = response.xpath('//ul[@class="imglist"]/li[position()>1]')

        for item in items:
            obj = ClassificationAllItem()
            name = item.css('a.title::text').extract_first()

            href = item.css('a.title::attr(href)').extract_first()

            obj['classification'] = classification
            obj['name'] = name
            obj['href'] = href

            yield obj