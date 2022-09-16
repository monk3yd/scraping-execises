# https://www.youtube.com/watch?v=IDhuUpeF1n0
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    # no session 0:00:21.326450
    start = datetime.now()
    for x in range(1, 21):
        get_title(x)
    finish = datetime.now() - start
    print(finish)

    # session
    start = datetime.now()
    session = requests.Session()
    for x in range(1, 21):
        get_title_session(x, session)
    finish = datetime.now() - start
    print(finish)

def get_title(n):
    url = f"https://scrapethissite.com/pages/forms/?page_num={n}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.text)
    return

def get_title_session(n, session):
    url = f"https://scrapethissite.com/pages/forms/?page_num={n}"
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.text)
    return


if __name__ == "__main__":
    main()
