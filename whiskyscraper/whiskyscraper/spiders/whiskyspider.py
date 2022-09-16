import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class WhiskeySpider(scrapy.Spider):
    name = "whiskey"
    start_urls = ["https://www.whiskyshop.com/single-malt-scotch-whisky?item_availability=In+Stock"]

    def parse(self, response):
        
        # Iterate through each item
        for product in response.css("div.product-item-info"):
            # Instantiate loader object
            loader = ItemLoader(item=WhiskyscraperItem(), selector=product)
            
            # Scrape items name, price and link with CSS Selectors and pass
            # them to ItemLoader for being processed in items.py
            loader.add_css("name", "a.product-item-link")
            loader.add_css("price", "span.price")
            loader.add_css("link", "a.product-item-link::atrr(href)")

            yield loader.load_item()  # sends scrape data to items.py

        # Go to next page and call parse func
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
