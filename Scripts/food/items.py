# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name        = scrapy.Field()
    level       = scrapy.Field()
    servings    = scrapy.Field()
    total       = scrapy.Field()
    ingredients = scrapy.Field()
    steps       = scrapy.Field()
    review      = scrapy.Field()
    rating      = scrapy.Field()

