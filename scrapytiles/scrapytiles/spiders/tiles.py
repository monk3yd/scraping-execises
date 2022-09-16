import scrapy


class TilesSpider(scrapy.Spider):
    name = "tiles"
    allowed_domains = ["magnatiles.com/"]
    start_urls = ["https://magnatiles.com/products/page/1/"]


    def parse(self, response):
        ...
