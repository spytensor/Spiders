# -*- coding: utf-8 -*-
import scrapy
from leifeng.items import LeifengItem
import time

class LeifengwangSpider(scrapy.Spider):
    name = 'leifengWang'
    #allowed_domains = ['https://www.leiphone.com']
    #start_urls = ['https://www.leiphone.com/category/ai/page/1']


    def start_requests(self):

        categories = ["ai", "transportation", "sponsor", "aijuejinzhi",
                      "fintech", "aihealth", "letshome", "arvr", "robot",
                      "yanxishe", "/weiwu", "iot"]

        for category in categories:
            for i in range(1, 40):
                requ_url = "https://www.leiphone.com/category/{}/page/".format(category) + str(i)
                yield scrapy.http.Request(url=requ_url, callback=self.parse)

    def parse(self, response):

        urls = response.xpath("//a[@class='headTit']/@href").extract()
        item = LeifengItem()

        for url in urls:
            yield scrapy.http.Request(url=url,meta={"item":item},callback=self.parse_detail)
            #print(item)

    def parse_detail(self,response):
        item = response.meta["item"]
        titles = response.xpath("//h1[@class='headTit']/text()").extract()[0].strip()
        author = response.xpath("//td[@class='aut']/a/text()").extract()[0].strip()
        url = response.xpath("//div[@class='lphArticle-detail']/@data-article_url").extract()[0]
        publishTime = response.xpath("//td[@class='time']/text()").extract()[0].strip()
        articleHead = response.xpath("//div[@class='article-lead']/text()[2]").extract()[0].strip()
        category = response.xpath("/html/body/div[2]/div/a[2]/text()").extract()[0]
        item["category"] = category
        item["title"] = titles
        item["author"] = author
        item["url"] = url
        item["publishTime"] = publishTime
        item["articleHead"] = articleHead
        item["_id"] = time.time()

        yield item