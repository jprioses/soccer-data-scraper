import navigate

class GetData:
    
    def __init__(self, url, country, league, season):
        
        self.country = country
        self.league = league
        self.season = season
        self.data = []
        self.arrayMatches = []
        self.url = url

    def getArrayMatches(self):
        navigate.openUrl(self.url)
        navigate.acceptCookies()
        self.arrayMatches = navigate.showMoreMatches()
        self.eachMatchData(self.arrayMatches)
             
    def eachMatchData(self, arrayMatches):
        i = 0
        for match in arrayMatches:
            navigate.eachMatch(match)
            self.data.append(GetEachMatchData())
            self.data[i].get_dateTimeRound()
            self.data[i].get_homeData()
            self.data[i].get_awayData()
            self.data[i].get_firstHalfHomeStats()
            self.data[i].get_firstHalfAwayStats()
            self.data[i].get_secondHalfHomeStats()
            self.data[i].get_secondHalfAwayStats()
            
            i+= 1

            navigate.closeWindow()

        navigate.closeBrowser()
           
class GetEachMatchData:

    def __init__(self):
            self.date = ''
            self.time= ''
            self.round=''
            self.home=''
            self.away=''
            self.homeScore=''
            self.awayScore=''
            self.homeLineups= []
            self.awayLineups= []
            self.homeGoals= []
            self.homeScorer= []
            self.awayGoals= []
            self.awayScorer= []
            self.firstHalfHomeStats = {}
            self.secondHalfHomeStats = {}
            self.firstHalfAwayStats = {}
            self.secondHalfAwayStats = {}

    def get_dateTimeRound(self):
        dateTimeInfo, roundInfo = navigate.eachMatchInfo()
        
        arrayDateTime = dateTimeInfo.split(' ')
        self.date = arrayDateTime[0]
        self.time = arrayDateTime[1]

        arrayRound = roundInfo.split(' - ROUND ')
        self.round = arrayRound[1]

    def get_homeData(self):
        self.home, self.homeScore, self.homeGoals, self.homeScorer= navigate.eachMatchGoals('home')
        
    def get_awayData(self):
        self.away, self.awayScore, self.awayGoals, self.awayScorer= navigate.eachMatchGoals('away')

    def get_firstHalfHomeStats(self):
        self.firstHalfHomeStats = navigate.eachMatchStats('home', '1ST HALF', False, False)
        
    def get_secondHalfHomeStats(self):
        self.secondHalfHomeStats = navigate.eachMatchStats('home', '2ND HALF', True, False)

    def get_firstHalfAwayStats(self):
        self.firstHalfAwayStats = navigate.eachMatchStats('away', '1ST HALF', True, True)

    def get_secondHalfAwayStats(self):
        self.secondHalfAwayStats = navigate.eachMatchStats('away', '2ND HALF', True, True)






    