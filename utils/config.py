import os

# Environment variable names
BROWSER = "BROWSER"
SCREEN_WIDTH = "SCREEN_WIDTH"
SCREEN_HEIGHT = "SCREEN_HEIGHT"
HEADLESS = "HEADLESS"
OLLAMA_URL = "OLLAMA_URL"

# Default values
DEFAULT_BROWSER = "chrome"
DEFAULT_SCREEN_WIDTH = "1920"
DEFAULT_SCREEN_HEIGHT = "1080"
DEFAULT_HEADLESS = "false"
DEFAULT_OLLAMA_URL = "http://localhost:3000"

class Config:
    @classmethod
    def browser(cls):
        return os.getenv(BROWSER, DEFAULT_BROWSER)

    @classmethod
    def screen_width(cls):
        return int(os.getenv(SCREEN_WIDTH, DEFAULT_SCREEN_WIDTH))

    @classmethod
    def screen_height(cls):
        return int(os.getenv(SCREEN_HEIGHT, DEFAULT_SCREEN_HEIGHT))

    @classmethod
    def headless(cls):
        return os.getenv(HEADLESS, DEFAULT_HEADLESS).lower() == 'true'

    @classmethod
    def ollama_url(cls):
        return os.getenv(OLLAMA_URL, DEFAULT_OLLAMA_URL)