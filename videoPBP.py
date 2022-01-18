from nba_api.stats.endpoints import videoevents
import requests

# getting video clip of a play given gameID and eventID.
#headers for the nba stats website.
HEADERDATA = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    # this one might not be right.
    'Referer': 'https://www.nba.com',
    #'Referer': 'https://stats.nba.com/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

def getVideo(game_id, event_id):
    """
    Given a game and event id, gets the video url associated with this play. The videoevents endpoint allows you to
    get the url of the overall thing, but not the VIDEO url, just of the nba stats url where you can play the video.
    headers are
    https://github.com/swar/nba_api/issues/194s
    """
    headers = HEADERDATA
    video_event = videoevents.VideoEvents(game_id, event_id)
    url = 'https://stats.nba.com/stats/videoeventsasset?GameEventID={}&GameID={}'.format(event_id, game_id)
    r = requests.get(url, headers=headers)
    json = r.json()
    video_urls = json['resultSets']['Meta']['videoUrls']
    playlist = json['resultSets']['playlist']
    # get video urls in the form of: {url, description}
    video_event = {'video': video_urls[0]['lurl'], 'desc': playlist[0]['dsc']}
    print(video_event);
def getTeamID(team):
    """
    Whether you input a team abbreviation, full name, just name, or city, this will return the proper id.
    team is a string of an abbreviation, city name, or Team name.
    """
    teamID=None
    teamGuess = None
    if team is None:
        return None
    if len(team) < 3:
        print("not a valid team")
        return None
    from nba_api.stats.static import teams
    teamGuess = teams.find_teams_by_city(team)
    if len(teamGuess) !=0:
        return teamGuess[0]['id']
    teamGuess = teams.find_teams_by_nickname(team)
    if len(teamGuess) != 0:
        return teamGuess[0]['id']
    teamGuess = teams.find_team_by_abbreviation(team)
    if len(teamGuess)!=0:
        return teamGuess[0]['id']
    teamGuess = teams.find_teams_by_full_name(team)
    if len(teamGuess)!=0:
        return teamGuess[0]['id']
    print("couldn't find game")
    return None

def findGames(team1, team2, date, season, WL, startDate, endDate, location):
    """
    returns a list of games that match the input criteria. Can do any input criteria desired.
    Uses leaguegamefinder from nba api. Assume that inputs which are not included in search are inputted as None.
    """
    if team1 != None:
        team1 = getTeamID(team1)
    if team2 !=None:
        team2 = getTeamID(team2)
    if startDate is None and endDate is None and date is not None:
        startDate = date
        endDate = date
    from nba_api.stats.endpoints import leaguegamefinder
    #find the game using this huge list, don't even need to use all this.
    gamefinder  = leaguegamefinder.LeagueGameFinder(league_id_nullable='00', team_id_nullable=team1, vs_team_id_nullable =team2, season_nullable = season, date_from_nullable = startDate, date_to_nullable=endDate, outcome_nullable= WL, location_nullable=location)
    gameList = gamefinder.get_data_frames()[0]
    return gameList
def getGameID(date, team_id):
    """
    get the id of a specific game(which lets us get play by play and events for that game)
    given the season, date, and at least one team in the game.
    date should be in form MM/DD/YYYY
    team_id = number id as string
    season - 2017-18 as a string, something like that.
    """
    from nba_api.stats.endpoints import leaguegamefinder
#league_id_nullable = '00', team_id_nullable = team_id, season_nullable =season, date_to_nullable = date, date_from_nullable = date
    gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable='00', team_id_nullable=team_id, date_from_nullable = date, date_to_nullable=date)
    game = gamefinder.get_data_frames()[0]
    print(game)
    #gets the right index in the dataframe.
    game_id = game.loc[0, "GAME_ID"]
    #GETS THE RIGHT ID.
    return game_id
def accessPBP(game_id):
    """
    Gets to the play by play data from the given game id, currently gets the fourth play of the game, but cacn
    change that later.
    """
    from nba_api.stats.endpoints import playbyplayv2
    pbp = playbyplayv2.PlayByPlayV2(game_id)
    pbp = pbp.get_data_frames()[0]
    print(pbp)
    pbp.head()
    from random import randint
    randomPlay = randint(0, len(pbp)-1)
    print(randomPlay)
    print(pbp.loc[randomPlay])
    return pbp.loc[randomPlay, "EVENTNUM"]

def main():
    gameList = findGames("New York", None, None, '2021-22',None, None, None, None)
    print(gameList)
    from random import randint
    gameChosen = randint(0, len(gameList)-1)
    game = gameList.loc[gameChosen, "GAME_ID"]
    eventID = accessPBP(game)
    print (eventID)
    getVideo(game, eventID)
if __name__ == "__main__":
    main()