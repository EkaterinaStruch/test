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
        :param pages: Количество страниц книги
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
