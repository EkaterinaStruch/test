import doctest

class Computer:
    def __init__(self, memory_size: int, occupied_memory: int):
        """
        Создание и подготвка к работе объекта "Компьютер"
        :param memory_size: Объём памяти
        :param occupied_memory: Объём занятой памяти
        Примеры:
        >>> computer = Computer(512, 0)
        """
        if not isinstance(memory_size, int):
            raise TypeError("Объём памяти компьютера должен быть типа int")
        if memory_size <= 0:
            raise ValueError("Объём памяти компьютера должен быть положительным числом и больше нуля")
        self.memory_size = memory_size

        if not isinstance(occupied_memory, int):
            raise TypeError("Объём занятой памяти компьютера должен быть типа int")
        if occupied_memory < 0:
            raise ValueError("Объём занятой памяти компьютера не может быть отрицательным числом")
        if occupied_memory > memory_size:
            raise ValueError("Объём занятой памяти компьютера не должен быть больше общего объёма памяти компьютера")
        self.occupied_memory = occupied_memory

    def is_empty_space(self) -> int:
        """
        Функция вычисления свободной памяти.
        :return: Объём свободной памяти
        >>> computer = Computer(512, 200)
        >>> computer.is_empty_space()
        312
        """
        return self.memory_size - self.occupied_memory

    def filling_memory_on_computer(self, memory: int) -> None:
        """
        Скачивание объекта на компьютер.
        :param memory: Количество заполняемого объёма памяти
        :raise ValueError: Если количество необходимого к заполнению объёма памяти превышает свободное место на компьютере, то вызываем ошибку
        Примеры:
        >>> computer = Computer(512, 0)
        >>> computer.filling_memory_on_computer(100)
        """
        if not isinstance(memory, int):
            raise TypeError("Количество заполняемой памяти должно быть типа int ")
        if memory < 0:
            raise ValueError("Количество заполняемой памяти должно быть положительным числом")
        ...


class CupofCoffee:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготвка к работе объекта "Кружка для кофе"
        :param capacity_volume: Объём кружки
        :param occupied_volume: Объём кофе
        Примеры:
        >>> cup_of_coffee = CupofCoffee(400, 0)
        """
        if not isinstance(capacity_volume, int):
            raise TypeError("Объём кружки должен быть типа int")
        if capacity_volume <= 0:
            raise ValueError("Объём кружки должен быть положительным числом и больше нуля")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, int):
            raise TypeError("Объём кофе должен быть типа int")
        if occupied_volume < 0:
            raise ValueError("Объём кофе не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Объём кофе не должен быть больше объёма кружки")
        self.occupied_volume = occupied_volume

    def coffee_pouring(self, coffee: int) -> None:
        """
        Функция наливания кофе в кружку.
        :param coffee: Объём кофе, наливаемого в кружку
        :raise ValueError: Если количество наливаемого кофе превышает количество свободного объёма в кружке, то возвращается ошибка.
        >>> cup_of_coffee = CupofCoffee(400, 0)
        >>> cup_of_coffee.coffee_pouring(200)
        """
        if not isinstance(coffee, int):
            raise TypeError("Объём кофе, наливаемого в кружку, должен быть типа int")
        if coffee < 0:
            raise ValueError("Объём кофе, наливаемого в кружку, должен быть положительным числом")

    def coffee_price(self, volume: int) -> int:
        """
        Функция по выводу стоимости кружки кофе.
        :param volume: Объём кружки с кофе
        >>> cup_of_coffee = CupofCoffee(400, 0)
        >>> cup_of_coffee.coffee_price(400)
        """
        if not isinstance(volume, int):
            raise TypeError("Объём кружки с кофе должен быть типа int ")
        if volume < 0:
            raise ValueError("Объём кружки с кофе должен быть положительным числом")
        ...


class Square:
    def __init__(self, side: int):
        """
        Создание и подготовка к работе объекта "Квадрат"
        :param side: Сторона квадрата
        Примеры:
        >>> square = Square(3)
        """
        if not isinstance(side, int):
            raise TypeError("Сторона квадрата должна быть типа int")
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом и больше нуля")
        self.side = side

    def calculating_area(self) -> int:
        """
        Функция вычисления площади квадрата.
        :return: Площадь квадрата
        >>> square = Square(3)
        >>> square.calculating_area()
        9
        """
        return self.side ** 2

    def calculating_perimeter(self) -> int:
        """
        Функция вычисления периметра квадрата.
        :return: Периметр квадрата
        >>> square = Square(3)
        >>> square.calculating_perimeter()
        12
        """
        return self.side * 4

if __name__ == "__main__":
    doctest.testmod()
