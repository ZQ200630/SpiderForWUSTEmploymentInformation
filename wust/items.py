# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WustItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    companyName = scrapy.Field()
    time = scrapy.Field()
    address = scrapy.Field()
    telephone = scrapy.Field()
    positionName = scrapy.Field()
    positionSalary = scrapy.Field()
    major = scrapy.Field()
