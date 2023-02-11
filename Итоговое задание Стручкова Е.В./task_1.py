import doctest

class Factory:
    """ Базовый класс "Завод" """

    def __init__(self, name: str, number_of_workers: int, number_of_equipment: int):
        """
        Подготовка объекта "Завод"
        :param name: Наименование завода
        :param number_of_workers: Количество работников
        :param number_of_equipment : Количество станков
        Пример:
        >>> steel_factory = Factory("Завод по переработке стали", 200, 50)
        """

        if not isinstance(name, str):
            raise TypeError ("Наименование завода должно быть типа str")
        self.name = name

        if not isinstance(number_of_workers, int):
            raise TypeError("Количество работников должно быть типа int")
        if number_of_workers < 0:
            raise ValueError("Количество работников должно быть положительным числом")
        self.number_of_workers = number_of_workers

        if not isinstance(number_of_equipment, int):
            raise TypeError("Количество станков должно быть типа int")
        if number_of_equipment < 0:
            raise ValueError("Количество станков должно быть положительным числом")
        self.number_of_equipment = number_of_equipment

    def __str__(self) -> str:
        return f"Завод: {self.name}, Количество работников: {self.number_of_workers}, Количество станков: {self.number_of_equipment}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, number_of_workers={self.number_of_workers!r}, number_of_equipment={self.number_of_equipment!r})"

    def week_working_hours(self, hours: int) -> int:
        """
        Определение количества рабочих часов в неделю
        :param hours: Количество рабочих часов в неделю по ТК РФ для одного работника
        :return: Количество рабочих часов в неделю
        Примеры:
        >>> steel_factory = Factory("Завод по переработке стали", 200, 50)
        >>> steel_factory.week_working_hours(40)
        8000
        """
        if not isinstance(hours, int):
            raise TypeError("Количество рабочих часов должно быть типа int")
        if hours < 0:
            raise ValueError("Количество рабочих часов должно быть положительным числом")
        return hours * self.number_of_workers

    def salary(self, wage_rate: int, month_hours: int) -> int:
        """
        Определение размера выплат работникам за месяц
        :param wage_rate: Cтавка в час для одного работника
        :param month_hours: Количество рабочих часов в месяц для одного работника
        :return: Общая сумма выплат работникам за месяц
        Примеры:
        >>> steel_factory = Factory("Завод по переработке стали", 200, 50)
        >>> steel_factory.salary(500, 160)
        16000000
        """
        if not isinstance(wage_rate, int):
            raise TypeError("Ставка в час должна быть типа int")
        if wage_rate < 0:
            raise ValueError("Ставка в час должна быть положительным числом")
        if not isinstance(month_hours, int):
            raise TypeError("Количество рабочих часов в месяц должно быть типа int")
        if month_hours < 0:
            raise ValueError("Количество рабочих часов в месяц должно быть положительным числом")
        return wage_rate * month_hours * self.number_of_workers


class WoodFactory(Factory):
    """Дочерний класс "Завод по переработке древесины" """

    def __init__(self, name: str, number_of_workers: int, number_of_equipment: int, type: str):
        """
        :param name: Название завода
        :param number_of_workers: Количество работников
        :param number_of_equipment: Количество оборудования
        :param type: Тип обрабатываемой древесины
        Примеры:
        >>> oak_factory = WoodFactory("Завод по переработке дуба", 100, 40, "Дуб")
        """
        super().__init__(name, number_of_workers, number_of_equipment)

        if not isinstance(type, str):
            raise TypeError("Тип обрабатываемой древесины должен быть типа str")
        self.type = type

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, number_of_workers={self.number_of_workers!r}, " \
                   f"number_of_equipment={self.number_of_equipment!r}, type={self.type!r})"

    def producing_volume(self, volume: int) -> int:
        """
        Определение объема выпускаемой продукции
        :param volume: Объём выпускаемой продукции с одного станка
        :return: Объём выпускаемой продукции с завода
        Примеры:
        >>> oak_factory = Wood_Factory("Завод по переработке дуба", 100, 40, "Дуб")
        >>> oak_factory.producing_volume(60)
        2400
        """
        return volume * self.number_of_equipment

if __name__ == "__main__":
    doctest.testmod()
    pass
