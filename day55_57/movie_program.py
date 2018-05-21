import movie_client
import requests


def main():
    val = 'RUN'
    menu_lookup = {'s': 'movie_search()', 'd': 'director_search()', 'i': 'imdb_search("search","tt00000000")',
                   'q': 'quit()'}
    while val:
        val = input('[s]earch, [d]irector, [i]mdb code or [q]uit?').lower()
        if val in menu_lookup.keys():
            exec(menu_lookup[val])


def movie_search():
    svc = movie_client.MovieClient()
    search_term = input('Enter a term to search for: ')
    result = perform_search(svc, search_term, 'search')
    if result:
        movies = result.get('hits')
        for idx, movie in enumerate(movies, 1):
            print(f"{idx} : {movie['title']} ({movie['year']})")
        details = input('Enter a number to see details of the movie, or any other key to return to the main menu: ')
        if details.isnumeric():
            details = int(details)
            if details in range(idx):
                imdb_search('view', movies[details-1].get('imdb_code'))
        else:
            return


def director_search():
    svc = movie_client.MovieClient()
    director_name = input('Enter a director to search for: ')
    result = perform_search(svc, director_name, 'by_director')
    if result:
        directors = result.get('hits')
        for idx, director in enumerate(directors, 1):
            print(f"{idx} : {director['title']} ({director['year']}) - dir: {director['director']}")
        details = input('Enter a number to see details of the movie, or any other key to return to the main menu: ')
        if details.isnumeric():
            details = int(details)
            if details in range(idx):
                imdb_search('view', directors[details - 1].get('imdb_code'))
        else:
            return


def imdb_search(mode, imdb_number):
    svc = movie_client.MovieClient()
    if mode == 'search':
        imdb_number = input('Enter an IMDB code (including tt): ')
    result = perform_search(svc, imdb_number, 'by_imdb_number')
    if result:
        print(f"{result['title']} ({result['year']}) {result['duration']} mins. - dir: {result['director']}")
        print(f"Rating: {result['rating']} Score: {result['imdb_score']}")


def quit():
    print('exiting...')
    exit()


def perform_search(svc, search_term, search_type):
    search_action = f"svc.{search_type}(search_term)"
    try:
        resp = eval(search_action)
    except requests.exceptions.ConnectionError:
        print('No connection.... aborting.')
        return
    result = resp.json()
    return result


if __name__ == '__main__':
    main()
