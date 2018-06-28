import requests
import csv
from objectpath import Tree


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
    team_info = search_result('Allsvenskan')
    with open('output.csv', 'w+') as f:
        w = csv.DictWriter(f, ['name', 'id', 'slug', 'url'])
        w.writeheader()
        for item in team_info:
            w.writerow(item)
