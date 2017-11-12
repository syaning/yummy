from scrapy import Item, Field


class XiachufangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CategoryItem(Item):
    category = Field()
    url = Field()
