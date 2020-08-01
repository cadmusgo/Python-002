# -*- coding: utf-8 -*-
from collections import defaultdict
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import random


class RandomProxyMiddleDownloaderMiddleware(HttpProxyMiddleware):

    def __init__(self, auth_encoding='utf-8', proxy_list=None):
        self.proxies = defaultdict(list)
        for proxy in proxy_list:
            parse = urlparse(proxy)
            self.proxies[parse.scheme].append(proxy)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('HTTPS_PROXY_LIST'):
            raise NotConfigured

        http_proxy_list = crawler.settings.get('HTTPS_PROXY_LIST')
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'utf-8')
        return cls(auth_encoding, http_proxy_list)

    def _set_proxy(self, request, scheme):
        proxy = random.choice(self.proxies[scheme])
        request.meta['proxy'] = proxy

    def process_exception(self, request, exception, spider):
        print(exception)

# class MaoyanDownloaderMiddleware:
#
#     def __init__(self, proxy_url=None):
#         self.proxy_url = proxy_url
#         print(proxy_url)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         if not crawler.settings.get('DYNAMIC_PROXY_URL'):
#             raise NotConfigured
#
#         proxy_url = crawler.settings.get('DYNAMIC_PROXY_URL')
#         s = cls(proxy_url)
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         request.meta['proxy'] = 'https://206.198.131.172:80'
#         # request.meta['proxy'] = random.choice(self.proxies["http"])
#         print(request.meta['proxy'])
#
#     def process_exception(self, request, exception, spider):
#         pass
#
#     def spider_opened(self, spider):
#         self.proxies = self.get_proxies()
#
#     def get_proxies(self):
#         r = requests.get(self.proxy_url)
#         proxies = json.loads(r.text)['data']['data']
#
#         proxy_list = defaultdict(list)
#         for proxy in proxies:
#             proxy_list[proxy['protocol']].append(f'{proxy["protocol"]}://{proxy["ip"]}:{proxy["port"]}')
#
#         return proxy_list
