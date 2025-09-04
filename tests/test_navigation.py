import unittest
from utils.driver_factory import get_driver
from utils.config import Config
from utils.page_factory import get_navigation_page
from pages.enums.theme_mode import ThemeMode
from utils.config import Config
import allure
from allure import severity_level
class TestNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.navigation_page = get_navigation_page(self.driver, Config.screen_width())
        self.driver.get(Config.ollama_url())
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    @allure.severity(severity_level.CRITICAL)
    @allure.label("test_device_name", Config.test_device_name())
    def test_dark_mode(self):
        self.navigation_page.set_theme_mode(ThemeMode.DARK)
        self.assertEqual(self.navigation_page.get_current_theme_mode(), ThemeMode.DARK)
        
        # [ ] - add return self for chaining use
        
