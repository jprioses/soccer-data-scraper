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
                'matches': []
            })

        i=0
        for data in self.leagueData.data:
            self.data[0]['matches'].append({
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

    def saveAsTXT(self):
        with open('data.txt', 'w') as txt_file:
            txt_file.writelines(json.dumps(self.data, indent=1))

    def saveAsCSV(self):
        fields = ['league', 'season', 'round','date','time','home','away','homeScore','awayScore','homeGoals','homeScorers','awayGoals','awayScorers', '1HalfStats '+'home '+'Ball Possession',
        '1HalfStats '+'away '+'Ball Possession',
        '1HalfStats '+'home '+'Goal Attempts',
        '1HalfStats '+'away '+'Goal Attempts',
        '1HalfStats '+'home '+'Shots on Goal',
        '1HalfStats '+'away '+'Shots on Goal',
        '1HalfStats '+'home '+'Shots off Goal',
        '1HalfStats '+'away '+'Shots off Goal',
        '1HalfStats '+'home '+'Blocked Shots',
        '1HalfStats '+'away '+'Blocked Shots',
        '1HalfStats '+'home '+'Free Kicks',
        '1HalfStats '+'away '+'Free Kicks',
        '1HalfStats '+'home '+'Corner Kicks',
        '1HalfStats '+'away '+'Corner Kicks',
        '1HalfStats '+'home '+'Throw-in',
        '1HalfStats '+'away '+'Throw-in',
        '1HalfStats '+'home '+'Goalkeeper Saves',
        '1HalfStats '+'away '+'Goalkeeper Saves',
        '1HalfStats '+'home '+'Fouls',
        '1HalfStats '+'away '+'Fouls',
        '1HalfStats '+'home '+'Yellow Cards',
        '1HalfStats '+'away '+'Yellow Cards',
        '1HalfStats '+'home '+'Red Cards',
        '1HalfStats '+'away '+'Red Cards',
        '1HalfStats '+'home '+'Total Passes',
        '1HalfStats '+'away '+'Total Passes',
        '1HalfStats '+'home '+'Completed Passes',
        '1HalfStats '+'away '+'Completed Passes',
        '1HalfStats '+'home '+'Tackles',
        '1HalfStats '+'away '+'Tackles',
        '1HalfStats '+'home '+'Attacks',
        '1HalfStats '+'away '+'Attacks',
        
        '1HalfStats '+'home '+'Dangerous Attacks',
        '1HalfStats '+'away '+'Dangerous Attacks',
        '2HalfStats '+'home '+'Ball Possession',
        '2HalfStats '+'away '+'Ball Possession',
        '2HalfStats '+'home '+'Goal Attempts',
        '2HalfStats '+'away '+'Goal Attempts',
        '2HalfStats '+'home '+'Shots on Goal',
        '2HalfStats '+'away '+'Shots on Goal',
        '2HalfStats '+'home '+'Shots off Goal',
        '2HalfStats '+'away '+'Shots off Goal',
        '2HalfStats '+'home '+'Blocked Shots',
        '2HalfStats '+'away '+'Blocked Shots',
        '2HalfStats '+'home '+'Free Kicks',
        '2HalfStats '+'away '+'Free Kicks',
        '2HalfStats '+'home '+'Corner Kicks',
        '2HalfStats '+'away '+'Corner Kicks',
        '2HalfStats '+'home '+'Throw-in',
        '2HalfStats '+'away '+'Throw-in',
        '2HalfStats '+'home '+'Goalkeeper Saves',
        '2HalfStats '+'away '+'Goalkeeper Saves',
        '2HalfStats '+'home '+'Fouls',
        '2HalfStats '+'away '+'Fouls',
        '2HalfStats '+'home '+'Yellow Cards',
        '2HalfStats '+'away '+'Yellow Cards',
        '2HalfStats '+'home '+'Red Cards',
        '2HalfStats '+'away '+'Red Cards',
        '2HalfStats '+'home '+'Total Passes',
        '2HalfStats '+'away '+'Total Passes',
        '2HalfStats '+'home '+'Completed Passes',
        '2HalfStats '+'away '+'Completed Passes',
        '2HalfStats '+'home '+'Tackles',
        '2HalfStats '+'away '+'Tackles',
        '2HalfStats '+'home '+'Attacks',
        '2HalfStats '+'away '+'Attacks',
        '2HalfStats '+'home '+'Dangerous Attacks',
        '2HalfStats '+'away '+'Dangerous Attacks',

        ]
        rows = []
        i=0
        for match in self.data[0]['matches'] :
            rows[i].append(self.data[0]['country'], 
            self.data[0]['league'], 
            self.data[0]['season'],
            match['round'],
            match['date'],
            match['time'], 
            match['home'], 
            match['away'],
            match['homeScore'], 
            match['awayScore'], 
            match['homeGoals'],
            match['homeScorers'],
            match['awayGoals'], 
            match['awayScorers'], 

            match['stats']['firstHalfStats']['home']['Ball Possession'],
            match['stats']['firstHalfStats']['away']['Ball Possession'],
            match['stats']['firstHalfStats']['home']['Goal Attempts'],
            match['stats']['firstHalfStats']['away']['Goal Attempts'],
            match['stats']['firstHalfStats']['home']['Shots on Goal'],
            match['stats']['firstHalfStats']['away']['Shots on Goal'],
            match['stats']['firstHalfStats']['home']['Shots off Goal'],
            match['stats']['firstHalfStats']['away']['Shots off Goal'],
            match['stats']['firstHalfStats']['home']['Blocked Shots'],
            match['stats']['firstHalfStats']['away']['Blocked Shots'],
            match['stats']['firstHalfStats']['home']['Free Kicks'],
            match['stats']['firstHalfStats']['away']['Free Kicks'],
            match['stats']['firstHalfStats']['home']['Corner Kicks'],
            match['stats']['firstHalfStats']['away']['Corner Kicks'],
            match['stats']['firstHalfStats']['home']['Throw-in'],
            match['stats']['firstHalfStats']['away']['Throw-in'],
            match['stats']['firstHalfStats']['home']['Goalkeeper Saves'],
            match['stats']['firstHalfStats']['away']['Goalkeeper Saves'],
            match['stats']['firstHalfStats']['home']['Fouls'],
            match['stats']['firstHalfStats']['away']['Fouls'],
            match['stats']['firstHalfStats']['home']['Yellow Cards'],
            match['stats']['firstHalfStats']['away']['Yellow Cards'],
            match['stats']['firstHalfStats']['home']['Red Cards'],
            match['stats']['firstHalfStats']['away']['Red Cards'],
            match['stats']['firstHalfStats']['home']['Total Passes'],
            match['stats']['firstHalfStats']['away']['Total Passes'],
            match['stats']['firstHalfStats']['home']['Completed Passes'],
            match['stats']['firstHalfStats']['away']['Completed Passes'],
            match['stats']['firstHalfStats']['home']['Tackles'],
            match['stats']['firstHalfStats']['away']['Tackles'],
            match['stats']['firstHalfStats']['home']['Attacks'],
            match['stats']['firstHalfStats']['away']['Attacks'],
            match['stats']['firstHalfStats']['home']['Dangerous Attacks'],
            match['stats']['firstHalfStats']['away']['Dangerous Attacks'],

            match['stats']['secondHalfStats']['home']['Ball Possession'],
            match['stats']['secondHalfStats']['away']['Ball Possession'],
            match['stats']['secondHalfStats']['home']['Goal Attempts'],
            match['stats']['secondHalfStats']['away']['Goal Attempts'],
            match['stats']['secondHalfStats']['home']['Shots on Goal'],
            match['stats']['secondHalfStats']['away']['Shots on Goal'],
            match['stats']['secondHalfStats']['home']['Shots off Goal'],
            match['stats']['secondHalfStats']['away']['Shots off Goal'],
            match['stats']['secondHalfStats']['home']['Blocked Shots'],
            match['stats']['secondHalfStats']['away']['Blocked Shots'],
            match['stats']['secondHalfStats']['home']['Free Kicks'],
            match['stats']['secondHalfStats']['away']['Free Kicks'],
            match['stats']['secondHalfStats']['home']['Corner Kicks'],
            match['stats']['secondHalfStats']['away']['Corner Kicks'],
            match['stats']['secondHalfStats']['home']['Throw-in'],
            match['stats']['secondHalfStats']['away']['Throw-in'],
            match['stats']['secondHalfStats']['home']['Goalkeeper Saves'],
            match['stats']['secondHalfStats']['away']['Goalkeeper Saves'],
            match['stats']['secondHalfStats']['home']['Fouls'],
            match['stats']['secondHalfStats']['away']['Fouls'],
            match['stats']['secondHalfStats']['home']['Yellow Cards'],
            match['stats']['secondHalfStats']['away']['Yellow Cards'],
            match['stats']['secondHalfStats']['home']['Red Cards'],
            match['stats']['secondHalfStats']['away']['Red Cards'],
            match['stats']['secondHalfStats']['home']['Total Passes'],
            match['stats']['secondHalfStats']['away']['Total Passes'],
            match['stats']['secondHalfStats']['home']['Completed Passes'],
            match['stats']['secondHalfStats']['away']['Completed Passes'],
            match['stats']['secondHalfStats']['home']['Tackles'],
            match['stats']['secondHalfStats']['away']['Tackles'],
            match['stats']['secondHalfStats']['home']['Attacks'],
            match['stats']['secondHalfStats']['away']['Attacks'],
            match['stats']['secondHalfStats']['home']['Dangerous Attacks'],
            match['stats']['secondHalfStats']['away']['Dangerous Attacks'])

            i+=1


        with open('data.csv', 'w') as csv_file:  
            # creating a csv writer object  
            csvwriter = csv.writer(csv_file)  
                
            # writing the fields  
            csvwriter.writerow(fields)  
                
            # writing the data rows  
            csvwriter.writerows(rows)




        

