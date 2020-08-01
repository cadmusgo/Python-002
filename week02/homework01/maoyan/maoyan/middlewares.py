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
