from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base.navigation_base import NavigationBase

class NavigationDesktop(NavigationBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_container = (By.XPATH, "//button[@aria-haspopup='menu']")
        
    def go_to_settings(self):
        menu_container = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_container)
        )
        menu_container.click()
        settings_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.settings_btn)
        )
        settings_button.click()

    def set_theme_mode(self, mode):
        self.go_to_settings()
        self.change_theme_mode(mode)