# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PositionspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    businessName = scrapy.Field()
    jobName = scrapy.Field()
    money = scrapy.Field()
    area = scrapy.Field()
    businessYear = scrapy.Field()
    education = scrapy.Field()
    businessPerson = scrapy.Field()
    businessType = scrapy.Field()
    position = scrapy.Field()
