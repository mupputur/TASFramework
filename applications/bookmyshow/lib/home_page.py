from selenium import webdriver
from applications.bookmyshow.lib.Locators import Locator
from selenium.webdriver.common.by import By
from applications.bookmyshow.lib.loggers import Logger
import os
import time



class  HomePage():
    def __init__(self):
        self.driver_path = "C:\\Users\\srihari\\PycharmProjects\\AutomationFramework\\dependencies\\drivers\\chrome\\chromedriver.exe"
        L = Logger()
        if not os.path.exists(self.driver_path):
            L.log_error(f"Not able to find web driver. path {self.driver_path}")
        self.driver = None
        self.launch_app()
        self.search_city()
        self.select_city()
        self.launch_app_with_popup_suppressed()
        self.Logger = None



        #self.navigate_movies()

    def launch_app(self, timeout=10):
        L = Logger()
        try:

            self.driver = webdriver.Chrome(executable_path=self.driver_path)
            self.driver.get("https://in.bookmyshow.com/")
            time.sleep(timeout)
            L.log_info("launching application is successfull")
        except Exception as e:
            L.log_error("Error while launching the application")


    def search_city(self):
        L = Logger()
        try:

            self.searchcity= self.driver.find_element(By.XPATH,Locator.Searchcity)
            self.searchcity.send_keys("pune")
            L.log_info("searching succesfully")

        except Exception as e:
            L.log_error("error while searching city")
    def select_city(self):

        L = Logger()
        try:
            time.sleep(2)
            self.selectcity = self.driver.find_element(By.XPATH,Locator.Selectcity)
            self.selectcity.click()
            L.log_info("city selected")
        except Exception as e:
            L.log_error("error while clicking city")

    def launch_app_with_popup_suppressed(self):
        L = Logger()
        try:

            time.sleep(10)
            self.pop_up = self.driver.find_element(By.XPATH,Locator.pop_up)
            self.pop_up.click()
            L.log_info("pop_up handled succesfully")
        except Exception as e:
            L.log_error("Error while handling pop_up")

    def navigate_movies(self):
        L = Logger()
        try:
            self.Movies = self.driver.find_element(By.XPATH,Locator.Movies)
            self.Movies.click()
            L.log_info("movies open succesfully")
        except Exception as e:
            L.log_error("error occurred while navigating to movies")


if __name__ == "__main__":
    h = HomePage()
    h.navigate_movies()
