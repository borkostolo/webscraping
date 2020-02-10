# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cancer_drug_name  = scrapy.Field()
    us_brand_name     = scrapy.Field() 
    fda_approved      = scrapy.Field()
    cancer_to_treat   = scrapy.Field()
    drug_price        = scrapy.Field()
    units_per_package = scrapy.Field()
    volume_per_unit   = scrapy.Field()
    dosage            = scrapy.Field()
    description       = scrapy.Field()



