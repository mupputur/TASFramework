from selenium import webdriver
import os
import time

class  HomePage:

    def __init__(self):
        self.driver_path = "C:\\Users\\srihari\\PycharmProjects\\AutomationFramework\\dependencies\\drivers\\chrome\\chromedriver.exe"
        if not os.path.exists(self.driver_path):
            print(f"Not able to find web driver. path {self.driver_path}")
        self.driver = None
        self.launch_app()

    def launch_app(self, timeout=10):
        try:
            self.driver = webdriver.Chrome(executable_path=self.driver_path)
            self.driver.get("https://in.bookmyshow.com/")
            time.sleep(timeout)
            self.driver.maximize_window()
        except Exception as e:
            print("Error while launching the application")

    def launch_app_with_popup_suppressed(self):
        pass

    def navigate_movies(self):
        pass

    def navigate_sports(self):
        pass

    def navigate_events(self):
        pass

    def navigate_activities(self):
        pass

class MoviesPage:

    def navigate_now_showig(self):
        pass

class  SportsPage:

    def navigate_to_cricket(self):
        pass
if __name__ == "__main__":
    h = HomePage()