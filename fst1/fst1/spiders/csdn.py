# -*- coding: utf-8 -*-
import scrapy
from fst1.items import Fst1Item

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        csdn = Fst1Item()
        csdn["title"] = response.xpath("//h3[@class='tracking-ad']/a/text()").extract()
        csdn["detail"] = response.xpath("//div[@class='blog_list_c']/text()").extract()
        csdn["link"] = response.xpath("//h3[@class='tracking-ad']/a/@href").extract()
        yield csdn