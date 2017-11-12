from scrapy import Spider, Request
from xiachufang.items import CategoryItem
from urllib.parse import urlparse, parse_qs

BASE_URL = 'http://www.xiachufang.com'


class CategoryListSpider(Spider):
    name = 'category_list'
    allowed_domains = [
        'xiachufang.com',
        'www.xiachufang.com',
        'm.xiachufang.com'
    ]
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            item = CategoryItem()
            item['category'] = sel.xpath('text()').extract()[0]
            item['url'] = BASE_URL + sel.xpath('@href').extract()[0]
            yield item


class RecipeSpider(Spider):
    name = 'recipe'
    allowed_domains = [
        'xiachufang.com',
        'www.xiachufang.com',
        'm.xiachufang.com'
    ]
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            url = BASE_URL + sel.xpath('@href').extract()[0]
            yield Request(url, callback=self.parse_recipe_list)
            print(response.url)

    def parse_recipe_list(self, response):
        for sel in response.css('.recipe'):
            url = BASE_URL + sel.xpath('@href').extract()[0]
            yield Request(url, callback=self.parse_recipe)

        count = len(response.css('.recipe'))
        if count > 0:
            segs = response.url.split('=')
            if len(segs) == 1:
                yield Request(response.url + '?page=2', callback=self.parse_recipe_list)
            else:
                page = int(segs[1]) + 1
                yield Request('%s=%d' % (segs[0], page), callback=self.parse_recipe_list)

    def parse_recipe(self, response):
        print(response.url)
        yield {'url': response.url}
