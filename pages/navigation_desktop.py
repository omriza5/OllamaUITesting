from pages.base.navigation_base import NavigationBase

class NavigationDesktop(NavigationBase):
    def __init__(self, driver):
        super().__init__(driver)

    def set_theme_mode(self, mode):
        self.go_to_settings()
        self.change_theme_mode(mode)