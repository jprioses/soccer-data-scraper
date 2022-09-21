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
    
    def acceptCookies(self):
        try:
            buttonAccept = WebDriverWait(chromeBrowser, 20).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            buttonAccept.click()
        except:
            print('Couldnt reach button')

    def showMoreMatches(self):
        while True:
            try:
                #loading = WebDriverWait(chromeBrowser, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'loadingAnimation'), ''))
                moreMatches = chromeBrowser.find_element(By.LINK_TEXT,'Show more matches') 
                ActionChains(chromeBrowser).scroll_to_element(moreMatches).perform()
                print(moreMatches)
                loading = chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text

                while (loading=='LOADING...'):
                    loading = chromeBrowser.find_element(By.CLASS_NAME, 'loadingAnimation').text
                
                moreMatches.click()
                print('Clicked')
            except :
                print('Couldnt find click button')
                break


premierLeague = GetData(url)
premierLeague.acceptCookies()
premierLeague.showMoreMatches()       