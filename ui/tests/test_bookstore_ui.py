import time
import allure
from ui.pages.bookstore_page import BookStorePage
from config.settings import UI_BASE_URL


@allure.title("Verify Book Store page loads and books are visible")
@allure.feature("Book Store UI")
def test_books_visible_on_ui(browser):
    page = BookStorePage(browser)

    with allure.step("Open Book Store page"):
        page.open_books_page(f"{UI_BASE_URL}/books")
        time.sleep(3)   # 👈 see page load

    with allure.step("Validate books are displayed"):
        count = page.get_books_count()
        time.sleep(2)   # 👈 see table
        assert count > 0
