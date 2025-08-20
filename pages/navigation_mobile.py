from selenium.webdriver.common.by import By
from pages.base.navigation_base import NavigationBase

class NavigationMobile(NavigationBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.hamburger_menu_icon = (By.CSS_SELECTOR, "button[aria-controls='radix-:rh:'] svg")

    def open_side_nav(self):
        hamburger_menu = self.driver.find_element(*self.hamburger_menu_icon)
        hamburger_menu.click()
    
    def set_theme_mode(self, mode):
        self.open_side_nav()
        self.go_to_settings()
        self.change_theme_mode(mode)
        