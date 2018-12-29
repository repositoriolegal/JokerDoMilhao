import pandas as pd


TIME_SLOTS = ['1T', '2T', 'FT', '1QT', '2QT', '3QT', '4QT', '5QT', '6QT']


def _in_range(series, low, high, ilow=True, ihigh=False):
    return ((series >= low if ilow else series > low) &
            (series <= high if ihigh else series < high))


class Stats():
    def __init__(self, events):
        self.events = events

    def tournament_goals_stats(self):
        goals_events = pd.DataFrame(goals_filter(self.events))

        goals_events['1T'] = goals_events['time'] <= 45
        goals_events['2T'] = ~goals_events['1T']
        goals_events['FT'] = True

        goals_events['1QT'] = _in_range(goals_events['time'], 0, 15)
        goals_events['2QT'] = _in_range(goals_events['time'], 15, 30)
        goals_events['3QT'] = _in_range(goals_events['time'], 30, 45)
        goals_events['4QT'] = _in_range(goals_events['time'], 45, 60)
        goals_events['5QT'] = _in_range(goals_events['time'], 60, 75)
        goals_events['6QT'] = goals_events['time'] >= 75

        goals_by_game = goals_events.groupby('eventid')[TIME_SLOTS].sum()

        cuts = [1.5, 2.5, 3.5, 4.5]
        data = []
        for cutoff in cuts:
            series = 100 * (goals_by_game > cutoff).sum()/len(events)
            data.append(series.to_dict())

        df = pd.DataFrame(data=data,
                          index=['OVER {}'.format(c) for c in cuts])

        return df
