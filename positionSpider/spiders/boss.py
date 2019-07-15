# -*- coding: utf-8 -*-
import scrapy
from ..items import PositionspiderItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']

    offset = 1

    first_url = 'https://www.zhipin.com/c101190100/?page='
    end_url = '&ka=page-'
    start_urls = [
        first_url + str(offset) + end_url + str(offset)
    ]

    def parse(self, response):
        ret = response.xpath("//div[@class='job-list']/ul/li")
        for r in ret:
            item = PositionspiderItem()
            item["jobName"] = r.xpath(".//div[@class='job-title']/text()").extract_first()
            item["businessName"] = r.xpath(".//div[@class='company-text']/h3[@class='name']/a/text()").extract_first()
            item["position"] = r.xpath(".//div[@class='info-primary']/p/text()[1]").extract_first()
            item["businessYear"] = r.xpath(".//div[@class='info-primary']/p/text()[2]").extract_first()
            item["education"] = r.xpath(".//div[@class='info-primary']/p/text()[3]").extract_first()
            item["area"] = ""
            item["businessType"] = r.xpath(".//div[@class='info-company']//p/text()[1]").extract_first()
            item["businessPerson"] = r.xpath(".//div[@class='info-company']//p/text()[3]").extract_first()
            item["money"] = r.xpath(".//span[@class='red']/text()").extract_first()

            print(item)

            yield item

        if self.offset < 10:
            self.offset += 1

        yield scrapy.Request(self.first_url + str(self.offset) + self.end_url + str(self.offset))