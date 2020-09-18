from selenium import webdriver
from applications.bookmyshow.lib.Locators import Locator
from selenium.webdriver.common.by import By
import os
import logging
import time
import datetime

class  HomePage(object):

    def __init__(self):
        self.driver_path = "C:\\Users\\srihari\\PycharmProjects\\AutomationFramework\\dependencies\\drivers\\chrome\\chromedriver.exe"
        if not os.path.exists(self.driver_path):
            print(f"Not able to find web driver. path {self.driver_path}")
        self.driver = None
        self.launch_app()
        self.search_city()
        self.select_city()
        self.launch_app_with_popup_suppressed()
        #self.navigate_movies()

    def launch_app(self, timeout=10):
        try:
            self.driver = webdriver.Chrome(executable_path=self.driver_path)
            self.driver.get("https://in.bookmyshow.com/")
            time.sleep(timeout)
            self.driver.maximize_window()
            print("launching application is successfull")
            print("Run Started at:" + str(datetime.datetime.now()))
        except Exception as e:
            print("Error while launching the application")


    def search_city(self):
        try:
            self.searchcity= self.driver.find_element(By.XPATH,Locator.Searchcity)
            self.searchcity.send_keys("pune")
            print("searching succesfully")

        except Exception as e:
            print("error while searching city")
    def select_city(self):
        try:
            time.sleep(2)
            self.selectcity = self.driver.find_element(By.XPATH,Locator.Selectcity)
            self.selectcity.click()
            print("city selected")
        except Exception as e:
            print("error while clicking city")
    def launch_app_with_popup_suppressed(self):
        try:
            time.sleep(10)
            self.pop_up = self.driver.find_element(By.XPATH,Locator.pop_up)
            self.pop_up.click()
            print("pop_up handled succesfully")
        except Exception as e:
            print("Error while handling pop_up")

    def navigate_movies(self):
        try:
            self.Movies = self.driver.find_element(By.XPATH,Locator.Movies)
            self.Movies.click()
            print("movies open succesfully")
        except Exception as e:
            print("error occurred while navigating to movies")



if __name__ == "__main__":
    h = HomePage()
    h.navigate_movies()