from scrapy import Item, Field


class XiachufangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CategoryItem(Item):
    category = Field()
    url = Field()


class RecipeItem(Item):
    food_id = Field()
    url = Field()
    name = Field()
    image = Field()
    description = Field()
    materials = Field()
    steps = Field()
    tip = Field()
