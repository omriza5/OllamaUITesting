from selenium.webdriver.common.by import By
from pages.enums.theme_mode import ThemeMode

class NavigationBase:
    def __init__(self, driver):
        self.driver = driver 
        self.menu_container = (By.XPATH, "//button[@aria-haspopup='menu']")
        self.settings_btn = (By.XPATH, "//button[.//div[@role='menuitem']//div[contains(., 'Settings')]]")
        self.main_html_tag = (By.TAG_NAME, "html")

    def set_theme_mode(self, mode):
        raise NotImplementedError("Subclasses must implement set_theme_mode()")
    
    def go_to_settings(self):
        menu_container = self.driver.find_element(*self.menu_container)
        menu_container.click()
        settings_button = self.driver.find_element(*self.settings_btn)
        settings_button.click()

    def change_theme_mode(self, mode):
        theme_button = self.driver.find_element(
            By.XPATH,
            f"//button[.//p[text()='{mode.value}']]"
        )
        theme_button.click()
        
    def get_current_theme_mode(self):
        DARK_MODE = "dark"
        LIGHT_MODE = "light"
        
        html_class = self.driver.find_element(*self.main_html_tag).get_attribute("class")
        if DARK_MODE in html_class:
            return ThemeMode.DARK
        elif LIGHT_MODE in html_class:
            return ThemeMode.LIGHT
        else:
            return None