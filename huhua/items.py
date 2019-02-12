# -*- coding: utf-8 -*-

import scrapy


class ClassificationItem(scrapy.Item):
    name = scrapy.Field()
    value = scrapy.Field()
    href = scrapy.Field()

# 记录classification下面所有花的name，便于后期加标签用
class ClassificationAllItem(scrapy.Item):
    classification = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()

class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    parent = scrapy.Field()

class FlowersListItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()

class FlowersDetailItem(scrapy.Item):
    name = scrapy.Field()
    pic = scrapy.Field()
    en_name = scrapy.Field()
    alias = scrapy.Field()
    category = scrapy.Field()
    keshu = scrapy.Field()
    shenghuaqi = scrapy.Field()
    dic = scrapy.Field()
