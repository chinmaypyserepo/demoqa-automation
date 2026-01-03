from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage

class BookStorePage(BasePage):
    SEARCH_BOX = (By.ID, "searchBox")
    BOOK_ROWS = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")

    def open_books_page(self, url):
        self.driver.get(url)

    def search(self, text):
        self.type(self.SEARCH_BOX, text)

    def book_count(self):
        self.wait_visible(self.BOOK_ROWS)
        return len(self.driver.find_elements(*self.BOOK_ROWS))
