import requests
import re
from bs4 import BeautifulSoup

def main():
    _titles = []
    m = requests.get('http://goodreads.com/books.html')
    soup = BeautifulSoup(m.text, 'html.parser')
    a = soup.find_all('a', href = True)
    cnt = 0
    for i in a:
        ml = requests.get('http://goodreads.com/' + i['href'])
        soup1 = BeautifulSoup(ml.text, 'html.parser')
        span = soup1.find_all('span', {'itemprop': 'name'})
        titles = [s.contents[0] for s in span]
        _titles += titles
        cnt += len(titles)
        print(cnt, end = '\r')
        if (cnt >= 10000):
            with open('titles.txt', 'a+') as f:
                for i in _titles:
                    f.write(i + '\n')
            _titles = []
            cnt = 0
if __name__ == '__main__':
    main()