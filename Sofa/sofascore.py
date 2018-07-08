import requests
import csv
from objectpath import Tree

URL_MATCH = 'https://www.sofascore.com/pt/{slug_match}/{match_custom_id}'
URL_MATCHES = "https://www.sofascore.com/tournament/24/{id_tournament}/standings/tables/json"

ALLSVENSKAN_ID = 15731

def get_id_matches():
    response = requests.get(URL_MATCHES.format(id_tournament=ALLSVENSKAN_ID))

    # Retornar lista de URLs de cada partida
    # URL.format(slug_match=,match_id)
    # slug_match e match_id estão contidos no json da response acima
    # Como acessar o Response de retorno: response.json()['teamEvents']['1768']['away'][0]
    # Opções de cada dicionário:
    # Dic_1: 'standingsTables', 'teamEvents'
    # Dic_2: '1768', '1762', '1759', '1769', '1761', '1891', '1771',
    # '1764', '1760', '1763', '22260', '1787', '1793', '1892', '1758', '1836'
    # Dic_3: 'total', 'home', 'away'
    return 'hello'

def search_result(query):
    SEARCH_URL = 'https://www.sofascore.com/search/results?q={}'.format
    T_QUERY = '$.*[@.name is "{}" and @.category.sport.name is "Football"].id'.format  # noqa

    response = requests.get(SEARCH_URL(query))
    if response.status_code == 200:
        response_tree = Tree(response.json()['tournaments'])
        tournament_id = tuple(response_tree.execute(T_QUERY(query)))[0]
        return get_team_ids(tournament_id)


def get_team_ids(tournament_id):
    SEARCH_URL = 'https://www.sofascore.com/u-tournament/{}/season/15731/json'
    T_QUERY = '$.standingsTables.tableRows'
    TEAM_URL_BASE = 'https://www.sofascore.com/pt/time/futebol/{slug}/{t_id}'
    teams = []

    response = requests.get(SEARCH_URL.format(tournament_id))
    if response.status_code == 200:
        response_tree = Tree(response.json())
        table_row = tuple(response_tree.execute(T_QUERY))[0]
        for row in table_row:
            info = row['team']
            team_url = TEAM_URL_BASE.format(slug=info['slug'], t_id=info['id'])
            team_obj = {
                'slug': info['slug'],
                'name': info['shortName'],
                'id': info['id'],
                'url': team_url
            }
            teams.append(team_obj)
    return teams


if __name__ == "__main__":
    get_id_matches()
 
    """team_info = search_result('Allsvenskan')
    with open('output.csv', 'w+') as f:
        w = csv.DictWriter(f, ['name', 'id', 'slug', 'url'])
        w.writeheader()
        for item in team_info:
            w.writerow(item)"""
