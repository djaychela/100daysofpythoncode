import feedparser, requests

feed_file = 'bbc_comedy.rss'

feed = feedparser.parse(feed_file)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f"Downloading {entry.title}: {entry.link}")
        audio = requests.get(entry.enclosures[0]['href'])
        print('Saving file...')
        with open(entry.title + '.mp3', 'wb') as file:
            file.write(audio.content)

