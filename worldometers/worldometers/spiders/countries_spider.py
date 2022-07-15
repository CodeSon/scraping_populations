from os import link
import scrapy


class CountriesSpiderSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
   
        
        countries = response.xpath("//td/a")
        for country in countries:

            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

        # To return the scrapy data,return it as a dictionary

       # absolute_url = f"https://www.worldometers.info{link}"

        yield response.follow(url=link)
