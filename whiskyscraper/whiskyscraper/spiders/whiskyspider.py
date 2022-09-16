import scrapy
from whiskyscraper.items import WhiskyscraperItem


class WhiskeySpider(scrapy.Spider):
    name = "whiskey"
    start_urls = ["https://www.whiskyshop.com/single-malt-scotch-whisky?item_availability=In+Stock"]

    def parse(self, response):
        # Instantiate item object
        item = WhiskyscraperItem()
        
        # Scrape name, price and link from each item
        for product in response.css("div.product-item-info"):
            item["name"] = product.css("a.product-item-link::text").get(),
            item["price"] = product.css("span.price::text").get().replace("£", ""),
            item["link"] = product.css("a.product-item-link").attrib["href"],

            yield item

        # Go to next page and call parse func
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
