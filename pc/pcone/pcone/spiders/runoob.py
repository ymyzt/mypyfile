# -*- coding: utf-8 -*-
import scrapy
from  pcone.items import PconeItem

class RunoobSpider(scrapy.Spider):
    name = 'runoob'
    allowed_domains = ['www.runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self, response):
     #    title = scrapy.Field()
    	# link = scrapy.Field()
    	# desc = scrapy.Field()
    	items = []
        ss = response.xpath("//h2/text()")
    	for s in ss:
            item = PconeItem()
            desc = s.extract()
            print desc
            item["title"] = desc
            items.append(item)
        #return items