# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# 在这里定义scraped项目模型

import scrapy



class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    mytest = scrapy.Field()



	
		