# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from huhua.items import FlowersDetailItem
from huhua.const import FLOWERS_DETAIL_START_URL

from scrapy_redis.spiders import RedisSpider


class FlowersDetailSpider(RedisSpider):
    name = 'flowers_detail'
    redis_key = FLOWERS_DETAIL_START_URL

    custom_settings = {'ITEM_PIPELINES': {
            'huhua.pipelines.RedisFlowersDetailPipeline': 301,
        },}

    def parse(self, response):
        _info = response.css('.infodata')

        obj = FlowersDetailItem()

        obj['pic'] = _info.css('.img img::attr(src)').extract_first()

        _con = _info.css('.cont')

        obj['name'] = _con.css('h1::text').extract_first()
        obj['en_name'] = _con.css('h1 font::text').extract_first() or ''
        obj['alias'] = _con.xpath('./label[1]/text()').extract_first().split('：')[1]  or ''
        obj['category'] = _con.xpath('./label[2]/a/text()').extract_first() or \
        _con.xpath('./label[2]/text()').extract_first()
        obj['keshu'] = _con.xpath('./label[3]/text()').extract_first().split('：')[1]
        obj['shenghuaqi'] = _con.xpath('./label[4]/a/text()').extract_first() or \
        _con.xpath('./label[4]/text()').extract_first()

        _options = response.css('.content dl')

        res = []
        for dl in _options:
            name = dl.xpath('./dt//a/text()').extract_first().split('的')[1]
            val = dl.xpath('./dd').extract_first().replace('<dd>','').replace('</dd>','')
            res.append({'name': name, 'val': val})
        obj['dic'] = res

        yield obj

