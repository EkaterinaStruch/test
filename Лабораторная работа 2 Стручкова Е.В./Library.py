BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: ID книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("ID книги должен быть типом данных int")
        if id_ <= 0:
            raise ValueError("ID книги должен быть положительным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типом данных str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц книги должно быть типом данных int")
        if pages <= 0:
            raise ValueError("Количество страниц книги должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books=[]):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Книги, имеющиеся в библиотеке
        """
        if not isinstance(books, list):
            raise TypeError("Список книг должен иметь тип данных list")
        self.books = books

    def get_next_book_id(self) -> int:
        if self.books == []:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, i: int):
        for i, book in enumerate(self.books):
            if book.id_ == i:
                return i
        return ValueError("Книги с запрашиваемым ID не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
