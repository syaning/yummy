from scrapy import Item, Field


class CategoryItem(Item):
    name = Field()
    url = Field()


class RecipeItem(Item):
    url = Field()
    name = Field()
    img = Field()
    desc = Field()
    materials = Field()
    steps = Field()
    tips = Field()
    cats = Field()
