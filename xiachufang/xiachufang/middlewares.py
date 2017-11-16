from xiachufang.util import base_url, rand_ua
from xiachufang.pool import ip_pool
import random


class HttpHeaderMiddleware(object):

    def process_request(self, request, spider):
        request.headers["User-Agent"] = rand_ua()
        request.headers["Referer"] = base_url


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        ip = random.choice(ip_pool)
        request.meta['proxy'] = 'http://%s:%d' % (ip[0], ip[1])
