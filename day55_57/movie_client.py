import uplink, requests
from uplink_helpers import raise_for_status


@uplink.json
@raise_for_status
class MovieClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search(self, keyword) -> requests.models.Response:
        """ Search TP Movie DB. """

    @uplink.get('/api/director/{director_name}')
    def by_director(self, director_name) -> requests.models.Response:
        """ Returns entries for a given director """

    @uplink.get('/api/movie/{imdb_number}')
    def by_imdb_number(self, imdb_number) -> requests.models.Response:
        """ Returns info about a film from its IMDB number. """
