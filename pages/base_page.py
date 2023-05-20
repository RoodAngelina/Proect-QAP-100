from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.url = url
        self.driver.implicitly_wait(timeout)
