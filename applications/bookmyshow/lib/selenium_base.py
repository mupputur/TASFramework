import datetime
from selenium import webdriver

class SeleniumBase:

    def __init__(self):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        print("_______________________________________________")
        print("Test environment is started")
        print("Run Started at:" + str(datetime.datetime.now()))


s = SeleniumBase()
s.setUp()