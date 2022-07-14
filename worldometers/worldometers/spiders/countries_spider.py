import scrapy


class CountriesSpiderSpider(scrapy.Spider):
    name = 'countries_spider'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        # To return the scrapy data,return it as a dictionary

        yield {
            'title' : title,
            'countries': countries
        }
