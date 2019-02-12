# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from huhua.items import CategoryItem


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['aihuhua.com']
    start_urls = ['http://www.aihuhua.com/baike/']
    custom_settings = {'ITEM_PIPELINES': {
            'huhua.pipelines.RedisCategoryPipeline': 301,
        },}

    def parse(self, response):
        items = response.xpath('//ul[@class="catelist"]/li/h2/a')

        for item in items:
            obj = CategoryItem()
            obj['name'] = item.xpath('./text()').extract_first()
            obj['href'] = item.xpath('./@href').extract_first()

            yield obj
        
        sub_items = response.xpath('//*[@class="sub_catelist"]')

        for item in sub_items:
            obj = CategoryItem()
            obj['parent'] = item.xpath('./dt/text()').extract_first().rstrip('：')
            for x in item.xpath('./dd/a'):
                obj['name'] = x.xpath('./text()').extract_first()
                obj['href'] = x.xpath('./@href').extract_first()

                yield obj


