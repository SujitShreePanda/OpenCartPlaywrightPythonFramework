from playwright.sync_api import Page


class HomePage:
    """Page Object for the Home Page"""
    def __init__(self,page: Page):
        self.page =page

        #=====Locators=====
        #Using Playwright's 'locator' method to identify UI elements

        self.lnk_my_account =page.locator('span:has-text("My Account")')
        self.lnk_register = page.locator('a:has-text("Register")')
        self.lnk_login = page.locator('a:has-text("Login")')
        self.lnk_search_box= page.locator('input[name="search"]')
        self.btn_search = page.locator("button[class='btn btn-default btn-lg']")


    #=====Action Methods=====
    #Each method represents a user interaction on the page.

    def get_home_page_title(self) -> str:
        "Return the title of the home page"
        title = self.page.title()
        return title

    def click_my_account(self):
        "Click on the My Account link"
        try:
            self.lnk_my_account.click()
        except Exception as e:
            print(f"Exception while clicking 'My Account':{e}")
            raise

    def click_register(self):

        try:
            self.lnk_register.click()
        except Exception as e:
            print(f"Exception while clicking 'Register':{e}")
            raise

    def click_login(self):
        """Click on the Login link"""
        try:
            self.lnk_login.click()
        except Exception as e:
            print(f"Exception while clicking 'Login':{e}")
            raise
    def enter_product_name(self, product_name:str):
        "Enter the product name in search box"
        try:
            self.lnk_search_box.fill(product_name)
        except Exception as e:
            print(f"Exception while entering '{product_name}':{e}")
            raise

    def click_search(self):
        "Click on the search button to initiate the product search"
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"Exception while clicking 'Search' button:{e}")
            raise