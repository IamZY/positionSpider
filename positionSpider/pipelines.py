# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymssql
from scrapy.conf import settings

class PositionspiderPipeline(object):
    # 保存json
    # def __init__(self):
    #     self.filename = open("zhilian.json","wb")
    #
    # def process_item(self, item, spider):
    #     # return item
    #     text = json.dumps(dict(item),ensure_ascii=False) + "\n"
    #     self.filename.write(text.encode("utf-8"))
    #
    #     return item
    #
    # def close_spider(self,spider):
    #     self.filename.close()

    # 存入数据库
    def __init__(self):
        # self.connect = pymssql.connect(
        #     host=settings["MYSQL_HOST"],
        #     db=settings["MYSQL_DBNAME"],
        #     user=settings["MYSQL_USER"],
        #     passwd=settings["MYSQL_PASSWD"],
        #     charset='utf8',
        #     use_unicode=True
        # )

        self.connect = pymssql.connect(host='127.0.0.1',
                                        user='sa',
                                        password='123456',
                                        database='Position',
                                        charset='utf8')

        self.cursor = self.connect.cursor()

    # def process_item1(self, item, spider):
    #     # 插入数据
    #     self.cursor.execute(
    #         """insert into zhilian(businessName, jobName, money , area,businessYear,education,businessPerson,businessType,position) value( %s, %s, %s, %s,%s, %s, %s, %s,%s) """,
    #         (
    #             item["businessName"],
    #             item["jobName"],
    #             item["money"],
    #             item["area"],
    #             item["businessYear"],
    #             item["education"],
    #             item["businessPerson"],
    #             item["businessType"],
    #             item["position"]
    #         )
    #     )
    #     # 提交sql语句
    #     self.connect.commit()

# def process_item2(self, item, spider):
    #     # 插入数据
    #     self.cursor.execute(
    #         """insert into 51job(businessName, jobName, money , area,businessYear,education,businessPerson,businessType,position) value( %s, %s, %s, %s,%s, %s, %s, %s,%s) """,
    #         (
    #             item["businessName"],
    #             item["jobName"],
    #             item["money"],
    #             item["area"],
    #             item["businessYear"],
    #             item["education"],
    #             item["businessPerson"],
    #             item["businessType"],
    #             item["position"]
    #         )
    #     )
    #     # 提交sql语句
    #     self.connect.commit()

    def process_item(self, item, spider):
        # 插入数据
        self.cursor.execute(
            """insert into Position(businessName, jobName, money , area,businessYear,education,businessPerson,businessType,position) values( %s, %s, %s, %s,%s, %s, %s, %s,%s) """,
            (
                item["businessName"],
                item["jobName"],
                item["money"],
                item["area"],
                item["businessYear"],
                item["education"],
                item["businessPerson"],
                item["businessType"],
                item["position"]
            )
        )
        # 提交sql语句
        self.connect.commit()