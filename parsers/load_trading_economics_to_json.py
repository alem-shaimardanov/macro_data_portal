import json
import scrapy

################### EXAMPLE 1 ####################
# class MySpider(scrapy.Spider):
#     name = 'example.com'
#     allowed_domains = ['example.com']
#     start_urls = [
#         'http://www.example.com/1.html',
#         'http://www.example.com/2.html',
#         'http://www.example.com/3.html',
#     ]

#     def parse(self, response):
#         for h3 in response.xpath('//h3').getall():
#             yield {"title": h3}

#         for href in response.xpath('//a/@href').getall():
#             yield scrapy.Request(response.urljoin(href), self.parse)


################### EXAMPLE 2 ####################
# class SuperSpider(CrawlSpider):
#     name = 'spider'
#     allowed_domains = ['quotes.toscrape.com']
#     start_urls = ['http://quotes.toscrape.com/']
#     base_url = 'http://quotes.toscrape.com'
#     rules = [Rule(LinkExtractor(allow = 'page/', deny='tag/'),
#                   callback='parse_filter_book', follow=True)]
 
#     def parse_filter_book(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'Author': quote.xpath('.//span/a/@href').get(),
#                 'Quote': quote.xpath('.//span[@class= "text"]/text()').get(),

