from tokenize import Number
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import copy


#Start Chrome web browser 
# chromeBrowser = webdriver.Chrome(service=Service("./chromedriver.exe"))
chromeBrowser = webdriver.Chrome()

#set the country, league and season, it may be equal to web page link
country = 'england'
league = 'premier-league'
season = '2021-2022'
url = 'https://www.livesport.com/en/soccer/'+ country + '/' + league + '-' + season + '/results/'
dataInfo = {   
            'home': '',
            'away':'',
            'matchDate':'',
            'matchHour': '',
            'matchRound': Number,
            'homeScore': '',
            'awayScore': '',
            'homeLineups': [],
            'awayLineups': [],
            'homeGoals': [],
            'homeScorer': [],
            'awayGoals': [],
            'awayScorer': [],
            'stats': {
                 'firstHalf': {
                     'homeStats': {},
                     'awayStats': {},
                 },
                 'secondHalf': {
                     'homeStats': {},
                     'awayStats': {},
                 }
            }
        }

class GetData:
    

    def __init__(self, url):
        chromeBrowser.get(url)
        self.country = country
        self.name = league
        self.season = season
        self.data = [ ]
        self.arrayMatches = []
        
        
      
    
    def acceptCookies(self):
        try:
            buttonAccept = WebDriverWait(chromeBrowser, 2).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            buttonAccept.click()
        except:
            print('Couldnt reach button')

    def showMoreMatches(self):
        while True:
            try:
                moreMatches = chromeBrowser.find_element(By.LINK_TEXT,'Show more matches') 
                ActionChains(chromeBrowser).scroll_to_element(moreMatches).perform()
                loading = chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text

                while (loading=='LOADING...'):
                    loading = chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text
                
                moreMatches.click()
                print('Clicked')
            except :
                print('Couldnt find click button')
                break

    def getArrayMatches(self):
        self.arrayMatches = chromeBrowser.find_elements(By.XPATH, "//*[starts-with(@id, 'g_1_')]") 
           
    def eachMatchData(self, arrayMatches):
        i = 0
        for match in arrayMatches:
            
            #click on the especific match
            ActionChains(chromeBrowser).scroll_to_element(match).perform()
            match.click()
            chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
            self.acceptCookies()

            #Take home and away info
            self.data.append(copy.deepcopy(dataInfo))
            home = chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__home').text
            away = chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__away').text
            self.data[i]['home'] = home
            self.data[i]['away'] = away
            print(self.data[i]['home'])


            roundContainer = chromeBrowser.find_element(By.CLASS_NAME, 'tournamentHeader__country') 
            roundInfo = roundContainer.find_element(By.TAG_NAME, 'a').text
            arrayRound = roundInfo.split(' - ROUND ')
            round = arrayRound[1]
            self.data[i]['matchRound'] = int(round)

            startTime = chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__startTime').text
            arrayTime = startTime.split(' ')
            date = arrayTime[0]
            hour = arrayTime[1]

            self.data[i]['matchDate'] = date
            self.data[i]['matchHour'] = hour

            score = chromeBrowser.find_element(By.CLASS_NAME, 'detailScore__wrapper')
            results = score.find_elements(By.TAG_NAME, 'span') 
            homeScore = results[0].text
            awayScore = results[2].text
            self.data[i]['homeScore'] = int(homeScore)
            self.data[i]['awayScore'] = int(awayScore)

            goalData = chromeBrowser.find_element(By.CLASS_NAME, 'smv__verticalSections' )
            
            homeGoalContainer = goalData.find_elements(By.CLASS_NAME, 'smv__homeParticipant')
            homeGoals, homeScorer = self.getGoals(homeGoalContainer)
            self.data[i]['homeGoals']= homeGoals
            self.data[i]['homeScorer']= homeScorer
            
            awayGoalContainer = goalData.find_elements(By.CLASS_NAME, 'smv__awayParticipant')
            awayGoals, awayScorer = self.getGoals(awayGoalContainer)
            self.data[i]['awayGoals'] = awayGoals
            self.data[i]['awayScorer'] = awayScorer

            chromeBrowser.find_element(By.LINK_TEXT, 'STATISTICS').click()
            WebDriverWait(chromeBrowser, 2).until(EC.presence_of_element_located((By.LINK_TEXT, '1ST HALF'))).click()

            homeStats1Half = self.getStats('home')
            self.data[i]['stats']['firstHalf']['homeStats'] = homeStats1Half
            
            awayStats1Half = self.getStats('away')
            self.data[i]['stats']['firstHalf']['awayStats'] = awayStats1Half

            WebDriverWait(chromeBrowser, 2).until(EC.presence_of_element_located((By.LINK_TEXT, '2ND HALF'))).click()

            homeStats2Half = self.getStats('home')
            self.data[i]['stats']['secondHalf']['homeStats'] = homeStats2Half
            
            awayStats2Half = self.getStats('away')
            self.data[i]['stats']['secondHalf']['awayStats'] = awayStats2Half

            i+= 1
            chromeBrowser.close()
            chromeBrowser.switch_to.window(chromeBrowser.window_handles[0])

            

    def getGoals(self, dataArray):
        goals = []   
        scorer = [] 

        for data in dataArray:
            try:
                data.find_element(By.CLASS_NAME,'soccer')
                minuteString = data.find_element(By.CLASS_NAME, 'smv__timeBox').text
                minute = minuteString.replace("'","",1)
                goals.append(minute)
                name = data.find_element(By.CLASS_NAME, 'smv__playerName').text
                scorer.append(name)
            except:
                print('Not a Goal')

        return goals, scorer

    def getStats(self, team):
        statsArray = chromeBrowser.find_elements(By.CLASS_NAME, 'stat__category')
        statsObject = {}
        for stat in statsArray:
            try:
                key = stat.find_element(By.CLASS_NAME, 'stat__categoryName').text
                value = stat.find_element(By.CLASS_NAME, 'stat__' + team + 'Value').text
                statsObject[key] = value
            except:
                print('No such Element')
        return statsObject

            

premierLeague = GetData(url)
premierLeague.acceptCookies()
premierLeague.showMoreMatches()
premierLeague.getArrayMatches()
premierLeague.eachMatchData(premierLeague.arrayMatches)       