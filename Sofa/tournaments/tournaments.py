from constants import ALLSVENSKAN_ID, ALLSVENSKAN_SEASON2018_ID, MLS_ID, MLS_SEASON2018_ID
from tournaments.base import BaseTournament

class Allsvenskan(BaseTournament):
    TOURNAMENT_ID = ALLSVENSKAN_ID
    TOURNAMENT_SEASON_ID = ALLSVENSKAN_SEASON2018_ID
    BY_ROUND = True


class MLS(BaseTournament):
    TOURNAMENT_ID = MLS_ID
    TOURNAMENT_SEASON_ID = MLS_SEASON2018_ID
    BY_MATCH = True
