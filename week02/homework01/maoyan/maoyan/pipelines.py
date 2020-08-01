# -*- coding: utf-8 -*-
import pymysql


class MaoyanPipeline:

    def __init__(self, db_info):
        self.db_info = db_info

    def process_item(self, item, spider):
        cur = self.conn.cursor()

        cur.execute("insert into movie(title,type,time) values(%s,%s,%s)", (item["title"], item["type"], item["time"]))
        self.conn.commit()

        return item

    @classmethod
    def from_crawler(cls, crawler):
        db_info = crawler.settings.get('DB_INFO')
        return cls(
            db_info=db_info
        )

    def open_spider(self, spider):
        self.conn = pymysql.Connect(**self.db_info)

    def close_spider(self, spider):
        self.conn.close()
