import pytest
from playwright.sync_api import Page, expect
from json import load

from models.menu import Menu

sites = load(open('data/pages.json'))
menu = Menu()


class TestMenu:
  @pytest.mark.parametrize('menu_item', menu.get_unlogged_user_menu_items)
  def test_menu(self, page: Page, menu_item: str):
    dev = {'type': '', 'msg': ''}

    def handle_console(console):
      dev['type'] = console.type
      dev['msg'] = console.text

    page.on("console", handle_console)

    page.goto(sites['home']['url'])
    page.get_by_role('link', name=sites[menu_item]['menu_button']).click()

    expect(page).to_have_url(sites[menu_item]['url'])
    expect(page).to_have_title(sites[menu_item]['title'])
    expect(page.get_by_role('heading', name=sites[menu_item]['header'], exact=True)).to_be_visible()
    assert dev['type'] != 'error', f'Dev console error: {dev["msg"]}'
