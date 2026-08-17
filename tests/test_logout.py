"""
Test Case: User Logout Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Navigate to the "My Account" menu and click on "Login".
3. Enter valid user credentials (email and password).
4. Click on the "Login" button.
5. Verify that the "My Account" page is displayed.
6. Click on the "Logout" link or button.
7. Verify that the Logout confirmation page is displayed.
8. Click the "Continue" button to return to the Home page.
9. Verify that the Home page is displayed by checking its title.

Expected Result:
----------------
After logging out, the user should be redirected to the Logout confirmation page.
Clicking "Continue" should navigate back to the Home page successfully.
"""


from playwright.sync_api import expect

from pages import logout_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.my_account_page import MyAccountPage
from config import Config


def test_user_logout(page):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)
    my_logout_page = LogoutPage(page)


    home_page.click_my_account()
    home_page.click_login()

    login_page.login(Config.email,Config.password)

    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)

    '''
    #here we used logout page through my account page, this is called chaining of Page Object class
    logout_page=my_account_page.click_logout()

    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)

    logout_page.click_continue()

    expect(page).to_have_title("Your Store")
    '''

    #by using logout page directly we can automate
    my_account_page.click_logout()

    expect(my_logout_page.get_continue_button()).to_be_visible(timeout=3000)
    my_logout_page.click_continue()
    expect(page).to_have_title("Your Store")
