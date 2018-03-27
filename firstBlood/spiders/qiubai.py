# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        print(response.text)
        div_list = response.xpath('//div[starts-with(@id,"qiushi_tag_")]')
        items = []
        for div in div_list:
            item = {}
            image_url = div.xpath('.//div[1]//img/@src').extract_first()  # 提取值
            name = div.xpath('.//div[1]//img/@alt').extract_first()  # 提取值
            age = div.xpath('.//div[1]/div/text()').extract_first()  # 提取值
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()  # 提取值
            item['image_url'] = image_url
            item['name'] = name
            item['age'] = age
            item['content'] = content
            items.append(item)
            print('*' * 59)
        return items
