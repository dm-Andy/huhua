# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from huhua.items import ClassificationItem

# 爬取所有的分类名称和地址
class ClassificationSpider(scrapy.Spider):
    name = 'classification'
    allowed_domains = ['aihuhua.com']
    start_urls = ['http://www.aihuhua.com/hua/']
    custom_settings = {'ITEM_PIPELINES': {
            'huhua.pipelines.RedisClassificationPipeline': 301,
        },}

    def parse(self, response):
        uls = response.xpath('//div[@class="catelists"]/ul')

        for ul in uls:
            item = ClassificationItem()

            item['name'] = ul.xpath('./h2/text()').extract_first()
            for x in ul.xpath('./li/a'):
                item['value'] = x.xpath('./text()').extract_first()
                item['href'] = x.xpath('./@href').extract_first()

                yield item

