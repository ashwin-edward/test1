import time

import keyboard
import pytest
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#class Test_ash():

    # @pytest.fixture()
    # def setup(self):
    #     self.driver = webdriver.Chrome(executable_path=r"G:\ashwin\python project\driver\chromedriver.exe")
    #     self.driver.get('https://in.bookmyshow.com/explore/home/chennai')
    #     self.driver.implicitly_wait(5)
    #
    #     yield
    #     #self.driver.quit()
    #     #time.sleep(5)
    #     print('ashwin')
    # def test_search(self,setup):
    #
    #     search = self.driver.find_element_by_xpath('//span[@id="4"]')
    #     search.click()
    #     WebDriverWait(self.driver,5)
    #     s_bar = self.driver.find_element_by_xpath('//input[@type="text"]')
    #     s_bar.send_keys('TENET')
    #     keyboard.press('ENTER')
    #     keyboard.release('ENTER')
    #     WebDriverWait(self.driver, 5)
    #     book_but = self.driver.find_element_by_xpath(
    #         '//button[@class="CommonContainers__ButtonComponent-sc-1lru625-0 CommonContainers__CtaComponent-sc-1lru625-1 styles__CtaButtonContainer-sc-1fc4j0r-0 hHODJm"]')
    #     book_but.click()
    #     WebDriverWait(self.driver, 5)
    #     language = self.driver.find_element_by_xpath('//div[@class="styles__DimensionComponent-sc-1efo077-3 ifVrUL"][2]')
    #     language.click()
    #     WebDriverWait(self.driver, 5)
    #     teater = self.driver.find_element_by_xpath('//a[@data-session-id="603"]')
    #     teater.click()
    #     WebDriverWait(self.driver, 5)
    #     alrt=self.driver.find_element_by_xpath('//a[@id="btnPopupAccept"]')
    #     alrt.click()
    #     WebDriverWait(self.driver, 5)
    #     seat=self.driver.find_element_by_xpath('//li[@id="pop_4"]')
    #     seat.click()
    #
    #     WebDriverWait(self.driver, 5)
    #     seat_cnfm = self.driver.find_element_by_xpath('class="action-btn"')
    #     seat_cnfm.click()

    # def test_book(self):
    #     print('ash')
    #
    #
    # def test_three(self):
    #
    #     print("test2")

@pytest.mark.parametrize("date,day",[("mon",11),("tue",22),("wen",33)])
def test_like(date,day):
    print(date)
    print(day)
