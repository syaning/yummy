from scrapy import Spider, Request
from xiachufang.items import CategoryItem
import json

BASE_URL = 'http://www.xiachufang.com'


class CategoryListSpider(Spider):
    name = 'category_list'
    allowed_domains = ['xiachufang.com', 'www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            item = CategoryItem()
            item['category'] = sel.xpath('text()').extract()[0]
            item['url'] = BASE_URL + sel.xpath('@href').extract()[0]
            yield item


class RecipeSpider(Spider):
    name = 'recipe'
    allowed_domains = ['xiachufang.com', 'www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            url = BASE_URL + sel.xpath('@href').extract()[0]
            yield Request(url, callback=self.parse_recipe_list)

    def parse_recipe_list(self, response):
        for sel in response.css('.recipe'):
            url = sel.xpath('@href').extract()[0]
            print(url)
