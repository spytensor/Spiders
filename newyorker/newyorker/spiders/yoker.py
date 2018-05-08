# -*- coding: utf-8 -*-
import scrapy
from newyorker.items import NewyorkerItem

class YokerSpider(scrapy.Spider):
    name = 'yoker'
    #allowed_domains = ['https://www.newyorker.com']
    #start_urls = ['https://www.newyorker.com/']
    def start_requests(self):
        #1. 生成一级页面链接，并发送请求
        for page in range(1,15):
            url = "https://www.newyorker.com/latest/news/page/" + str(page)
            yield scrapy.http.Request(url=url,callback=self.parse)

    def parse(self, response):
        #2. 解析一级页面信息，获取二级页面链接，并发送请求
        urls = response.xpath("//div[@class='River__riverItemContent___2hXMG']/a/@href").extract()
        for url in urls:
            item = NewyorkerItem()
            item["newsUrl"] = "https://www.newyorker.com"+url
            yield scrapy.http.Request(url=item["newsUrl"],meta={"item":item},callback=self.parse_detail)

    def parse_detail(self,response):
        #3. 解析二级页面，获取所需信息
        item = response.meta["item"]

        try:
            #3.1 新闻来源
            newsFrom = "newyorker"
            #3.2 新闻类别
            newsCategory = response.xpath("//div[@class='ArticleHeader__rubric___3YLRT']/a/text()").extract()[0]
            #3.3 发布时间
            PublishTime = response.xpath("//p[@class='ArticleTimestamp__timestamp___1klks ']/text()").extract()[0]
            #3.4 新闻图片
            imgUrl = response.xpath("//figure/div/div[2]/div/picture/img/@src").extract()[0]
            #3.5 图片描述
            imgDes = response.xpath("//figure/figcaption/span/div/p/text()").extract()
            #3.6 新闻文本
            newsContext = response.xpath("//div[@class='SectionBreak__sectionBreak___1ppA7']/p/text()").extract()
            #3.7 新闻标题
            newsTitle = response.xpath("//h1/text()").extract()[0]

            item["newsFrom"] = newsFrom
            item["newsCategory"] = newsCategory
            item["newsTitle"] = newsTitle
            item["PublishTime"] = PublishTime
            item["imgUrl"] = imgUrl
            item["imgDes"] = imgDes
            item["newsContext"] = newsContext

            yield item
        except:
            pass