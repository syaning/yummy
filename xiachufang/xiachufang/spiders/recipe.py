from scrapy import Spider, Request
from xiachufang.items import RecipeItem
from xiachufang.util import base_url, domains


class RecipeSpider(Spider):
    name = 'recipe'
    allowed_domains = domains
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        for sel in response.css('.cates-list-all li a'):
            url = base_url + sel.xpath('@href').extract()[0]
            yield Request(url, callback=self.parse_recipe_list)

    def parse_recipe_list(self, response):
        for sel in response.css('.recipe'):
            url = base_url + sel.xpath('@href').extract()[0]
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
        item = RecipeItem()
        item['url'] = response.url
        item['name'] = response.css('h1.page-title') \
                               .xpath('text()') \
                               .extract()[0].strip()

        img_sel = response.css('.recipe-show .cover img')
        if len(img_sel):
            item['img'] = img_sel.xpath('@src').extract()[0]
        else:
            item['img'] = ''

        desc_sel = response.css('.recipe-show .desc')
        if len(desc_sel):
            item['desc'] = desc_sel.xpath('text()').extract()[0].strip()
        else:
            item['desc'] = ''

        item['materials'] = []
        for sel in response.css('.ings tr'):
            url_sel = sel.css('.name a')
            name_sel = url_sel or sel.css('.name')
            name = name_sel.xpath('text()').extract()[0].strip()
            unit = sel.css('.unit').xpath('text()').extract()[0].strip()
            if len(url_sel):
                url = base_url + url_sel.xpath('@href').extract()[0]
            else:
                url = ''
            item['materials'].append({'name': name, 'unit': unit, 'url': url})

        item['steps'] = []
        for sel in response.css('.steps li'):
            text = sel.css('.text').xpath('text()').extract()[0].strip()
            img_sel = sel.css('img')
            if len(img_sel):
                img = img_sel.xpath('@src').extract()[0]
            else:
                img = ''
            item['steps'].append({'text': text, 'img': img})

        tip_sel = response.css('.tip')
        if len(tip_sel):
            tips = tip_sel.xpath('text()').extract()
            item['tips'] = [tip.strip() for tip in tips]
        else:
            item['tips'] = []

        item['cats'] = []
        for sel in response.css('.recipe-cats a'):
            name = sel.xpath('text()').extract()[0]
            url = base_url + sel.xpath('@href').extract()[0]
            item['cats'].append({'name': name, 'url': url})

        yield item
