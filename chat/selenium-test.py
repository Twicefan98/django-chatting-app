from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class ChatSeleniumTests(ChannelsLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    # Utility Functions
    # def _enter_chat_room(self):
        