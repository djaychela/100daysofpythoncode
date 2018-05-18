import api


def main():

    keyword = input('Keyword of title search: ')
    results = api.find_movie_by_title(keyword)
    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.imdb_code} : {r.title} - IMDB Score {r.imdb_score}")


if __name__ == '__main__':
    main()
