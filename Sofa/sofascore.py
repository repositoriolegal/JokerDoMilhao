import logging
import requests
import sys


URL_MATCHES = "https://www.sofascore.com/tournament/24/{id_tournament}/standings/tables/json"
URL_MATCH_DATA = "https://www.sofascore.com/event/{match_id}/json?_="

ALLSVENSKAN_ID = 15731

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)


def get_id_matches():
    response = requests.get(URL_MATCHES.format(id_tournament=ALLSVENSKAN_ID))

    data = response.json()

    teams_ids = data['teamEvents'].keys()

    keys = ['total', 'home', 'away']
    incidents = []
    for team_id in teams_ids:
        logging.info("Getting all matches incidents from %s...", team_id)

        for key in keys:
            for match in data['teamEvents'][team_id][key]:

                match_incidents = get_match_data(match['id'])

                incidents.append(match_incidents)

        logging.info("Got all matches incidents from %s...", team_id)

    import ipdb;ipdb.set_trace()


def get_match_data(match_id):
    logging.info("Getting match incidents data...")

    response = requests.get(URL_MATCH_DATA.format(match_id=match_id))

    data = response.json()

    incidents_data = {  "season": data['event']['season'],
                        "homeTeam": data['event']['homeTeam'],
                        "awayTeam": data['event']['awayTeam'],
                        "incidents": data['incidents']}

    logging.info("Got match incidents data")
    return incidents_data


if __name__ == "__main__":
    get_id_matches()
