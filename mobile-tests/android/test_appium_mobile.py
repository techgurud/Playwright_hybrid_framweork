from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import pytest

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'emulator-5554',
        'app': '/path/to/your/app.apk',
        'automationName': 'UiAutomator2'
    }

    # Ensure desired_caps is not None
    if desired_caps is None:
        raise ValueError("Desired capabilities must be defined")

    driver = webdriver.Remote("http://localhost:4724/wd/hub", desired_caps)
    yield driver
    driver.quit()

def test_sample(driver: WebDriver):
    # Add your mobile test steps here
    assert driver is not None
