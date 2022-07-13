import scrapy


class CountriesSpiderSpider(scrapy.Spider):
    name = 'countries_spider'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/']

    def parse(self, response):
        pass
