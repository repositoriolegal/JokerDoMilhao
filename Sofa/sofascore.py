import requests
import csv
from objectpath import Tree

URL_MATCHES = "https://www.sofascore.com/tournament/24/{id_tournament}/standings/tables/json"
URL_MATCH_DATA = "https://www.sofascore.com/event/{match_id}/json?_="

ALLSVENSKAN_ID = 15731


def get_id_matches():
    response = requests.get(URL_MATCHES.format(id_tournament=ALLSVENSKAN_ID))

    data = response.json()

    teams_ids = data['teamEvents'].keys()
    print(teams_ids)

    for team_id in teams_ids:
        print(team_id)

        keys = ['total', 'home', 'away']

        for match in data['teamEvents'][team_id]['total']:

            match_id = match['id']

            get_match_data(match_id)

        break

    # incidentType": "goal

    # for in keys:

    import ipdb;ipdb.set_trace()

        # data['teamEvents'][team_id]['away'][game]['awayScore']['current']

        # get_match_info()

    # O response retorna um data da seguinte maneira
    # Retornar lista de URLs de cada partida
    # URL.format(slug_match=,match_id)
    # slug_match e match_id estão contidos no json da response acima
    # Como acessar o Response de retorno: response.json()['teamEvents']['1768']['away'][0]
    # Opções de cada dicionário:
    # Dic_1: 'standingsTables', 'teamEvents'
    # Dic_2: '1768', '1762', '1759', '1769', '1761', '1891', '1771',
    # '1764', '1760', '1763', '22260', '1787', '1793', '1892', '1758', '1836'
    # Dic_3: 'total', 'home', 'away'

def get_match_data(match_id):

    response = requests.get(URL_MATCH_DATA.format(match_id=match_id))

    data = response.json()

    if data['event']['season']['year'] == "2018":

        aux = []
        for incident in data['incidents']:
            if incident['incidentType'] == "goal":

                aux.append(incident)

                print("Home: " + str(incident['homeScore']))
                print("Away: " + str(incident['awayScore']))
                print("Time: " + str(incident['time']))

        print(len(aux))


if __name__ == "__main__":
    get_id_matches()
 
    """team_info = search_result('Allsvenskan')
    with open('output.csv', 'w+') as f:
        w = csv.DictWriter(f, ['name', 'id', 'slug', 'url'])
        w.writeheader()
        for item in team_info:
            w.writerow(item)"""
