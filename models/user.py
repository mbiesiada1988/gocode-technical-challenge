from json import load

sites = load(open('data/pages.json'))
credentials = load(open('data/credentials.json'))


class UserPage:
  def __init__(self, page):
    self.get_header = page.get_by_role("heading", name=sites['user']['header'] + credentials['user']['name'])
