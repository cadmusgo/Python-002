# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    def process_item(self, item, spider):
        with open('./movie-spider.csv', 'a+', encoding='utf-8') as f:
            print(f'{item["title"]},{item["movie_type"]},{item["movie_time"]}')
            f.write(f'{item["title"]},{item["movie_type"]},{item["movie_time"]}\n')

        return item
