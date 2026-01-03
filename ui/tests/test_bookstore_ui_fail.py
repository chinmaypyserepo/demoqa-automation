import time
import allure
from ui.pages.bookstore_page import BookStorePage
from config.settings import UI_BASE_URL


@allure.title("Force failure to verify Allure report")
@allure.feature("Book Store UI")
def test_books_failure_demo(browser):
    page = BookStorePage(browser)

    with allure.step("Open Book Store page"):
        page.open_books_page(f"{UI_BASE_URL}/books")
        time.sleep(3)

    with allure.step("Force failure intentionally"):
        time.sleep(2)
        assert page.get_books_count() > 1000   # ❌ intentional fail
