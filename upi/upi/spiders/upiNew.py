# -*- coding: utf-8 -*-
import scrapy
from upi.items import UpiItem


class UpinewSpider(scrapy.Spider):
    name = 'upiNew'
    #allowed_domains = ['https://www.upi.com/Top_News']
    start_urls = ['https://www.upi.com/Top_News/',
                  'https://www.upi.com/Entertainment_News/',
                  'https://www.upi.com/Odd_News/',
                  'https://www.upi.com/Defense-News/',
                  'https://www.upi.com/Energy-News/',
                  'https://www.upi.com/Sports_News/',
                  'https://www.upi.com/Science_News/',
                  'https://www.upi.com/Health_News/',
                  'https://www.upi.com/News_Photos/']

    def parse(self, response):
        urls = response.xpath("//div[@class='upi_item']/a/@href").extract()
        for url in urls:
            item = UpiItem()
            item["newsUrl"] = url
            yield scrapy.http.Request(url,meta={"item":item},callback=self.parse_detail)

    def parse_detail(self,response):
        #2. 解析二级网页，获取所需信息
        item = response.meta["item"]

        #2.1 新闻网站
        newsFrom = "UPI"
        #2.2 新闻类别
        try:
            newsCategory = response.xpath("//div[@class='breadcrumb grey']/a[3]/text()").extract()[0]
        except:
            newsCategory = response.xpath("//div[@class='breadcrumb grey']/a[2]/text()").extract()[0]
        try:
            #2.3 发布时间
            try:
                publishTime = response.xpath("//div[@class='meta grey']/text()").extract()
                PublishTimes = []
                for OrigTime in publishTime:
                    if OrigTime == "\n\t\t\t\t" or OrigTime == "\t\t\t\t":
                        pass
                    else:
                        PublishTimes.append(OrigTime)
                PublishTime = PublishTimes[1].split("|")[1].strip()
            except:
                publishTime = response.xpath("//div[@class='meta grey']/text()").extract()
                PublishTime = publishTime[0].split("|")[1].strip()
            #2.4 新闻标题
            newsTitle = response.xpath("//h1[@class='st_headline title']/text()").extract()[0]
            #2.5 新闻图片url
            imgUrl = response.xpath("//div[@class='img']/img/@src").extract()[0]
            #2.6 图片描述
            imgDes = response.xpath("//div[@class='caption']/text()").extract()[0].strip()
            #2.7 新闻内容
            newsContext = response.xpath("//div[@id='article']/p/text()").extract()

            item["newsFrom"] = newsFrom
            item["newsCategory"] = newsCategory
            item["PublishTime"] = PublishTime
            item["newsTitle"] = newsTitle
            item["imgUrl"] = imgUrl
            item["imgDes"] = imgDes
            item["newsContext"] = newsContext
            yield item
        except:
            pass

