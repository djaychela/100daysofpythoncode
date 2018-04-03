import csv
import requests
from collections import OrderedDict

min_films = 4
year_cutoff = 1960
csv_url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"


def download_director_csv():
    global csv_url
    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode('utf-8')
    cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    director_csv_list = list(cr)
    return director_csv_list


def filter_director_data(director_list):
    new_list = []
    for row in director_list:
        current_line = OrderedDict()
        data_wanted = ['director_name', 'movie_title', 'title_year', 'imdb_score']
        for data in data_wanted:
            current_line[data] = row[data]
        new_list.append(current_line)
    return new_list


def create_director_dict(new_list):
    director_dict = OrderedDict()
    for entry in new_list:
        film_entry = {}
        data_wanted = ['movie_title', 'title_year', 'imdb_score']
        for data in data_wanted:
            film_entry[data] = entry[data]
        if entry['director_name'] not in director_dict.keys():
            director_dict[entry['director_name']] = [film_entry]
        else:
            director_dict[entry['director_name']].append(film_entry)
    return director_dict


def print_directors_films(director, director_dict):
    director_score = calculate_directors_score(director, director_dict)
    print('{:<25} {:>20.1f}' .format(director, director_score))
    print('{:*^46}'.format(''))
    for film in director_dict[director]:
        print('{:<4} {:<30} {:>10}'.format(film['title_year'] , film['movie_title'][:30], film['imdb_score']))
    print()


def calculate_directors_score(director, director_dict):
    director_score = 0
    total_films = 0
    for film in director_dict[director]:
        if film['title_year'] and int(film['title_year']) >= year_cutoff:
            director_score += float(film['imdb_score'])
            total_films += 1
    if total_films:
        director_score = director_score / total_films
    return director_score


def calculate_directors_scores(director_dict):
    directors_scores = {}
    for director in director_dict.keys():
        if len(director_dict[director]) >= min_films:
            score = calculate_directors_score(director, director_dict)
            directors_scores[director] = score
    directors_scores_sorted = sorted(directors_scores, key=directors_scores.get, reverse=True)
    return directors_scores_sorted


def main():
    csv_list = download_director_csv()
    csv_list = filter_director_data(csv_list)
    directors = create_director_dict(csv_list)
    directors_scores_sorted = calculate_directors_scores(directors)
    for order in directors_scores_sorted[:20]:
        print_directors_films(order, directors)


if __name__ == '__main__':
    main()


