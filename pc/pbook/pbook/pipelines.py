# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PbookPipeline(object):
    def process_item(self, item, spider):
    	print "process_item-------------------------------"
    	print item["z_chapter"]
    	# if spider == "xbqg":
    	f = open("./123/"+item["z_chapter"]+".txt",'w')
    	f.write(item['z_content'])
    	f.close()
        # return item
