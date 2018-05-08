# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NprnewsItem(scrapy.Item):
    # 1. 新闻标题
    newsTitle = scrapy.Field()
    # 2. 所属网站
    newsFrom = scrapy.Field()
    # 3. 新闻作者
    newsAuthor = scrapy.Field()
    # 4. 发布时间
    PublishTime = scrapy.Field()
    # 5. 新闻URL
    newsUrl = scrapy.Field()
    # 6. 新闻类别
    newsCategory = scrapy.Field()
    # 7. 新闻文本
    newsContext = scrapy.Field()
    # 8. 新闻图片url
    imgUrl = scrapy.Field()
    # 9. 图片描述
    imgDes = scrapy.Field()