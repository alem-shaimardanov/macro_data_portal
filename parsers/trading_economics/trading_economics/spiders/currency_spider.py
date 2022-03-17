import scrapy
from ..items import TradingEconomicsItem

class QuoteSpider(scrapy.Spider):
    # Give the name to a crawler
    name = 'currency'
    start_urls = ['https://tradingeconomics.com/kazakhstan/currency']

    def parse(self, response):
        # Create an object of class TradingEconomicsItem class
        items = TradingEconomicsItem()

        # Load the table from the webpage
        table = response.xpath('//*[@class="table table-hover table-heatmap"]')

        # Convert the table into a list of rows by accessing every 'tr' tag
        rows = table.xpath('//tr')


        # Loop through rows of table
        for i, row in enumerate(rows):
            # If not header, run the following block of code
            if i > 0:
                country_name = row.xpath('.//td[1]//a/text()').get().rstrip().strip()
                last_value = row.xpath('.//td[2]//span/text()').get()

                # if last_value is None, use another way to access the value
                if last_value is None:
                    last_value = row.xpath('.//td[2]/text()').get()
                
                prev_value = row.xpath('.//td[3]//span/text()').get()

                # if prev_value is None, use another way to access the value
                if prev_value is None:
                    prev_value = row.xpath('.//td[3]/text()').get()
                

                reference = row.xpath('.//td[4]//span/text()').get()
                units = row.xpath('.//td[5]/text()').get()
                
                # Add the previous 5 values into 'items' dictionary
                items['country_name'] = country_name
                items['last_value'] = last_value
                items['prev_value'] = prev_value
                items['reference'] = reference
                items['units'] = units

                yield items
            
            # If the row is the header, skip it
            else:
                continue