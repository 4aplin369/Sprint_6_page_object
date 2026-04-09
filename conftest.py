import pytest
import src.data as data

from selenium import webdriver


def browser_settings():
    driver_options = webdriver.FirefoxOptions()
    width, height = data.RESOLUTION
    driver_options.add_argument(f"--width={width}")
    driver_options.add_argument(f"--height={height}")

    return driver_options


@pytest.fixture
def driver():
    driver = webdriver.Firefox(options=browser_settings())
    driver.get(data.DEFAULT_URL)
    yield driver
    driver.quit()
