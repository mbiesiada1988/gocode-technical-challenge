from json import load

data = load(open('data/account.json'))
credentials = load(open('data/credentials.json'))

class AccountPage:
    def __init__(self, page):
        self.get_username_input = page.get_by_placeholder(data["username_placeholder"], exact=True)
        self.get_password_input = page.get_by_placeholder(data["password_placeholder"], exact=True)
        self.get_password_input_type = page.get_attribute('[id="password"]', 'type')
        self.get_login_button = page.get_by_role("button", name=data["login_button"], exact=True)
        self.get_error_message = page.get_by_text(data["login_error_message"], exact=True)
        self.get_username_in_dom = page.get_by_text(credentials['user']['login'])
        self.get_password_in_dom = page.get_by_text(credentials['user']['password'])
        self.get_sign_up_link = page.get_by_role("")