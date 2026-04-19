from json import load
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
  parser.addoption("--config", action="store", default="config.json", help="Path to configuration file")
  parser.addoption("--browser_name", action="store", default=None, help="Browser name")
  parser.addoption("--env", action="store", default=None, help="Base URL")


def get_config(pytestconfig):
  cli_config = pytestconfig.getoption("--config")
  with open(cli_config, "r") as file:
    config_file = load(file)
  cli_browser = pytestconfig.getoption("--browser_name")
  cli_url = config_file["environments"].get(pytestconfig.getoption("--env")) or pytestconfig.getoption("--env")

  return {
    "browser": cli_browser or config_file["browser"],
    "base_url": cli_url or config_file["environments"][config_file["env"]],
    "headless": not pytestconfig.getoption("--headed"),
    "slowmo": pytestconfig.getoption("--slowmo"),
  }


@pytest.fixture(scope="session")
def config(pytestconfig):
  return get_config(pytestconfig)


@pytest.fixture(scope="session")
def browser(config):
  with sync_playwright() as playwright:
    browser_type = getattr(playwright, config["browser"])
    browser = browser_type.launch(headless=config["headless"], slow_mo=config["slowmo"])
    yield browser
    browser.close()


@pytest.fixture
def page(browser, config):
  context = browser.new_context(base_url=config["base_url"])
  page = context.new_page()
  yield page
  context.close()
