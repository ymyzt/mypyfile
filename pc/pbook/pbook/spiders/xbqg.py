# -*- coding: utf-8 -*-
import scrapy
from pbook.items import PbookItem

class XbqgSpider(scrapy.Spider):
    name = 'xbqg'
    allowed_domains = ['www.xxbiquge.com']
    start_urls = ['https://www.xxbiquge.com/0_36/']
    baseurl = "https://www.xxbiquge.com"
    def parse(self, response):
    	print "1111111111111111111111111111111111111111111111111"
        file = response.xpath("//div[@class = 'box_con']/div[@id = 'list']/dl/dd")
        # print file
        for f in file:
            print u""+ f.extract()
            # print f
            # print 2222222
            item = PbookItem()
            item["z_chapter"] = f.xpath(".//a/text()")[0].extract()
            # print "----------------------------"
            # print u""+item["z_chapter"]
            # print 3333
            url_2 = self.baseurl + f.xpath(".//a/@href")[0].extract()
            # print 4444
            # print  u""+url
            yield scrapy.Request(url = url_2 ,callback = self.parseContent,meta = {'item':item})
            # print 5555

        	
    def parseContent(self, response):
    	item = response.meta['item']
    	str= response.xpath("//div[@class = 'content_read']/div[@class = 'box_con']\
    		/div[@id = 'content']").extract()[0].encode("utf-8")
        str = str.replace("<div id='content'>","")
        str = str.replace("<br>","")
        str = str.replace("</div>","")
        item['z_content'] = str
        yield item