import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["Harry Potter", "Lord of the Rings", "Sherlock Holmes"])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [("Harry Potter", "Фантастика"), ("Sherlock Holmes", "Детективы")])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book7")
        collector.set_book_genre("Book7", "Фантастика")
        assert collector.get_book_genre("Book7") == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book3")
        collector.set_book_genre("Book3", "Ужасы")
        assert collector.get_books_with_specific_genre("Ужасы") == ["Book3"]

    def test_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Book4")
        collector.set_book_genre("Book4", "Комедии")
        assert collector.get_books_for_children() == ["Book4"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book5")
        collector.add_book_in_favorites("Book5")
        assert "Book5" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book6")
        collector.add_book_in_favorites("Book6")
        collector.delete_book_from_favorites("Book6")
        assert "Book6" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

