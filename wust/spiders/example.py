# -*- coding: utf-8 -*-
import scrapy
import re
from wust.items import WustItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['wust.91wllm.com']
    start_urls = ['https://wust.91wllm.com/teachin/index']

    def parse(self, response):
        res = response.css('.infoBox').css('.infoList').css('a::attr(href)').extract()
        for i in res:
            url = 'https://wust.91wllm.com' + i
            yield scrapy.Request(url=url, callback=self.pageParse)
        nextURL = response.css('#yw0 > li.next > a::attr(href)').extract()
        # print(res)
        yield scrapy.Request(url=nextURL[0], callback=self.parse)
        # for i in res:
        #     print(i)

    def pageParse(self, response):
        requireMajor = response.css(
            'body > div.container > div.container.clearfix > div > div.details-table > div > table > tbody > tr > td > div > div::attr(title)').extract()
        position = response.css(
            'body > div.container > div.container.clearfix > div > div.details-table > div > table > tbody > tr')
        for i in range(len(requireMajor)):
            if re.match(".*电子信息工程.*", requireMajor[i]) is not None or re.match(".*机械工程.*", requireMajor[i]) is not None:
                major = None
                if re.match(".*电子信息工程.*", requireMajor[i]) is not None and re.match(".*机械工程.*", requireMajor[i]) is None:
                    major = "电子信息工程"

                if re.match(".*电子信息工程.*", requireMajor[i]) is None and re.match(".*机械工程.*", requireMajor[i]) is not None:
                    major = "机械工程"

                if re.match(".*电子信息工程.*", requireMajor[i]) is not None and re.match(".*机械工程.*", requireMajor[i]) is not None:
                    major = "电子信息工程 & 机械工程"
                companyName = response.css('.name.text-primary').css('a::text').extract()[0]
                time = response.css(
                    'body > div.container > div.container.clearfix > div > div.details-list > ul:nth-child(2) > li:nth-child(1)').css(
                    'span::text').extract()[0]
                address = response.css(
                    'body > div.container > div.container.clearfix > div > div.details-list > ul:nth-child(2) > li:nth-child(2) > span::text').extract()[
                    0]
                tel = response.css(
                    'body > div.container > div.container.clearfix > div > div.details-list > ul:nth-child(2) > li:nth-child(6) > span::text').extract()[
                    0].strip()
                positionName = position.css('td:nth-child(2) > div > div > a::attr(title)').extract()[i]
                positionSalary = position.css('td:nth-child(2) > div > div > ul > li.text-warning > b::text').extract()[i]
                item = WustItem()
                item['url'] = response.url
                item['companyName'] = companyName
                item['time'] = time
                item['address'] = address
                item['telephone'] = tel
                item['positionSalary'] = positionSalary
                item['positionName'] = positionName
                item['major'] = major
                yield item
