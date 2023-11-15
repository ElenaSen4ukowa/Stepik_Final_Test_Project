from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
# from .login_page import LoginPage # для переходов между страницами

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) # для переходов между страницами
        alert = self.browser.switch_to.alert # инкапсуляция бизнес-логики в методах
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
