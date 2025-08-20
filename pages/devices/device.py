from pages.enums.device_type import DeviceType

# Device width thresholds (in pixels)
MOBILE_MAX_WIDTH = 480
TABLET_MAX_WIDTH = 1024

def get_device_type(width: int) -> DeviceType:
    """Return the device type based on screen width."""
    if width <= MOBILE_MAX_WIDTH:
        return DeviceType.MOBILE
    elif width <= TABLET_MAX_WIDTH:
        return DeviceType.TABLET
    else:
        return DeviceType.DESKTOP