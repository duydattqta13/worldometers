import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # countries = response.xpath('//td/a')
        tables = response.xpath('//tr')

        for table in tables:
            name = table.xpath('.//td/a/text()').get()
            link = table.xpath('.//td/a/@href').get()
            population = table.xpath('.//td[3]/text()').get()
            year = table.xpath('.//td[4]/text()').get()
            net_change = table.xpath('.//td[5]/text()').get()

            yield{
        		'name': name,
        		'link': link,
                'population': population,
                'year': year,
                'net_change': net_change
        	}
        pass
