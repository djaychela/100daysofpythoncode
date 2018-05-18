import requests, json

api_url = "http://www.omdbapi.com/?apikey=91c2f6d7&"


def get_data(term='star wars', search_type='search'):
    if search_type == 'search':
        verb = 's='
    elif search_type == 'imdbID':
        verb = 'i='
    full_url = api_url + verb + term
    r = requests.get(full_url)
    text = r.content.decode('UTF-8')
    return text


def main():
    mode = 'search'
    while True:
        term = input('Enter a term to search for or e(X)it: ')
        if term.lower() == 'x':
            break
        if term.isdigit():
            response = get_data(current_info[int(term)], search_type='imdbID')
            mode = 'list'
        else:
            response = get_data(term, search_type='search')
        data = json.loads(response)
        if mode == 'search':
            current_info={}
            for idx, item in enumerate(data['Search'],1):
                print(f"{idx}: {item['Title']} ({item['Year']})")
                current_info[idx] = item['imdbID']
        else:
            print(f"{data['Title']} - {data['Year']}. Rating: {data['imdbRating']}")
            print(f"{data['Plot']}.")
            mode = 'search'


if __name__ == '__main__':
    main()
