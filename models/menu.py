from json import load

sites = load(open('data/pages.json'))


class Menu:
  def __init__(self):
    self.get_logged_user_menu_items = [
      item for item in list(sites.keys()) if sites[item]['access'] in ['logged', 'both']
    ]
    self.get_unlogged_user_menu_items = [
      item for item in list(sites.keys()) if sites[item]['access'] in ['unlogged', 'both']
    ]
