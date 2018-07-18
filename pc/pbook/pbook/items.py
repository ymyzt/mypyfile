# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PbookItem(scrapy.Item):
    # define the fields for your item here like:
    #z_name = scrapy.Field()
    z_chapter = scrapy.Field()
    #z_url = scrapy.Field()
    z_content = scrapy.Field()
    #pass
