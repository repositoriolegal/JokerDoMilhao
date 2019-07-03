import logging
import sys

from repositories import ElasticSearch
from tournaments import Allsvenskan, BRSerieA, Allsvenskan, MLS, BRSerieA, BRSerieB, PremierLeagueEngland

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)


if __name__ == "__main__":
    allsvenskan = Allsvenskan()

    events = allsvenskan.get_matches_events()

    logging.info('Start to send to Elasticsearch')

    es = ElasticSearch()
    for event in events:
        es.insert(event)

    logging.info('Finish to send information to Elasticsearch')
