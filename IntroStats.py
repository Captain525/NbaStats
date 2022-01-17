"""
Static statistics access. Can access player information without having to submit requests
to the API.
Player info: id, full name, first name, last name, is active. ALL STATIC DOES IS
GET THE LISTS, NOT THE DATA.


"""
import nba_api.stats.library.parameters
from nba_api.stats.static import players
playerList = players.get_players()
numPlayers = len(playerList)
print(playerList[:100])


"""
Teams: id, full name, abbreviation, nickname, city, state, year founded. 
"""
from nba_api.stats.static import teams
team_dict = teams.get_teams()
numTeams = len(team_dict)
print(team_dict)

"""
Now, we have the static info for teams and players, but no actual data or api endpoint connections. 

"""

"""
first endpoint used is commonplayerinfo, which contains 3 data sets:
1. available seasons
2. common player info - qualitative life info, not statistics. 
3. playerheadline stats - player name and id, as well as pts ast reb and pie. 

Parameters to common player info: player id, league id. Don't have to put in league id. 
"""
import requests
from nba_api.stats.endpoints import commonplayerinfo
#get just steph from the list.
steph = [player for player in playerList if player['full_name'] == 'Stephen Curry'][0]

print(steph)
print(steph.get("id"))
#time to submit a basic request.
curryInfo = commonplayerinfo.CommonPlayerInfo(player_id=steph.get("id"));
curryDF = curryInfo.player_headline_stats.get_data_frame()
curryDFINFO = curryInfo.common_player_info.get_data_frame()
print(curryDF);
print(curryDFINFO);

from nba_api.stats.endpoints import alltimeleadersgrids
headers ={
"Referer": "https://www.nba.com/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57"}
#request = requests.get(url="https://stats.nba.com/stats/alltimeleadersgrids?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TopX=10", headers=headers)
top1003PT = alltimeleadersgrids.AllTimeLeadersGrids()
print(top1003PT.fg3_pct_leaders.get_data_frame())