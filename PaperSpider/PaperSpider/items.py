# -*- coding: utf-8 -*-

from scrapy import Item, Field
class PaperItem(Item):
    title = Field()
    journal = Field()
    link_url = Field()
    DOI = Field()
