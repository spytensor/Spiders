# -*- coding: utf-8 -*-
import scrapy
from bossZhipin.items import BosszhipinItem
import time

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['https://www.zhipin.com']
    #start_urls = ['https://www.zhipin.com/c101010100-p100117/?page=1&ka=page-1']

    #第一步、生成每页的url
    def start_requests(self):
        categories = {
            "机器学习": "p101301",
            "深度学习": "p101302",
            "图像算法": "p101303",
            "图像处理": "p101304",
            "语音识别": "p101305",
            "图像识别": "p101306",
            "算法研究员": "p101307",
            "自然语言处理": "p100117"
        }
        for category in categories:
            for i in range(1,11):
                url = "https://www.zhipin.com/c101010100-{}/?page={}&ka=page-{}".format(category,i,i)
                yield scrapy.Request(url,callback=self.parse)
    #第二步、获取每个职位的url
    def parse(self, response):
        item = BosszhipinItem()
        try:
            titles = response.xpath("//div[@class='job-title']//text()").extract()
            job_urls = response.xpath("//h3[@class='name']/a/@href").extract()
            salaries = response.xpath("//span[@class='red']/text()").extract()
        except:
            pass
        for title,job_url,salary in zip(titles,job_urls,salaries):
            item["job_title"] = title
            item["job_url"] = "https://www.zhipin.com"+job_url
            item["salary"] = salary

            yield scrapy.Request(url=item["job_url"],meta={"item":item},callback=self.parse_detail)

    def parse_detail(self,response):
        item = response.meta["item"]
        try:
            #1.薪资待遇,出现点问题，在上一级进行保存
            #salary = response.xpath("//*[@id=\"main\"]/div[1]/div/div/div[2]/div[2]/span/text()").extract()[0].replace("K","000")
            #2.工作经验
            experience = response.xpath("//div[@class='job-primary detail-box']//div[@class='info-primary']/p/text()[2]").extract()[0][3:]
            #3.学历要求
            education = response.xpath("//div[@class='job-primary detail-box']//div[@class='info-primary']/p/text()[3]").extract()[0][3:]
            #4.所拥有标签
            tags = response.xpath("//div[@class='job-tags']/span/text()").extract()
            #5.发布时间
            publish_time = response.xpath("//span[@class='time']/text()").extract()
            #6.工作地点
            location = response.xpath("//div[@class='location-address']/text()").extract()
            #7.企业名称
            company_name = response.xpath("//h3[@class='name']/a/text()").extract()
            #8.企业类型
            company_type = response.xpath("//div[@class='info-company']/p/a/text()").extract()
            #9.企业规模
            company_size = response.xpath("//div[@class='info-company']/p/text()[2]").extract()
            #10.融资情况
            finacing = response.xpath("//*[@id=\"main\"]/div[1]/div/div/div[3]/p[1]/text()[1]").extract()
            #11.HR姓名
            hr_name = response.xpath("//h2/text()").extract()
            #12.HR职业
            hr_profession = response.xpath("//*[@id=\"main\"]/div[3]/div/div[2]/div[2]/p/text()[1]").extract()
            #13.HR在线情况
            hr_online_time = response.xpath("//*[@id=\"main\"]/div[3]/div/div[2]/div[2]/p/text()[2]").extract()
            #14.职位描述
            job_description = response.xpath("//*[@id=\"main\"]/div[3]/div/div[2]/div[3]/div[1]/div/text()").extract()
            job_description = [i.strip() for i in job_description]
        except:
            pass
        item["experience"] = experience
        item["education"] = education
        item["tags"] = tags
        item["publish_time"] = publish_time
        item["location"] = location
        item["company_name"] = company_name
        item["company_type"] = company_type
        item["company_size"] = company_size
        item["finacing"] = finacing
        item["hr_name"] = hr_name
        item["hr_profession"] = hr_profession
        item["hr_online_time"] = hr_online_time
        item["job_description"] = job_description
        item["_id"] = time.time()
        yield item
