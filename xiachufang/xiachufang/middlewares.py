from xiachufang.util import base_url, rand_ua


class HttpHeaderMiddleware(object):

    def process_request(self, request, spider):
        request.headers["User-Agent"] = rand_ua()
        request.headers["Referer"] = base_url
