"""
Automatic voting with selenium
Number of drivers could be raised if CPU allows.
"""

import sys
import time
import win32gui
PY_PATH = r'C:\ProgramData\Anaconda3\Lib\site-packages'
sys.path.append(PY_PATH)
from selenium import webdriver


DRIVER_LOCATION = r'C:\Users\james.chan\Downloads\chromedriver_win32\chromedriver.exe'
GOOGLE_CHROME_LOCATION = 'data:, - Google Chrome'
NUMBER_OF_DRIVERS = 4
VOTES_COUNT = 1000
LINK_START = 'https://mcz-livebest.com/music/?id=31'
VOTE_LINK = 'https://mcz-livebest.com/music/?id=84' #31,40,154,83
VOTE_LIMIT = 5 #Number of votes you can do before deleting cookies


def mcz(votes_count, vote_link):
    """
    Perform the vote.
    """
    driver = []

    for i in range(NUMBER_OF_DRIVERS):
        driver.append(webdriver.Chrome(executable_path = DRIVER_LOCATION))
        win32gui.MoveWindow(win32gui.FindWindow(None, DRIVER_LOCATION),
                            2000, 100, 100, 100, True)
        win32gui.MoveWindow(win32gui.FindWindow(None, GOOGLE_CHROME_LOCATION),
                            2000, 100, 100, 100, True)

    for j in range(votes_count):
        #driver.minimize_window()
        for i in range(NUMBER_OF_DRIVERS):
            driver[i].get(LINK_START)
        for m in range(VOTE_LIMIT):
            if m == 0:
                time.sleep(4.5)
            else:
                time.sleep(7)
            for i in range(NUMBER_OF_DRIVERS):
                driver[i].get(vote_link)
            time.sleep(1.5)
            for i in range(NUMBER_OF_DRIVERS):
                driver[i].find_elements_by_css_selector('[href*="#modalConfirm"]')[0].click()
            time.sleep(1.5)
            for i in range(NUMBER_OF_DRIVERS):
                driver[i].find_elements_by_css_selector('a.vote')[0].click()
        time.sleep(1)
        #print(j, 5) #For keep tracking of the votes.
        for i in range(NUMBER_OF_DRIVERS):
            driver[i].delete_all_cookies()

if __name__ == "__main__":
    mcz(VOTES_COUNT, VOTE_LINK)
        #driver[i].quit()
#driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/table/tbody/tr[1]")[1].click()
#driver.find_elements_by_css_selector('[onclick*="showvariance1("]')[0].click()
#driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/table/tbody/tr[2]")[1].click()
#driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/table/tbody/tr[2]")[1].click()
#driver.find_elements_by_css_selector('[onclick*="showvariance1("]')[1].click()
#elements = driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/table/tbody[1]")
