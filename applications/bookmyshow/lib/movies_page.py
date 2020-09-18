from applications.bookmyshow.lib.home_page import HomePage
from selenium.webdriver.common.by import By
from applications.bookmyshow.lib.Locators import Locator

class MoviesPage(HomePage):

    def navigate_now_showning(self):
        try:
            self.NowShowing = self.driver.find_element(By.XPATH,Locator.NowShowing)
            self.NowShowing.click()
            print("navigate to now_showing success")
        except Exception as e:
            print("error navigating to now_showing")
    def navigate_comingsoon(self):
        try:
            self.navigate_movies()
            self.comingsoon = self.driver.find_element(By.XPATH, Locator.comingsoon)
            self.comingsoon.click()
            print("navigate to comingsoon is success")
        except Exception as e:
            print("error navigating to comingsoon. Error: {}".format(str(e)))
    def navigate_Exclusive(self):
        try:
            self.Exclusive = self.driver.find_element(By.XPATH, Locator.Exclusive)
            self.Exclusive.click()
        except Exception as e:
            print("error navigating to Exclusive")

if __name__ == "__main__":
    s = MoviesPage()
    s.navigate_comingsoon()