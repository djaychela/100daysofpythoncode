import pandas as pd

csv_url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
min_films = 4
year_cutoff = 1960

def get_and_clean_data(url):
    df = pd.read_csv(csv_url)
    all_columns = list(df.columns)
    delete_columns = [x for x in all_columns if x not in ['director_name', 'imdb_score', 'movie_title', 'title_year']]
    for column in delete_columns:
        del df[column]
    return df


def print_director_summary(director, score, df):
    print('{:<25} {:>20.1f}' .format(director, score))
    print('{:*^46}'.format(''))
    for i in range(len(df)):
        print('{:<4.0f} {:<30} {:>10}'.format(df.iloc[i]['title_year'], df.iloc[i]['movie_title'][:30], df.iloc[i]['imdb_score']))
    print()


def main():
    directors = get_and_clean_data(csv_url)
    directors = directors.loc[directors['title_year'] >= year_cutoff]
    director_list = directors.director_name.unique()
    director_scores = {}
    for director in director_list:
        director_df = directors.loc[directors['director_name'] == director]
        if len(director_df) >= min_films:
            director_scores[director] = director_df['imdb_score'].mean()
    director_scores_sorted = sorted(director_scores, key=director_scores.get, reverse=True)
    for director in director_scores_sorted[:20]:
        director_df = directors.loc[directors['director_name'] == director]
        print_director_summary(director, director_scores[director], director_df)


if __name__ == "__main__":
    main()

