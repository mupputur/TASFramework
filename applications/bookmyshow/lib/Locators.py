class Locator(object):

# home page locators
      Movies = "//a[contains(text(),'Movies')]"
      Events = "//a[contains(text(),'Events')]"
      Sports = "//a[contains(text(),'Sports')]"
# pop-up handling
      pop_up = "//*[@id='wzrk-cancel']"
#search city
      Searchcity = "//input[@id='inp_RegionSearch_top']"
# select city
      Selectcity = "//strong[@class='tt-highlight']"

# Page open confirmation locators for movies
      Movies_button = "//a[contains(text(),'Movies')]"
      NowShowing = "//a[@id='now-showing-btn']"
      comingsoon = "//a[@id='coming-soon-btn']"
      Exclusive = "//a[@id='exclusives-btn']"
# page open confirmation locators for events
      All = "//a[@class='df-ai df-ap df-aq df-ar df-as df-q']"
      Conferences = "//a[@class='df-ai df-ap df-ar df-as df-at df-q'][contains(text(),'Conferences')]"
      Screening = "//a[@class='df-ai df-ap df-ar df-as df-at df-q'][contains(text(),'Screening')]"
# page open confirmation locators for sports
      Cycling = "//a[@class='df-ai df-ap df-ar df-as df-at df-q'][contains(text(),'Cycling')]"
      Cricket = "//a[@class='df-ai df-ap df-ar df-as df-at df-q'][contains(text(),'Cricket')]"
      Running = "//a[@class='df-ai df-ap df-ar df-as df-at df-q'][contains(text(),'Running')]"