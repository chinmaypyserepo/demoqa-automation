import pytest
from ui.pages.bookstore_page import BookStorePage
from config.settings import UI_BASE_URL

@pytest.mark.ui
def test_search_book_after_login(login_browser):
    page = BookStorePage(login_browser)
    page.open_books_page(f"{UI_BASE_URL}/books")
    page.search("Git")
    assert page.book_count() > 0
