from itertools import chain


def matches_gen(data):
    yield {
        'team-slug' : data['event']['homeTeam']['slug'],
        'eventid': data['event']['id'],
    }

    yield {
        'team-slug' : data['event']['awayTeam']['slug'],
        'eventid': data['event']['id'],
    }


def goals_gen(data):
    team_dict = {
        1: data['event']['homeTeam'],
        2: data['event']['awayTeam'],
    }

    for incident in data['incidents']:
        if incident['incidentType'] == 'goal':
            team = team_dict[incident['scoringTeam']]
            yield {
                'team-slug': team['slug'],
                'time': incident['time'],
                'eventid': data['event']['id'],
            }

def goals_filter(events):
    return list(chain.from_iterable(map(goals_gen, events)))
