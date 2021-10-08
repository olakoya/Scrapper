from bs4 import BeautifulSoup as bs
import requests
import argparse

cookie = {
    'session-id': '132-8218184-9440318'
}

HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})

# search_query = input("please enter an item: ") 
def scrapper(search_query):
    for i in range(1,8):

        URL = f"https://www.amazon.com/s?k={search_query}&page={i}"
        site = requests.get(URL, headers = HEADERS, cookies = cookie)
        response = site.text

        soup = bs(response, 'html.parser')
        
        products = soup.find_all('div',{'data-component-type':'s-search-result'})

        for product in products:
            print(product.text)
       
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('search', help='enter a search item', type=str)
    args = parser.parse_args()
    scrapper(args.search)