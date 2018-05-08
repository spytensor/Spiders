# -*- coding: utf-8 -*-
import scrapy
from nprNews.items import NprnewsItem

class NprSpider(scrapy.Spider):
    name = 'npr'
    start_urls = ['https://www.npr.org/sections/thetwo-way/',
                  'https://www.npr.org/sections/money/',
                  'https://www.npr.org/sections/alltechconsidered/',
                  'https://www.npr.org/sections/13.7/',
                  'https://www.npr.org/sections/health-shots/',
                  'https://www.npr.org/sections/codeswitch/']

    def parse(self, response):
        #1.解析一级界面，保存二级界面的url，并发送请求
        try:
            urls = response.xpath("//article[@class='item has-image']//h2/a/@href").extract()

            for url in urls:
                item = NprnewsItem()
                item["newsUrl"] = url
                yield scrapy.Request(url=url,meta={"item":item},callback=self.parse_detail)
        except:
            pass

    def parse_detail(self,response):
        try:
            #2. 对二级界面进行解析，保存需要的信息
            item = response.meta["item"]
            #2.1 新闻来源
            newsFrom = self.name
            #2.2 新闻标题
            newsTitle = response.xpath("//h1/text()").extract()[0]
            #2.3 新闻类别
            newsCategory = item["newsUrl"].split("/")[4]
            #2.4 发布时间
            publishTime = response.xpath("//time/span/text()").extract()
            PublishTime = publishTime[1] + " | " + publishTime[0]
            #2.5 所含图片
            imgurl = response.xpath("//div[@class='imagewrap']/img/@src").extract()[0]
            imgUrl = "https:"+imgurl
            #2.6 图片描述
            imgDes = response.xpath("//div[@class='caption']/p/text()").extract()[0].strip()
            #2.7 新闻内容
            newsContext = response.xpath("//div[@id='storytext']/p/text()").extract()

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