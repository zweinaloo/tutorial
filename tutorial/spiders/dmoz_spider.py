# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["moedao.com"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "http://www.javlibrary.com/cn/vl_newentries.php"
        "http://www.moedao.com/"
    ]

    def parse(self, response):
         # for sel in response.xpath("//div[@class='hotbox']"):
            item = DmozItem()
            # item['title'] = sel.xpath('a/text()').extract()
            # item['link'] = sel.xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            item['image_urls'] = response.xpath("//div/a/img/@src").extract()
            yield item
