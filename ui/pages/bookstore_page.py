from selenium.webdriver.common.by import By


class BookStorePage:
    def __init__(self, driver):
        self.driver = driver

    def open_books_page(self, url):
        self.driver.get(url)

    def get_books_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "rt-tr-group"))
