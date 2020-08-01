# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


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
        movie_type = strip_text(movie_type)

        # 電影時刻
        movie_time = ''.join(x for x in movie.xpath('.//div[@class="movie-hover-info"]/div[4]/text()').extract())
        movie_time = strip_text(movie_time)
        yield MaoyanItem(
            title=title,
            type=movie_type,
            time=movie_time
        )

    # strip text


def strip_text(text):
    return text.strip().replace('类型:', '').replace(' ', '').replace('\n', ' ').replace('\r', '')