from playwright.sync_api import Page, expect
from json import load

from models.home import HomePage

sites = load(open('data/pages.json'))


class TestHome:
  def test_shop_now(self, page: Page):
    home = HomePage(page)

    page.goto(sites['home']['url'])
    home.get_shop_now_link.click()

    expect(page).to_have_url(sites['products']['url'])
    expect(page).to_have_title(sites['products']['title'])
    expect(page.get_by_role('heading', name=sites['products']['header'], exact=True)).to_be_visible()
