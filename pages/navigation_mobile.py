import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base.navigation_base import NavigationBase

class NavigationMobile(NavigationBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.hamburger_menu_icon = (By.CSS_SELECTOR, "button[data-testid='hamburger-menu']")
        self.menu_container = (By.XPATH, "//div[@role='dialog']//div[2]//button[1]")

    def open_side_nav(self):
        hamburger_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.hamburger_menu_icon)
        )
        hamburger_menu.click()

    def go_to_settings(self):
        self.open_side_nav()
        menu_container = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_container)
        )
        menu_container.click()
        # time.sleep(50)
        settings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.settings_btn)
        )
        settings_button.click()

    def change_theme_mode(self, mode):
        theme_button = self.driver.find_element(
            By.XPATH,
            f"//button[.//p[text()='{mode.value}']]"
        )
        theme_button.click()
        
    def set_theme_mode(self, mode):
        self.go_to_settings()
        self.change_theme_mode(mode)
