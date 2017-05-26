# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Fst1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 创建容器存储标题
    # 标签
    title = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 介绍
    detail = scrapy.Field()
