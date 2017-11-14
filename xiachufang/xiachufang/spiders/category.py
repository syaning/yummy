from scrapy import Spider
from xiachufang.items import CategoryItem
from xiachufang.util import base_url, domains


class CategoryListSpider(Spider):
    name = 'category'
    allowed_domains = domains
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            item = CategoryItem()
            item['name'] = sel.xpath('text()').extract()[0]
            item['url'] = base_url + sel.xpath('@href').extract()[0]
            yield item
