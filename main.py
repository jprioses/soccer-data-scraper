from getData import GetData
from organiseData import OrganiseData

country = 'france'
league = 'ligue-2'
season = '2020-2021'
premierLeague = GetData(country, league, season)
premierLeague.getArrayMatches()
jsonData = OrganiseData(premierLeague)
jsonData.jsonFormat()
jsonData.saveAsJSON()
jsonData.saveAsTXT()
jsonData.saveAsCSV()




    