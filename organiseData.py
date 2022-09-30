import json
import csv

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
            json.dump(self.data, json_file, indent=1)

    def saveAsTXt(self):
        with open('data.txt', 'w') as txt_file:
            txt_file.writelines(json.dumps(self.data, indent=1))

    def saveAsCSV(self):
        with open('data.csv', 'w') as csv_file:  
            # creating a csv writer object  
            csvwriter = csv.writer(csv_file)  
                
            # writing the fields  
            csvwriter.writerow(fields)  
                
            # writing the data rows  
            csvwriter.writerows(rows)




        

