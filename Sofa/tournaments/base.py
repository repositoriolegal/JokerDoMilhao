import logging
import requests
import sys

from constants import URL_TOURNAMENT, URL_ROUND_MATCHES, URL_MATCH_DATA


logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)


class BaseTournament():
    URL_TOURNAMENT = URL_TOURNAMENT
    URL_ROUND_MATCHES = URL_ROUND_MATCHES
    URL_MATCH_DATA = URL_MATCH_DATA
    TOURNAMENT_ID = None
    TOURNAMENT_SEASON_ID = None

    def get_matches_events(self):
        response = requests.get(self.URL_TOURNAMENT.format(id_tournament=self.TOURNAMENT_ID, id_season=self.TOURNAMENT_SEASON_ID))
        data = response.json()

        matches_ids = self.get_all_matches_ids_by_rounds(data=data)

        events = self.get_all_matches_data(matches_ids)

        print(len(events))


    def get_all_matches_ids_by_rounds(self, data) -> list:
        rounds = data['events']['rounds']

        matches_ids = []
        for round_item in rounds:
            round_name = round_item.get('name')
            label = round_name or round_item['round']

            logging.info("Getting all matches ids from round %s...", label)

            if round_name != 'Final':
                ids = self.get_matches_ids_by_round(round_number = round_item['round'])
                matches_ids = matches_ids + ids

            else:
                # If it is a Final Match, the Match ID information it is in the data variable.
                ids = self.get_matches_ids(data['events'])
                matches_ids = matches_ids + ids


            logging.info("Got all matches ids from round %s", label)

        return matches_ids


    def get_matches_ids_by_round(self, round_number) -> list:
        response = requests.get(self.URL_ROUND_MATCHES.format(id_tournament=self.TOURNAMENT_ID,
                                                        id_season=self.TOURNAMENT_SEASON_ID,
                                                        round_number=round_number))

        data = response.json()

        matchs_ids = self.get_matches_ids(data)

        return matchs_ids

    
    def get_matches_ids(self, data) -> list:
        matchs_ids = []
        for match in data['roundMatches']['tournaments'][0]['events']:
            matchs_ids.append(match['id'])

        return matchs_ids


    def get_all_matches_data(self, matches_ids) -> list:
        events = []
        for id_match in matches_ids:
            events.append(self.get_match_data(id_match))

        return events


    def get_match_data(self, match_id) -> dict:
        logging.info("Getting match data from match number %s...", match_id)

        response = requests.get(self.URL_MATCH_DATA.format(match_id=match_id))

        match_data = response.json()

        logging.info("Got match data")
        return match_data
