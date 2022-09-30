from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chromeBrowser = webdriver.Chrome()

def openUrl(url):
    
    chromeBrowser.get(url)

def acceptCookies():
        try:
            buttonAccept = WebDriverWait(chromeBrowser, 2).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            buttonAccept.click()
        except:
            print('Couldnt reach button')

def showMoreMatches():
    arrayAllMatches = []
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
            arrayAllMatches = chromeBrowser.find_elements(By.XPATH, "//*[starts-with(@id, 'g_1_')]") 
            print('Couldnt find click button')
            return arrayAllMatches

def eachMatch(match):
    ActionChains(chromeBrowser).scroll_to_element(match).perform()
    match.click()
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
    acceptCookies()

def eachMatchInfo():

    dateTime = chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__startTime').text
    
    roundContainer = chromeBrowser.find_element(By.CLASS_NAME, 'tournamentHeader__country') 
    roundInfo = roundContainer.find_element(By.TAG_NAME, 'a').text
    
    return dateTime, roundInfo

def eachMatchGoals(team):
    teamName = chromeBrowser.find_element(By.CLASS_NAME, 'duelParticipant__' + team).text
    scoreContainer = chromeBrowser.find_element(By.CLASS_NAME, 'detailScore__wrapper')
    scoreArray = scoreContainer.find_elements(By.TAG_NAME, 'span') 

    if (team=='home'):
        score = int(scoreArray[0].text)
    if (team=='away'):
        score = int(scoreArray[2].text)

    goalData = chromeBrowser.find_element(By.CLASS_NAME, 'smv__verticalSections' )
            
    goalContainer = goalData.find_elements(By.CLASS_NAME, 'smv__' + team + 'Participant')

    goals = []   
    scorer = [] 

    for data in goalContainer:
        try:
            data.find_element(By.CLASS_NAME,'soccer')
            minuteString = data.find_element(By.CLASS_NAME, 'smv__timeBox').text
            minute = minuteString.replace("'","",1)
            goals.append(minute)
            name = data.find_element(By.CLASS_NAME, 'smv__playerName').text
            scorer.append(name)
        except:
            print('Not a Goal')

    return teamName, score, goals, scorer

def eachMatchStats(team, half, isStatsClicked, isHalfClicked):

    if (not(isStatsClicked)):
        chromeBrowser.find_element(By.LINK_TEXT, 'STATISTICS').click()
    if (not(isHalfClicked)):
        WebDriverWait(chromeBrowser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, half))).click()   

    
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

def closeWindow():
    chromeBrowser.close()
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[0])

def closeBrowser():
    chromeBrowser.close()



    
