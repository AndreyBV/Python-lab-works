from datetime import date
import functionsBook as fBook

# Данные для создания книги
dataOwner = {"auto" : {
        "Модель": "Lada Vesta",
        "Год выпуска": "2015",
        "Регистрационный номер": "е215ва159",
        "Заводской №": "109186",
        "Объем двигателя, л": "1.8",
        "Начальный пробег автоб, км": "158"
    }, "owner" : {
    "ФИО": ["Иванов", "Иван", "Иванович"],
    "Адрес": ["Россия", "Пермский край", "г.Пермь", "ул.Попова", 20, 15],
    "Телефон": "89026316888",
    "E-mail": "email@email.ru"
    }
}

# Вызов метода по созданию сервисной книги
book = fBook.сreate_book(**dataOwner)

# Вывод данных сервисной книги
pprint(book)

