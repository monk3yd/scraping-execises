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
    # selector = ".header.container-fluid"  # multiple class selector
    # selector = "ol li"  # multiple element child selector
    # selector = "ol.row li"  # multiple class-element child selector
    # selector = "ol.row + div"  # multiple class-element next (immediately after) selector

    # Attribute selectors
    selector = "div[role=alert]"
    selector = "[type=submit]"
    selector = "a[href]"
    selector = "img[src]"

    print(response.html.find(selector))

    ...


if __name__ == "__main__":
    main()
