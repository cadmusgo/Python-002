# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class MaoyanMovieSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    # start_urls = ['http://httpbin.org/get']

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

        yield  dict(
            title=title,
            movie_type=movie_type,
            movie_time=movie_time
        )

# strip text
def stripText(text):
    return text.strip().replace('类型:', '').replace(' ', '').replace('\n', ' ').replace('\r', '')


if __name__ == "__main__":
    html = ''
    with open('D:\github\_my\Python-002\week01\sample.html', 'r', encoding='utf-8') as f:
        html = f.read()
    y = parse_item(html)
    print(list(y))

