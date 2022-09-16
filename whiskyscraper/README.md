# Complete Beginner Example Web Scraping with Scrapy
https://www.youtube.com/watch?v=s4jtkzHhLzY&t=247s

> Comment: project can't be finished as in the video because the page needs to be rendered (Enable JavaScript and cookies to continue)

>Fix: use scrapy-playwright

> Tip: use the **scrapy shell** to interrogate the html 

## Scrapy Shell
Start:
`scrapy shell`

Use fetch command:
`> fetch("https://www.whiskyshop.com/single-malt-scotch-whisky?item_availability=In+Stock")`

The response is automatically saved in a response variable 
`response`

Manage response which contain the html by using CSS Selectors:
- Select all matched elements (obj):
`response.css("div.product-item-info")`

- Select first matched item (html) 
`response.css("div.product-item-info").get()` 

- Select list of all matched items (html)
`response.css("div.product-item-info").get_all()` 

- Iterate through elements
`products = response.css("div.product-item-info")`
`len(products)`
