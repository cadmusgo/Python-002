# -*- coding: utf-8 -*-
"""
作業要求:
    使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
    猫眼电影网址： https://maoyan.com/films?showType=3
    要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

"""
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector
from pathlib import Path
import os

class MaoyanMovieSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        return parse_item(response.text)


# module method
def parse_item(html):
    movies = Selector(text=html).xpath('//div[@class="movie-item-hover"]')
    # list = []
    for movie in movies:
        # title
        title = movie.xpath('.//div[@class="movie-hover-title"][1]/span/text()').extract_first()

        # # 電影類型
        movie_type = ''.join(x for x in movie.xpath('.//div[@class="movie-hover-info"]/div[2]/text()').extract())
        movie_type = stripText(movie_type)

        # 電影時刻
        movie_time = ''.join(x for x in movie.xpath('.//div[@class="movie-hover-info"]/div[4]/text()').extract())
        movie_time = stripText(movie_time)
        yield MaoyanItem(
            title=title,
            type=movie_type,
            time=movie_time
        )

# strip text
def stripText(text):
    return text.strip().replace('类型:', '').replace(' ', '').replace('\n', ' ').replace('\r', '')


if __name__ == "__main__":
    html = ''
    htmlFile = os.path.join(Path(__file__).parent.parent.parent.parent,"sample.html")
    print(htmlFile)
    with open(htmlFile, 'r', encoding='utf-8') as f:
        html = f.read()
    y = parse_item(html)
    print(list(y))

