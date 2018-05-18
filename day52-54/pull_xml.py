import requests

url='https://podcasts.files.bbci.co.uk/p02pc9x6.rss'


def main():
    r = requests.get(url)
    with open('bbc_comedy.rss', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    main()
