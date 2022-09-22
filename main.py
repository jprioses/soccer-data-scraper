from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np

#Start Chrome web browser 
# chromeBrowser = webdriver.Chrome(service=Service("./chromedriver.exe"))
chromeBrowser = webdriver.Chrome()

#set the country, league and season, it may be equal to web page link
country = 'england'
league = 'premier-league'
season = '2021-2022'
url = 'https://www.livesport.com/en/soccer/'+ country + '/' + league + '-' + season + '/results/'


class GetData:
    def __init__(self, url):
        chromeBrowser.get(url)
        self.arrayMatches = []
        self.stringMatchesGeneral = ''
        self.homeGoals = []
    
    def acceptCookies(self):
        try:
            buttonAccept = WebDriverWait(chromeBrowser, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
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
        self.stringMatchesGeneral = chromeBrowser.find_element(By.ID, 'live-table').text 
            
    def eachMatchData(self, arrayMatches):
        for match in arrayMatches:
            ActionChains(chromeBrowser).scroll_to_element(match).perform()
            match.click()
            chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
            self.acceptCookies()
            goalData = chromeBrowser.find_element(By.CLASS_NAME, 'smv__verticalSections' )
            print(goalData)
            

premierLeague = GetData(url)
premierLeague.acceptCookies()
premierLeague.showMoreMatches()
premierLeague.getArrayMatches()
premierLeague.eachMatchData(premierLeague.arrayMatches)       