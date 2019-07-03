import os
from urllib.parse import urljoin

# Tournament Constants
url_host = os.environ.get('URL_HOST')
URL_TOURNAMENT = urljoin(url_host,"u-tournament/{id_tournament}/season/{id_season}/json?_=")
URL_ROUND_MATCHES = urljoin(url_host,"u-tournament/{id_tournament}/season/{id_season}/matches/round/{round_number}?_=")
URL_WEEK_MATCHES = urljoin(url_host,"u-tournament/{id_tournament}/season/{id_season}/matches/week/{start_date}/{end_date}")
URL_MATCH_DATA = urljoin(url_host,"event/{match_id}/json?_=")

# Allsvenskan Constants
ALLSVENSKAN_ID = 40
ALLSVENSKAN_SEASON2018_ID = 15731
ALLSVENSKAN_SEASON2019_ID = 19949

# MLS Constants
MLS_ID = 242
MLS_SEASON2018_ID = 15813
MLS_SEASON2019_ID = 20108

# BR Serie A Constants
BRSERIEA_ID = 325
BRSERIEA_SEASON2018_ID = 16183
BRSERIEA_SEASON2019_ID = 22931

# BR Serie B Constants
BRSERIEB_ID = 390
BRSERIEB_SEASON2018_ID = 16184
BRSERIEB_SEASON2019_ID = 22932

# Premier League England Constants
PREMIER_LEAGUE_ENGLAND_ID = 17
PREMIER_LEAGUE_ENGLAND_SEASON2018_ID = 13380
PREMIER_LEAGUE_ENGLAND_SEASON2019_ID = 23776
