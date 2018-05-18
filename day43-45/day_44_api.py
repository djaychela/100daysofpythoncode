import requests


def search_talkpython(term):
    url = f"http://search.talkpython.fm/api/search?q={term}"
    resp = requests.get(url)
    result = resp.json()

    return result

