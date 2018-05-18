import requests, bs4, pickle, collections
import cProfile
profiler = cProfile.Profile()
profiler.disable()

url = "https://www.gumtree.com/search?search_category=cars&search_location=bh119la&q=golf&distance=30&max_price=500&seller_type=private"

Advert = collections.namedtuple('Advert', 'title, miles, price')


def get_page(file_url):
    try:
        with open('data/gumtree.pyc', 'rb') as file:
            page_raw = pickle.load(file)
            print('*** file loaded ***')
    except FileNotFoundError:
        page_raw = requests.get(file_url)
        page_raw.raise_for_status()
        with open('data/gumtree.pyc', 'wb') as file:
            pickle.dump(page_raw, file)
            print('*** file saved ***')

    return page_raw


def scrape_page(page):
    profiler.enable()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    html_title_list = soup.select('.listing-title')
    html_price_list = soup.select('.listing-price')
    html_mileage = soup.select('ul.listing-attributes > li > span[itemprop="mileageFromOdometer"]')
    title_list = [headers.getText().strip('\n') for headers in html_title_list]
    price_list = [headers.getText().strip('\n') for headers in html_price_list]
    miles_list = [miles.getText() for miles in html_mileage]
    title_list = clean_list(title_list)
    price_list = clean_list(price_list)
    title_price = zip(title_list, miles_list, price_list)
    items = []
    for title, miles, price in title_price:
        if title[0] == '&':
            continue
        current_item = Advert(title, miles, price)
        items.append(current_item)
    profiler.disable()
    return items


def clean_list(input_list):
    output_list = [item.strip('\n') for item in input_list if item.strip(' ')[0] != '&']
    return output_list


def report(items_list):
    for item in items_list:
        print(f'Ad: {item.title} - {item.miles} - {item.price}')


def print_html(raw_page):
    print(raw_page.text)
    return


def main():

    page = get_page(url)
    items_list = scrape_page(page)
    report(items_list)

    profiler.print_stats(sort='cumtime')

if __name__ == '__main__':
    main()
