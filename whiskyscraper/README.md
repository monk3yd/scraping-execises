# Complete Beginner Example Web Scraping with Scrapy
https://www.youtube.com/watch?v=s4jtkzHhLzY&t=247s

> Comment: project can't be finished as in the video because the page needs to be rendered (Enable JavaScript and cookies to continue)

>Fix: use scrapy-playwright

> Tip: use the **scrapy shell** to interrogate the html 
> Tip: Workflow when web scraping: request-parse-output/extract-transform-load

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
`response.css("div.product-item-info").getall()` 

- Iterate through elements
`products = response.css("div.product-item-info")`
`len(products)`

- Select link of product
`products.css("a.product-item-link").get()`

- Get text from link element
`products.css("a.product-item-link::text").get()`

- Get list of text items from all link elements in page
`products.css("a.product-item-link::text").getall()`

- Get text from link element and replace char
`products.css("span.price::text").get().replace("£", "")`

- Get href from link element
`products.css("a.product-item-link").attrib["href"]`


## Assemblying Spider
1. Create Spider
2. Parse response using .supra data
3. Find next button
4. Iterate through all pages

