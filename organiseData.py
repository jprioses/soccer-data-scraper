import json

class OrganiseData:
    def __init__(self, leagueData):
        self.leagueData = leagueData
        self.data = []
    
    def jsonFormat(self):

        self.data.append({
                'country': self.leagueData.country,
                'league': self.leagueData.league,
                'season': self.leagueData.season,
            })

        i=1
        for data in self.leagueData.data:
            self.data.append({
                'id':i,
                'date': data.date,
                'time': data.time,
                'round': data.round,
                'home': data.home,
                'away': data.away,
                'homeScore': data.homeScore,
                'awayScore': data.awayScore,
                'homeGoals': data.homeGoals,
                'homeScorers': data.homeScorer,
                'awayGoals': data.awayGoals,
                'awayScorers': data.awayScorer,
                'stats': {
                    'firstHalfStats': {
                        'home': data.firstHalfHomeStats,
                        'away': data.firstHalfAwayStats,
                    },
                    'secondHalfStats': {
                        'home': data.secondHalfHomeStats,
                        'away': data.secondHalfAwayStats,
                    }
                }
            })
            i+=1
    
    def saveAsJSON(self):
        with open('data.json', 'w') as json_file:
            json.dump(self.data, json_file)
        

