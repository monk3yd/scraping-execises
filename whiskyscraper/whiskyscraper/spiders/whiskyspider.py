import scrapy


class WhiskeySpider(scrapy.Spider):
    name = "whiskey"
    start_urls = ["https://www.whiskyshop.com/single-malt-scotch-whisky?item_availability=In+Stock"]

    def parse(self, response):
        for product in response.css("div.product-item-info"):
            try:
                yield {
                    "name": product.css("a.product-item-link::text").get(),
                    "price": product.css("span.price::text").get().replace("£", ""),
                    "link": product.css("a.product-item-link").attrib["href"],
                }
            except:
                yield {
                    "name": product.css("a.product-item-link::text").get(),
                    "price": "sold out",
                    "link": product.css("a.product-item-link").attrib["href"],
                }
