import os
import unittest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
import time

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set
class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(OLLAMA_URL)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.assertIn('Ollama UI', self.driver.title)
    
    def test_send_message(self):
        self.driver.implicitly_wait(2)
        
        # select model
        model_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-state='closed'][role='combobox']")
        model_button.click()
        
        self.driver.implicitly_wait(2)
        model_option = self.driver.find_element(By.XPATH, "//button[normalize-space(text())='gemma3:1b']")
        model_option.click()
        self.driver.implicitly_wait(2)
        
        send_icon = self.driver.find_element(By.CLASS_NAME, "lucide-send-horizontal")
        send_button = send_icon.find_element(By.XPATH, "./ancestor::button")
        # send button should be disabled
        self.assertTrue(send_button.get_attribute("disabled") is not None)
        query_textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Enter your prompt here']")
        query_textarea.send_keys("Hello, Ollama!")
        # send button should be enabled
        self.assertTrue(send_button.get_attribute("disabled") is None)
        
        send_icon.click()
        