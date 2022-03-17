import scrapy
from ..items import TradingEconomicsItem

class QuoteSpider(scrapy.Spider):
    # Give the name to a crawler
    name = 'currency'
    start_urls = ['https://tradingeconomics.com/kazakhstan/currency']

    def parse(self, response):
        # Create an object of class TradingEconomicsItem class
        items = TradingEconomicsItem()

        # Load all tables from the webpage
        all_tables = response.xpath('//*[@class="table-responsive markets2 market-border"]')

        # Load the KZT table from the webpage
        table = all_tables.xpath('.//div[2]//table[@class="table table-hover sortable-theme-minimal table-heatmap"]//tr')
        

        # for row in table:
        #     symbol = row.xpath('.//td[1]//a//b/text()').get()
        #     price = row.xpath('.//td[2]/text()').get()
        #     difference = row.xpath('.//td[4]/text()').get()
        #     day_difference = row.xpath('.//td[5]/text()').get()
        #     year_difference = row.xpath('.//td[6]/text()').get()
        #     date = row.xpath('.//td[7]/text()').get()


        # Loop through rows of table
        for i, row in enumerate(table):
            # If not header, run the following block of code
            if i > 0:
                symbol = row.xpath('.//td[1]//a//b/text()').get()
                price = row.xpath('.//td[2]/text()').get()
                difference = row.xpath('.//td[4]/text()').get()
                day_difference = row.xpath('.//td[5]/text()').get()
                year_difference = row.xpath('.//td[6]/text()').get()
                date = row.xpath('.//td[7]/text()').get()
                
                # Add the previous 5 values into 'items' dictionary
                items['symbol'] = symbol
                items['price'] = price
                items['difference'] = difference
                items['day_difference'] = day_difference
                items['year_difference'] = year_difference
                items['date'] = date

                yield items
            
            # If the row is the header, skip it
            else:
                continue


            # Don't be complacent.