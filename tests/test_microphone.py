import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



class TestMicrophone(unittest.TestCase):
    OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Bypass permission dialog
        chrome_options.add_argument("--use-fake-device-for-media-stream")  # Use a fake microphone
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.OLLAMA_URL)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_microphone_button_animation(self):
        mic_icon = self.driver.find_element(By.CLASS_NAME, "lucide-mic")
        mic_button = mic_icon.find_element(By.XPATH, "./ancestor::button")
        # First Click to activate microphone
        mic_button.click()
        
        span_animation_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'animate-pulse')]")))
        
        self.assertIsNotNone(span_animation_element, "Pulse animation element should be present")   
        self.assertTrue(span_animation_element.is_displayed(), "The span should appear when the microphone is activated")

        # Second Click to deactivate microphone
        time.sleep(2)
        mic_button.click()
        time.sleep(2)