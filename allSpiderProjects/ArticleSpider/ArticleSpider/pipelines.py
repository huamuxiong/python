# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json
import MySQLdb
import MySQLdb.cursors

from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    """存json文件"""
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()


class MysqlPipeline(object):
    """同步插入数据库，随着爬取的数据库越来越大，而且爬取的速度远远
    比插入数据库的速度要快，偏偏execute提交数据库的时候如果不执行完
    是不会往下执行的，很浪费时间"""
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root3306', 'article_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):

        insert_sql = """insert into jobbole_article(title, ftime, url, url_object_id,  zan_count) 
            values (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['ftime'], item['url'], item['url_object_id'], item['zan_count']))
        self.conn.commit()


class MysqlTwistedPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings['MYSQL_HOST'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            db = settings['MYSQL_DBNAME'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变为异步执行
        self.dbpool.runInteraction(self.do_insert, item)
        self.addErrback(self.handle_error)  # 处理异常

    def handle_error(self, failure):
        """处理异步插入异常"""
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = """insert into jobbole_article(title, ftime, url, url_object_id,  zan_count) 
                    values (%s, %s, %s, %s, %s)
                """
        cursor.execute(insert_sql,
                            (item['title'], item['ftime'], item['url'], item['url_object_id'], item['zan_count']))


class ArticleImagePipeline(ImagesPipeline):
    """处理图片"""
    def item_completed(self, results, item, info):
        if 'front_img_path' in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_img_path'] = image_file_path
        return item
