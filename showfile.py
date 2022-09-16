# Use CSS Selectors for web scraping
# https://www.youtube.com/watch?v=hkDAW7hhEYU

from requests_html import HTMLSession


def main():
    session = HTMLSession()
    response = session.get("https://books.toscrape.com/")

    # General selectors
    # selector = "#default"  # id selector
    # selector = ".default"  # class selector
    # selector = "div"  # element selector
    
    # More specific selectors

    print(response.html.find(selector))

    ...


if __name__ == "__main__":
    main()
