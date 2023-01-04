import json
import csv
import os

class OrganiseData:
    def __init__(self, leagueData):
        self.leagueData = leagueData
        self.data = []
        self.dirName = self.getDirName()
        self.fileName =  self.dirName + '/' + self.leagueData.league + self.leagueData.season

        
    def getDirName(self):
        dirName = './data/' + self.leagueData.league 
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass

        return dirName

    def jsonFormat(self):

        self.data.append({
                'country': self.leagueData.country,
                'league': self.leagueData.league,
                'season': self.leagueData.season,
                'matches': []
            })

        i=len(self.leagueData.arrayMatches)
        for data in self.leagueData.data:
            self.data[0]['matches'].append({
                'id':str(i),
                'count':str(i) + ' out of ' + str(len(self.leagueData.arrayMatches)),
                'date': data.date,
                'time': data.time,
                'round': data.round,
                'home': data.home,
                'away': data.away,
                'homeScore': data.homeScore,
                'awayScore': data.awayScore,
                'homeGoals': data.homeGoals,
                'homeScorers': data.homeScorer,
                'homeAsist': data.homeAsist,
                'awayGoals': data.awayGoals,
                'awayScorers': data.awayScorer,
                'awayAsist': data.awayAsist,
                'stats': {
                    'firstHalfStats': {
                        'home': data.firstHalfHomeStats,
                        'away': data.firstHalfAwayStats,
                    },
                    'secondHalfStats': {
                        'home': data.secondHalfHomeStats,
                        'away': data.secondHalfAwayStats,
                    }
                },
                'odds': {
                    'moneyLine': {
                        'home': data.homeOdds,
                        'draw': data.evenOdds,
                        'away': data.awayOdds
                    },
                    'overUnder': {
                        'over0.5': data.over0,
                        'under0.5': data.under0,
                        'over1.5': data.over1,
                        'under1.5': data.under1,
                        'over2.5': data.over2,
                        'under2.5': data.under2,
                        'over3.5': data.over3,
                        'under3.5': data.under3,
                    }
                }
            })
            i-=1
    
    def saveAsJSON(self):
        with open(self.fileName + '.json', 'w') as json_file:
            json.dump(self.data, json_file, indent=1)

    def saveAsTXT(self):
        with open(self.fileName + '.txt', 'w') as txt_file:
            txt_file.writelines(json.dumps(self.data, indent=1))

    def saveAsCSV(self):
        fields = [
        'id',
        'country',
        'league', 
        'season', 
        'round',
        'date',
        'time', 
        'count',
        'home',
        'away',
        'homeScore',
        'awayScore',
        'homeGoals',
        'homeScorers', 
        'homeAsists',
        'awayGoals',
        'awayScorers', 
        'awayAsists',

        '1HalfStats '+'home '+'Ball Possession',
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
        '1HalfStats '+'home '+'Offsides',
        '1HalfStats '+'away '+'Offsides',
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
        '2HalfStats '+'home '+'Offsides',
        '2HalfStats '+'away '+'Offsides',
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

        'moneyLineOdds '+'home',
        'moneyLineOdds '+'draw',
        'moneyLineOdds '+'away',

        'overUnderOdds '+'over0.5',
        'overUnderOdds '+'under0.5',
        'overUnderOdds '+'over1.5',
        'overUnderOdds '+'under1.5',
        'overUnderOdds '+'over2.5',
        'overUnderOdds '+'under2.5',
        'overUnderOdds '+'over3.5',
        'overUnderOdds '+'under3.5'
        
        ]

        rows = []
        i=0
        for match in self.data[0]['matches'] :
            rows.append([])
            rows[i].extend((
            match['id'], 
            self.data[0]['country'], 
            self.data[0]['league'], 
            self.data[0]['season'],
            match['round'],
            match['date'],
            match['time'], 
            match['count'], 
            match['home'], 
            match['away'],
            match['homeScore'], 
            match['awayScore'], 
            match['homeGoals'],
            match['homeScorers'],
            match['homeAsist'],
            match['awayGoals'], 
            match['awayScorers'], 
            match['awayAsist'],

            match['stats']['firstHalfStats']['home'].get('Ball Possession', 0),
            match['stats']['firstHalfStats']['away'].get('Ball Possession', 0),
            match['stats']['firstHalfStats']['home'].get('Goal Attempts', 0),
            match['stats']['firstHalfStats']['away'].get('Goal Attempts', 0),
            match['stats']['firstHalfStats']['home'].get('Shots on Goal', 0),
            match['stats']['firstHalfStats']['away'].get('Shots on Goal', 0),
            match['stats']['firstHalfStats']['home'].get('Shots off Goal', 0),
            match['stats']['firstHalfStats']['away'].get('Shots off Goal', 0),
            match['stats']['firstHalfStats']['home'].get('Blocked Shots', 0),
            match['stats']['firstHalfStats']['away'].get('Blocked Shots', 0),
            match['stats']['firstHalfStats']['home'].get('Free Kicks', 0),
            match['stats']['firstHalfStats']['away'].get('Free Kicks', 0),
            match['stats']['firstHalfStats']['home'].get('Corner Kicks', 0),
            match['stats']['firstHalfStats']['away'].get('Corner Kicks', 0),
            match['stats']['firstHalfStats']['home'].get('Offsides', 0),
            match['stats']['firstHalfStats']['away'].get('Offsides', 0),
            match['stats']['firstHalfStats']['home'].get('Throw-in', 0),
            match['stats']['firstHalfStats']['away'].get('Throw-in', 0),
            match['stats']['firstHalfStats']['home'].get('Goalkeeper Saves', 0),
            match['stats']['firstHalfStats']['away'].get('Goalkeeper Saves', 0),
            match['stats']['firstHalfStats']['home'].get('Fouls', 0),
            match['stats']['firstHalfStats']['away'].get('Fouls', 0),
            match['stats']['firstHalfStats']['home'].get('Yellow Cards', 0),
            match['stats']['firstHalfStats']['away'].get('Yellow Cards', 0),
            match['stats']['firstHalfStats']['home'].get('Red Cards', 0),
            match['stats']['firstHalfStats']['away'].get('Red Cards', 0),
            match['stats']['firstHalfStats']['home'].get('Total Passes', 0),
            match['stats']['firstHalfStats']['away'].get('Total Passes', 0),
            match['stats']['firstHalfStats']['home'].get('Completed Passes', 0),
            match['stats']['firstHalfStats']['away'].get('Completed Passes', 0),
            match['stats']['firstHalfStats']['home'].get('Tackles', 0),
            match['stats']['firstHalfStats']['away'].get('Tackles', 0),
            match['stats']['firstHalfStats']['home'].get('Attacks', 0),
            match['stats']['firstHalfStats']['away'].get('Attacks', 0),
            match['stats']['firstHalfStats']['home'].get('Dangerous Attacks', 0),
            match['stats']['firstHalfStats']['away'].get('Dangerous Attacks', 0),

            match['stats']['secondHalfStats']['home'].get('Ball Possession', 0),
            match['stats']['secondHalfStats']['away'].get('Ball Possession', 0),
            match['stats']['secondHalfStats']['home'].get('Goal Attempts', 0),
            match['stats']['secondHalfStats']['away'].get('Goal Attempts', 0),
            match['stats']['secondHalfStats']['home'].get('Shots on Goal', 0),
            match['stats']['secondHalfStats']['away'].get('Shots on Goal', 0),
            match['stats']['secondHalfStats']['home'].get('Shots off Goal', 0),
            match['stats']['secondHalfStats']['away'].get('Shots off Goal', 0),
            match['stats']['secondHalfStats']['home'].get('Blocked Shots', 0),
            match['stats']['secondHalfStats']['away'].get('Blocked Shots', 0),
            match['stats']['secondHalfStats']['home'].get('Free Kicks', 0),
            match['stats']['secondHalfStats']['away'].get('Free Kicks', 0),
            match['stats']['secondHalfStats']['home'].get('Corner Kicks', 0),
            match['stats']['secondHalfStats']['away'].get('Corner Kicks', 0),
            match['stats']['secondHalfStats']['home'].get('Offsides', 0),
            match['stats']['secondHalfStats']['away'].get('Offsides', 0),
            match['stats']['secondHalfStats']['home'].get('Throw-in', 0),
            match['stats']['secondHalfStats']['away'].get('Throw-in', 0),
            match['stats']['secondHalfStats']['home'].get('Goalkeeper Saves', 0),
            match['stats']['secondHalfStats']['away'].get('Goalkeeper Saves', 0),
            match['stats']['secondHalfStats']['home'].get('Fouls', 0),
            match['stats']['secondHalfStats']['away'].get('Fouls', 0),
            match['stats']['secondHalfStats']['home'].get('Yellow Cards', 0),
            match['stats']['secondHalfStats']['away'].get('Yellow Cards', 0),
            match['stats']['secondHalfStats']['home'].get('Red Cards', 0),
            match['stats']['secondHalfStats']['away'].get('Red Cards', 0),
            match['stats']['secondHalfStats']['home'].get('Total Passes', 0),
            match['stats']['secondHalfStats']['away'].get('Total Passes', 0),
            match['stats']['secondHalfStats']['home'].get('Completed Passes', 0),
            match['stats']['secondHalfStats']['away'].get('Completed Passes', 0),
            match['stats']['secondHalfStats']['home'].get('Tackles', 0),
            match['stats']['secondHalfStats']['away'].get('Tackles', 0),
            match['stats']['secondHalfStats']['home'].get('Attacks', 0),
            match['stats']['secondHalfStats']['away'].get('Attacks', 0),
            match['stats']['secondHalfStats']['home'].get('Dangerous Attacks', 0),
            match['stats']['secondHalfStats']['away'].get('Dangerous Attacks', 0),

            match['odds']['moneyLine']['home'],
            match['odds']['moneyLine']['draw'],
            match['odds']['moneyLine']['away'],

            match['odds']['overUnder']['over0.5'],
            match['odds']['overUnder']['under0.5'],
            match['odds']['overUnder']['over1.5'],
            match['odds']['overUnder']['under1.5'],
            match['odds']['overUnder']['over2.5'],
            match['odds']['overUnder']['under2.5'],
            match['odds']['overUnder']['over3.5'],
            match['odds']['overUnder']['under3.5'])
            )

            i+=1


        with open(self.fileName + '.csv', 'w') as csv_file:  
            # creating a csv writer object  
            csvwriter = csv.writer(csv_file)  
                
            # writing the fields  
            csvwriter.writerow(fields)  
                
            # writing the data rows  
            csvwriter.writerows(rows)




        

