cards = {
    "Тип автомаобиля":"Легковой",
    "Заводской №":"1423-5663-3152",
    "Марка автомобиля":"Reno",
    "Модель автомобиля":"Logan",
    "Дата регистрации":[12,5,2015],
    
    "Фамилия":"Иванов",
    "Имя":"Иван",
    "Отчество":"Иванович",
    "Телефон":"8945361031",
    "Почтовый адрес":"Россия, г.Пермь, Краснова - 9, 45",
    
    "Техобслуживания":[{
        "Пробег":29000,
        "Дата прохождения":[20,10,2016],
        "Наличие дефектов":False,
        "Описание дефектов":"",
        "Стоимость ремонта":0
    },]
}

#Создание сервисной книжки авто
def CreateBook(auto_type, number, mark, model, date_register, family, name, surname, phone, address, service):
    return {
        "Тип автомаобиля":auto_type,
        "Заводской №":number,
        "Марка автомобиля":mark,
        "Модель автомобиля":model,
        "Дата регистрации":date_register,#"12.05.2015"

        "Фамилия":family,
        "Имя":name,
        "Отчество":surname,
        "Телефон":phone,
        "Почтовый адрес":address,

        "Техобслуживания":service  
    }

#Добавление записи об техосмотре
def AddService(mileage, date, is_defect, description, price):
    return {
        "Пробег":mileage,
        "Дата прохождения":date,#"20.10.2016"
        "Наличие дефектов":is_defect,
        "Описание дефектов":description,
        "Стоимость ремонта":price
    }

#Вывод истории техосмотров
def PrintHistorySer(book):    
    for elem in book:
        for key, val in elem.items():
            print(key, " - ", val)
        print()

#Вывод книжки более качественно
def BeautPrint(book):
    for key, elem in book.items():
        if key == "Техобслуживания":
            print("История техобслуживания в книге " + book["Марка автомобиля"] + " " + book["Модель автомобиля"] + " " + book["Заводской №"] + ":")
            PrintHistorySer(elem)
        else:
            print(key, " - ", elem)

newBook = CreateBook("Легковой",
    "5550-1235-6611",
    "Audi", 
    "r8", 
    [12,4,2016],
    "Романов",
    "Роман",
    "Романович",
    "84452198335",
    "Россия, г.Масква, Ленина - 9, кв. 44",
    [])

newBook["Техобслуживания"].append(AddService(10500,[22,10,2017], True, "Поврежден капот", 15000))
newBook["Техобслуживания"].append(AddService(28500,[5,4,2019], True, "Замена колес", 20000))

BeautPrint(newBook)

"""
Тип автомаобиля  -  Легковой
Заводской №  -  5550-1235-6611
Марка автомобиля  -  Audi
Модель автомобиля  -  r8
Дата регистрации  -  [12, 4, 2016]
Фамилия  -  Романов
Имя  -  Роман
Отчество  -  Романович
Телефон  -  84452198335
Почтовый адрес  -  Россия, г.Масква, Ленина - 9, кв. 44
История техобслуживания в книге Audi r8 5550-1235-6611:
Пробег  -  10500
Дата прохождения  -  [22, 10, 2017]
Наличие дефектов  -  True
Описание дефектов  -  Поврежден капот
Стоимость ремонта  -  15000

Пробег  -  28500
Дата прохождения  -  [5, 4, 2019]
Наличие дефектов  -  True
Описание дефектов  -  Замена колес
Стоимость ремонта  -  20000
"""

"""
        Данные авбомобиля
Тип
Заводской №
Марка автомобиля
Модель автомобиля
Дата регистрации

        Данные владельца
Фамилия
Имя
Отчество
Телефон
Почтовый адрес

        Карточка Технического обслуживания
Пробег (км)
Дата прохождения
Наличие дефектов (bool)
Описание дефектов 
Стоимость ремонта

"""