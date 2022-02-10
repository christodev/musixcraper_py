from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


"Method to Extract Lyrics from List of WebElement containing scattered lyrics"
# def ExtractLyricsFromList(listOfScatteredLyricsWebElts: List[WebElement]) -> list:
def ExtractLyricsFromList(listOfScatteredLyricsWebElts: List[WebElement]) -> list:
    lyrics = list("")
    for webElt in listOfScatteredLyricsWebElts:
        lyrics.append(webElt.text)
    return lyrics        

"Method to get browser Configuration"
def GetBrowserOptions() -> Options:
    options = Options()
    # Deciding whether to show UI or not
    # options.headless = False;
    options.add_experimental_option("detach", True) #Ta ma ysakir bas ykhalis

"Method to Search for the Lyrics of a song"
def SearchForLyrics() -> str:
    options = GetBrowserOptions();

    DRIVER_PATH = '/Users/kik/Downloads/chromedriver'

    browser = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)

    #IMPORTANT DO NOT TOUCH 
    #ta ma ya3te errors metel Elt not interactable (when clicking a btn)
    browser.implicitly_wait(100)

    browser.get('https://www.musixmatch.com')

    #Grab the SEARCH INPUT
    searchInput = browser.find_element(By.CLASS_NAME,'mui-input--search-bar')

    #Grab the BTN
    # submitBtn = driver.find_element(By.CLASS_NAME,'gNO89b')

    #Write into the SEARCH INPUt
    searchInput.send_keys('woman')

    #CLICK THE SEARCH BTN
    searchInput.send_keys(Keys.RETURN)

    # browser.implicitly_wait(130)
    ##NOW WE REACHED RESULTS PAGE
    #Grab first RESULT (<a> tag)
    firstResult = browser.find_element(By.CLASS_NAME, 'title')

    #Click on it
    firstResult.click()

    ##NEXT TIME REMOVE THE LINK OF THE LYRICS AND START BROWSING FROM SCRATCH##
    print(f"firstResult: {firstResult}")
    #Find the Lyrics Elements
    # lyricsElts = browser.find_elements(By.CLASS_NAME, 'lyrics__content__ok')

    # wait for the elt
    lyricsElts = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='lyrics__content__ok']")))
    # lyricsElts = browser.find_elements(By.XPATH, "//span[@class='lyrics__content__ok']")
    # lyricsElts = browser.find_elements(By.TAG_NAME, "span");
    
    print(f"lyricsElts: {lyricsElts}")

    lyricsList = list("")
    for webElt in lyricsElts:
        lyricsList.append(webElt.text)

    #Extract the lyrics
    lyrics = "".join(lyricsList)

    # driver.close()

if __name__ == '__main__':
    # lyrics = SearchForLyrics()
    print("lyrics")