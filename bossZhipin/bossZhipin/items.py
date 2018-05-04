# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义所要爬取的内容
    #1. 薪资待遇
    salary = scrapy.Field()
    #2. 工作经验
    experience = scrapy.Field()
    #3. 学历
    education = scrapy.Field()
    #4. 标签
    tags = scrapy.Field()
    #5. 发布时间
    publish_time = scrapy.Field()
    #6. 工作地点
    location = scrapy.Field()
    #7. 企业名称
    company_name = scrapy.Field()
    #8. 企业类型
    company_type = scrapy.Field()
    #9. 企业规模
    company_size = scrapy.Field()
    #10. 企业融资情况
    finacing = scrapy.Field()
    #11. HR姓名
    hr_name = scrapy.Field()
    #12. HR职业
    hr_profession = scrapy.Field()
    #13. HR在线情况
    hr_online_time = scrapy.Field()
    #14. 工作职位描述
    job_description = scrapy.Field()
    #15. 详情页面
    job_url = scrapy.Field()
    #16. 工作标题
    job_title = scrapy.Field()
    #17.mongodb所需
    _id = scrapy.Field()