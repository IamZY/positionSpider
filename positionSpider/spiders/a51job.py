# -*- coding: utf-8 -*-
import scrapy
from ..items import PositionspiderItem

class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['search.51job.com','jobs.51job.com']

    offset = 1

    first_url = 'https://search.51job.com/list/070200,000000,0000,00,9,99,%2B,2,'
    end_url = '.html?lang=c&stype=1&postchannel=0000' \
          '&workyear=99&cotype=99&degreefrom=99' \
          '&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1' \
          '&ord_field=0&confirmdate=9&fromType=&dibiaoid=0' \
          '&address=&line=&specialarea=00&from=&welfare='

    start_urls = [
        first_url + str(offset) + end_url
    ]


    def parse(self, response):
        ret = response.xpath("//div[@class='dw_table']/div[@class='el']")
        # print(ret)
        for r in ret:
            item = PositionspiderItem()
            item["jobName"] = r.xpath("./p/span/a/@title").extract_first()
            href = r.xpath("./p/span/a/@href").extract_first()
            item["businessName"] = r.xpath("./span[@class='t2']/a/@title").extract_first()
            item["position"] = r.xpath("./span[@class='t3']/text()").extract_first()
            item["money"] = r.xpath("./span[@class='t4']/text()").extract_first()
            item["area"] = ""
            yield scrapy.Request(
                href,
                callback=self.parse_detail,
                meta={"item":item}
            )
            # print(href)
            # print(item)

        if self.offset < 2000:
            self.offset += 1

        yield scrapy.Request(self.first_url + str(self.offset) + self.end_url,callback=self.parse)

    def parse_detail(self,response):
        item = response.meta["item"]
        # print(item)
        temp = response.xpath("//div[@class='tHeader tHjob']/div/div/p[@class='msg ltype']/@title").extract_first()
        str_temp = str(temp)
        # item["businessYear"] = str_temp.split('|')[1]
        businessYear = str_temp.split('|')[1].replace("\xa0","")
        item["businessYear"] = businessYear
        # item["education"] = str_temp.split('|')[2]
        education = str_temp.split('|')[2].replace("\xa0","")
        item["education"] = education
        item["businessPerson"] = response.xpath("//div[@class='tBorderTop_box']/div[@class='com_tag']/p[2]/@title").extract_first()
        item["businessType"] = response.xpath("//div[@class='tBorderTop_box']/div[@class='com_tag']/p[3]/@title").extract_first()
        print(item)
        yield item
