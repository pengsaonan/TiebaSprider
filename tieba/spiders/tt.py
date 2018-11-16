# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem

class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['tieba.baidu.com']
    #填写所需爬取的贴吧名字
    tieba_name = "新垣结衣"
    offset = 0
    url = "http://tieba.baidu.com/f?kw=" + tieba_name + "&pn="
    start_urls = [url]

    def parse(self, response):
        item = TiebaItem()
        links = response.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href').extract()
        for link in links:
            item['tiezi_url'] = "http://tieba.baidu.com/" + link
            yield scrapy.Request(item['tiezi_url'], callback=self.parse_image_link)
        if self.offset <= 100:
            self.offset +=50
            yield scrapy.Request(self.url + str(self.offset) + '.html', callback=self.parse)

    def parse_image_link(self, response):
        item = TiebaItem()
        image_links = response.xpath('//img[@class="BDE_Image"]/@src').extract()
        for image_link in image_links:
            item['image_url'] = image_link
            yield item