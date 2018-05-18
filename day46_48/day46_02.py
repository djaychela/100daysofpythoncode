import requests
import bs4

url = "https://pybit.es/pages/articles.html"


def get_page():
    raw_site_page = requests.get(url)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.articleList')
    header_list = [headers.getText() for headers in html_header_list]
    return header_list


def search(site):
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    list_elements = soup.main.ul.find_all('li')
    li_list = [li.text for li in list_elements]
    return li_list


def main():
    site = get_page()
    returned = search(site)
    # returned = scrape(site)
    for item in returned:
        print(item)


if __name__ == '__main__':
    main()
