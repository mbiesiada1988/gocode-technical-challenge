from json import load

data = load(open('data/home.json'))


class HomePage:
  def __init__(self, page):
    self.get_shop_now_link = page.get_by_role("link", name=data['shop_now_link'], exact=True)
