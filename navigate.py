from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class Navigate:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_extension('./plugins/Adblocker_5_3_3_0.crx')
        self.chromeBrowser = webdriver.Chrome(chrome_options=chrome_options)
        
    def openUrl(self, url):
        
        self.chromeBrowser.get(url)
        
        self.chromeBrowser.switch_to.window(self.chromeBrowser.window_handles[1])
        self.chromeBrowser.close()
        self.chromeBrowser.switch_to.window(self.chromeBrowser.window_handles[0])

    def acceptCookies(self):
            try:
                buttonAccept = WebDriverWait(self.chromeBrowser, 2).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
                buttonAccept.click()
            except:
                print('Couldnt reach button')

    def showMoreMatches(self):
        arrayAllMatches = []
        while True:
            try:
                moreMatches = self.chromeBrowser.find_element(By.LINK_TEXT,'Show more matches') 
                ActionChains(self.chromeBrowser).scroll_to_element(moreMatches).perform()
                loading = self.chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text

                while (loading=='LOADING...'):
                    loading = self.chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text
                
                moreMatches.click()
                print('Clicked')
            except :
                arrayAllMatches = self.chromeBrowser.find_elements(By.XPATH, "//*[starts-with(@id, 'g_1_')]") 
                print('Couldnt find click button')
                return arrayAllMatches

    def eachMatch(self,match):
        #ActionChains(self.chromeBrowser).scroll_from_origin(ScrollOrigin.from_element(match),196,300).perform()
        ActionChains(self.chromeBrowser).scroll_to_element(match).perform()
        match.click()
        self.chromeBrowser.switch_to.window(self.chromeBrowser.window_handles[1])
        self.acceptCookies()

    def eachMatchInfo(self):

        dateTime = self.chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__startTime').text
        
        roundContainer = self.chromeBrowser.find_element(By.CLASS_NAME, 'tournamentHeader__country') 
        roundInfo = roundContainer.find_element(By.TAG_NAME, 'a').text
        
        return dateTime, roundInfo

    def eachMatchGoals(self,team):
        teamName = self.chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__' + team).text
        scoreContainer = self.chromeBrowser.find_element(By.CLASS_NAME, 'detailScore__wrapper')
        scoreArray = scoreContainer.find_elements(By.TAG_NAME, 'span') 

        if (team=='home'):
            score = int(scoreArray[0].text)
        if (team=='away'):
            score = int(scoreArray[2].text)

        goalData = self.chromeBrowser.find_element(By.CLASS_NAME, 'smv__verticalSections' )
                
        goalContainer = goalData.find_elements(By.CLASS_NAME, 'smv__' + team + 'Participant')

        goals = []   
        scorer = [] 
        asist = []

        for data in goalContainer:
            try:
                data.find_element(By.CLASS_NAME,'soccer')
                minuteString = data.find_element(By.CLASS_NAME, 'smv__timeBox').text
                minute = minuteString.replace("'","",1)
                goals.append(minute)
                name = data.find_element(By.CLASS_NAME, 'smv__playerName').text
                asistName = data.find_element(By.CLASS_NAME, 'smv__assist').find_element(By.TAG_NAME, 'a').text
                scorer.append(name)
                asist.append(asistName)
            except:
                print('Not a Goal')
        
        return teamName, score, goals, scorer, asist

    def eachMatchStats(self,team, half, isStatsClicked, isHalfClicked):

        if (not(isStatsClicked)):
            self.chromeBrowser.find_element(By.LINK_TEXT, 'STATS').click()
        if (not(isHalfClicked)):
            WebDriverWait(self.chromeBrowser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, half))).click()   

        
        statsArray = self.chromeBrowser.find_elements(By.CLASS_NAME, 'stat__category')
        statsObject = {}
        for stat in statsArray:
            try:
                key = stat.find_element(By.CLASS_NAME, 'stat__categoryName').text
                value = stat.find_element(By.CLASS_NAME, 'stat__' + team + 'Value').text
                statsObject[key] = value
            except:
                print('No such Element')

        return statsObject
    
    def eachMatchOdds(self):

        homeOdds = 0
        evenOdds = 0
        awayOdds = 0
        over0 = 0
        under0 = 0
        over1 = 0
        under1 = 0
        over2 = 0
        under2 = 0
        over3 = 0
        under3 = 0

        try:
            self.chromeBrowser.find_element(By.LINK_TEXT, 'ODDS').click()
            WebDriverWait(self.chromeBrowser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'ui-table__row')))
            table = self.chromeBrowser.find_element(By.CLASS_NAME, 'ui-table__row')
            odds = table.find_elements(By.CLASS_NAME,'oddsCell__odd')
            homeOdds = odds[0].text
            evenOdds = odds[1].text
            awayOdds = odds[2].text
            print('ODDS ARE: ' + homeOdds + ' ' + evenOdds + ' ' + awayOdds)
        except:
            print('No MoneyLine Odds')

        try:    
            self.chromeBrowser.find_element(By.LINK_TEXT,'O/U').click()
            WebDriverWait(self.chromeBrowser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'ui-table__row')))
            table =self.chromeBrowser.find_elements(By.CLASS_NAME,'ui-table__row')
            for odd in table:
                type = odd.find_element(By.CLASS_NAME, 'oddsCell__noOddsCell')
                if type=='0.5': 
                    odds = odd.find_elements(By.CLASS_NAME,'oddsCell__odd')
                    over0 = odds[0]
                    under0 = odds[1]
                if type=='1.5': 
                    odds = odd.find_elements(By.CLASS_NAME,'oddsCell__odd')
                    over1 = odds[0]
                    under1 = odds[1]
                if type=='2.5': 
                    odds = odd.find_elements(By.CLASS_NAME,'oddsCell__odd')
                    over2 = odds[0]
                    under2 = odds[1]
                if type=='3.5': 
                    odds = odd.find_elements(By.CLASS_NAME,'oddsCell__odd')
                    over3 = odds[0]
                    under3 = odds[1]
        except:
            print('No O/U Odds')
        

    def closeWindow(self):
        self.chromeBrowser.close()
        self.chromeBrowser.switch_to.window(self.chromeBrowser.window_handles[0])

    def closeBrowser(self):
        self.chromeBrowser.close()



    
