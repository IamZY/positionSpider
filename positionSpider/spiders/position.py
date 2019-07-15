# -*- coding: utf-8 -*-
import scrapy
import json
import random
import time
import hashlib
from ..items import PositionspiderItem


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['fe-api.zhaopin.com']

    # 1、生成一个随机32位数id
    md5 = hashlib.md5()
    id = str(random.random())
    md5.update(id.encode('utf-8'))
    random_id = md5.hexdigest()
    # 2、生成当前时间戳
    now_time = int(time.time() * 1000)
    # 3、生成随机6位数
    randomnumb = int(random.random() * 1000000)
    #组合代码
    x_zp_page_request_id = str(random_id) + '-' + str(now_time) + '-' + str(randomnumb)
    url_v = round(random.random(), 8)


    url = "https://fe-api.zhaopin.com/c/i/sou?" \
          "pageSize=90" \
          "&cityId=635" \
          "&salary=0,0" \
          "&workExperience=-1" \
          "&education=-1" \
          "&companyType=-1" \
          "&employmentType=-1" \
          "&jobWelfareTag=-1" \
          "&kt=3&=0" \
          "&_v="+str(url_v)+ \
          "&x-zp-page-request-id="+str(x_zp_page_request_id)+ \
          "&x-zp-client-id=6c3394df-ce7c-4bec-818f-f6c82d66e758" \
          "&start="

    offset = 0

    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        res = json.loads(response.text)["data"]["results"]
        '''
        businessName = scrapy.Field()
        jobName = scrapy.Field()
        money = scrapy.Field()
        area = scrapy.Field()
        businessYear = scrapy.Field()
        education = scrapy.Field()
        businessPerson = scrapy.Field()
        businessType = scrapy.Field()
        '''
        for r in res:
            item = PositionspiderItem()
            item["businessName"] = r["company"]["name"]
            item["jobName"] = r["jobName"]
            item["money"] = r["salary"]
            item["area"] = r["businessArea"]
            item["businessYear"] = r["workingExp"]["name"]
            item["education"] = r["eduLevel"]["name"]

            # item["businessPerson"] = r["company"]["size"]["name"]
            t = r["company"]["size"]
            if "name" in t:
                item["businessPerson"] = r["company"]["size"]["name"]


            item["businessType"] = r["jobType"]["items"][0]["name"]
            item["position"] = r["city"]["display"]
            print(item)
            yield item

        if self.offset < 990:
            self.offset += 90

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)