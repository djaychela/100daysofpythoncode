import day_44_api


def main():
    search_term = input('Enter Keyword to search for: ')
    results = day_44_api.search_talkpython(search_term)
    print(f"There are {len(results['results'])} matching entries:")
    print('*** Episodes ***')
    for idx, res in enumerate(results['results'],1):
        if res['category'] == 'Episode':
            print(f"{idx}: [{res['id']}] - {res['title']}")
    print('*** Transcripts ***')
    for idx, res in enumerate(results['results'],1):
        if res['category'] == 'Transcript':
            print(f"{idx}: [{res['id']}] - {res['title']}")


if __name__ == '__main__':
    main()