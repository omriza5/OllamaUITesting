from pages.devices.device import get_device_type
from pages.enums.device_type import DeviceType
from pages.navigation_mobile import NavigationMobile
from pages.navigation_desktop import NavigationDesktop

def get_navigation_page(driver, width):
    device_type = get_device_type(width)
    if device_type == DeviceType.MOBILE:
        return NavigationMobile(driver)
    else:
        return NavigationDesktop(driver)