from getData import GetData
from organiseData import OrganiseData


country = 'england'
league = 'premier-league'
season = '2021-2022'
leagueLink = 'https://www.livesport.com/en/soccer/'+ country + '/' + league + '-' + season + '/results/'

premierLeague = GetData(leagueLink, country, league, season)
premierLeague.getArrayMatches()
jsonData = OrganiseData(premierLeague)
jsonData.jsonFormat()
jsonData.saveAsJSON()




    