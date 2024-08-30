from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

"""Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
chrome_options = Options()
chrome_options.binary_location = os.getenv('CHROME_BINARY', '/default/path/to/chrome')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

# Close the browser


class SeleniumController:

    def __init__(self):
        pass

    # Initialize the Chrome WebDriver
    # Creates new instance of chrome and opens url for count time
    def createInstance(self, url, count):
        service_path = os.getenv('CHROMEDRIVER_PATH', '/default/path/to/chromedriver')
        service = Service(service_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # Open a specific URL
        driver.get(url)

        # Wait for the page to load
        time.sleep(count)

        # Perform a hard refresh by clearing the cache and reloading
        driver.execute_script("window.location.reload(true);")

        # Wait for the hard refresh to complete
        time.sleep(3)

        # Close the browser
        driver.quit()

