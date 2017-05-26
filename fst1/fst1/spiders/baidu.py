# -*- coding: utf-8 -*-
import scrapy
from fst1.items import Fst1Item

class BaiduSpider(scrapy.Spider):
    # 爬虫文件名字
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['baidu.com']
    # 初始爬取网址
    start_urls = ['http://www.baidu.com/',]

    # 回调函数，把响应信息返回给response
    def parse(self, response):
        # 创建实例化对象
        item = Fst1Item()
        # 输出
        item["title"] = response.xpath('/html/head/title/text()').extract()
        #print(item["title"])
        # 返回item对应的内容到pipelines
        yield item