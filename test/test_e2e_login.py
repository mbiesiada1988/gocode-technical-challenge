import pytest
from playwright.sync_api import Page, expect
from json import load

from models.account import AccountPage
from models.user import UserPage
from models.menu import Menu

sites = load(open('data/pages.json'))
credentials = load(open('data/credentials.json'))

class TestLogin:
    @pytest.fixture
    def setup(self, page: Page):
        page.goto(sites['account']['url'])
        self.account_page = AccountPage(page)

    # will fail because correct credentials are shown on page, and lack of secure HTTP
    def test_basic_security_check(self, page: Page, setup):
        assert self.account_page.get_password_input_type == 'password', 'Password input has wrong type'
        expect(self.account_page.get_username_in_dom).to_have_count(0)
        expect(self.account_page.get_password_in_dom).to_have_count(0)
        assert 'https://' in page.url, 'Unsecure connection'

    def test_empty_login(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        self.account_page.get_username_input.fill(credentials['test_logins']['empty'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_username_input).to_be_focused()

    def test_empty_password(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['empty'])
        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_password_input).to_be_focused()

    def test_empty_credentials(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        self.account_page.get_username_input.fill(credentials['test_logins']['empty'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['empty'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_username_input).to_be_focused()

    def test_username_case_sensitive(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['case_sensitive'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_case_sensitive(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['case_sensitive'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_username_long(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(
          credentials['test_logins']['stress_seed']*credentials['test_logins']['stress_multiplier'])
        self.account_page.get_password_input.fill(credentials['user']['login'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_long(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(
          credentials['test_passwords']['stress_seed']*credentials['test_passwords']['stress_multiplier'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_username_special_signs(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['special_signs'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_special_signs(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['special_signs'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_username_leading_space(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['leading_space'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_leading_space(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['leading_space'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_username_following_space(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['following_space'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_following_space(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['following_space'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_credentials_incorrect(self, page: Page, setup):
        dev = {'type': '', 'msg': ''}
        def handle_console(console):
            dev['type'] = console.type
            dev['msg'] = console.text
        page.on("console", handle_console)

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['incorrect'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['incorrect'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()
        assert dev['type'] != 'error', f'Error in developers console: {dev["msg"]}'

    def test_username_incorrect(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['test_logins']['incorrect'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_password_incorrect(self, page: Page, setup):
        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['test_passwords']['incorrect'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()

    def test_login_happy_path(self, page: Page, setup):
        user_page = UserPage(page)
        dev = {'type': '', 'msg': ''}
        def handle_console(console):
            dev['type'] = console.type
            dev['msg'] = console.text
        page.on("console", handle_console)

        expect(page).to_have_url(sites['account']['url'])

        self.account_page.get_username_input.fill(credentials['user']['login'])
        self.account_page.get_password_input.fill(credentials['user']['password'])
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['user']['url'])
        expect(user_page.get_header).to_be_visible()
        assert dev['type'] != 'error', f'Error in developers console: {dev["msg"]}'

    def test_wcag_navigation_compatibility(self, page: Page, setup):
        user_page = UserPage(page)
        menu = Menu()

        expect(page).to_have_url(sites['account']['url'])

        for element in range(len(menu.get_unlogged_user_menu_items) + 1):
            page.keyboard.press('Tab')
        for letter in credentials['user']['login']:
            page.keyboard.press(letter)
        page.keyboard.press('Tab')
        for letter in credentials['user']['password']:
            page.keyboard.press(letter)
        page.keyboard.press('Enter')

        expect(page).to_have_url(sites['user']['url'])
        expect(user_page.get_header).to_be_visible()

    @pytest.mark.parametrize('test_string', credentials['owasp']['sql_injection'])
    def test_owasp_sql_injection(self, page: Page, setup, test_string):
        dev = {'msg': '', 'type': ''}
        def handle_console(console):
            dev['msg'] = console.text
            dev['type'] = console.type
        page.on("console", handle_console)

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(test_string)
        self.account_page.get_password_input.fill(test_string)
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()
        assert dev['type'] != 'error', f'Error in developers console: {dev["msg"]}'
        assert credentials['user']['login'] not in dev['msg']
        assert credentials['user']['password'] not in dev['msg']

    @pytest.mark.parametrize('test_string', credentials['owasp']['xss'])
    def test_owasp_xss(self, page: Page, setup, test_string):
        alert = {'msg': ''}
        def handle_dialog(dialog):
            alert['msg'] = dialog.message
            dialog.dismiss()
        page.on("dialog", handle_dialog)

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).not_to_be_visible()

        self.account_page.get_username_input.fill(test_string)
        self.account_page.get_password_input.fill(test_string)
        self.account_page.get_login_button.click()

        expect(page).to_have_url(sites['account']['url'])
        expect(self.account_page.get_error_message).to_be_visible()
        assert alert['msg'] != '1', f'String: {test_string} may pose an XSS threat'

    def test_sign_up(self, page: Page):
        pass
