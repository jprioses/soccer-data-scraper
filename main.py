from getData import GetData
from organiseData import OrganiseData

country = 'england'
league = 'premier-league'
season = '2021-2022'
premierLeague = GetData(country, league, season)
premierLeague.getArrayMatches()
jsonData = OrganiseData(premierLeague)
jsonData.jsonFormat()
jsonData.saveAsTXT()




    