from stats import Stats
from tournaments import Allsvenskan, BRSerieA, Allsvenskan, MLS, BRSerieA, BRSerieB, PremierLeagueEngland


if __name__ == "__main__":
    allsvenskan = Allsvenskan()
    events = allsvenskan.get_matches_events()
    stats = Stats(events)
    stats.tournament_goals_stats().to_csv('./goals_stats.csv')
