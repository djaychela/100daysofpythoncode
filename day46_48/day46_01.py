import requests
import bs4

url = "https://pybit.es/pages/projects.html"


def get_page():
    raw_site_page = requests.get(url)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')
    header_list = [headers.getText() for headers in html_header_list]
    for headers in header_list:
        print(headers)


def main():
    site = get_page()
    scrape(site)


if __name__ == '__main__':
    main()
