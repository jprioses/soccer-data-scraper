import navigate


#Start Chrome web browser 
# chromeBrowser = webdriver.Chrome(service=Service("./chromedriver.exe"))


#set the country, league and season, it may be equal to web page link



class GetData:
    
    def __init__(self):
        
        self.country = navigate.country
        self.name = navigate.league
        self.season = navigate.season
        self.data = [ ]
        self.arrayMatches = []
        

    def getArrayMatches(self):
        self.arrayMatches = navigate.showMoreMatches()
             
    def eachMatchData(self, arrayMatches):
        i = 0
        for match in arrayMatches:
            
            self.data.append(EachMatchData())
            self.data[i].get_dateTimeRound()
            self.data[i].get_homeData()
            self.data[i].get_awayData()
    
            i+= 1

            navigate.closeWindow()
           
class EachMatchData:
    def __init__(self):
            self.date = ''
            self.hour= ''
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
        self.hour = arrayDateTime[1]

        arrayRound = roundInfo.split(' - ROUND ')
        self.round = arrayRound[1]

    def get_homeData(self):
        self.home, self.homeScore, self.homeGoals, self.homeScorer= navigate.eachMatchGoals('home')
        
    def get_awayData(self):
        self.away, self.awayScore, self.awayGoals, self.awayScorer= navigate.eachMatchGoals('away')

    def get_firstHalfHomeStats(self):
        self.firstHalfHomeStats = navigate.eachMatchStats('home', '1RST HALF', True)
        
    def get_secondHalfHomeStats(self):
        self.secondHalfHomeStats = navigate.eachMatchStats('home', '2ND HALF', False)

    def get_firstHalfAwayStats(self):
        self.firstHalfAwayStats = navigate.eachMatchStats('away', '1RST HALF', False)

    def get_secondHalfAwayStats(self):
        self.secondHalfAwayStats = navigate.eachMatchStats('away', '2ND HALF', False)


premierLeague = GetData()



    