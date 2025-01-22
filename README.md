# Программа для работы с банковскими операциями

## Описание:
### Программа содержит функции:
- для маскировки номера карты или банковского счёта
- для сортировки банковских операций по их статусу
- для сортировки всех бнковских операций по дате их выполнения

---

## Содержание:
* ## <a id="title1">Описание</a>
* ## <a id="title1">Установка</a>
* ## <a id="title1">Использование</a>
* ## <a id="title1">Тестирование</a>
* ## <a id="title1">Команда проекта</a>
* ## <a id="title1">Источники</a>

---

## Установка:
1. #### Клонируйте репозиторий:
```commandline
python
git clone git@github.com:MikhailGubin/banking_operations.git
```

2. #### Установите зависимости:
```commandline
python
pip install -r requirements.txt
```

---

## Использование:
1. #### Функция get_mask_card_number 
##### Описание:
    Маскирует номер банковской карты.
    Добавлено логирование данной функции. 
##### Пример работы функции:
```commandline
python
7000792289606361  # входной аргумент
7000 79** **** 6361  # выход функции

#Пример логов в файле masks.log
2025-01-19 14:03:27,357 - src.masks - INFO - Начало работы функции get_mask_card_number
2025-01-19 14:03:27,358 - src.masks - INFO - Функция get_mask_card_number успешно завершила работу

2025-01-19 14:12:59,924 - src.masks - INFO - Начало работы функции get_mask_card_number
2025-01-19 14:12:59,924 - src.masks - ERROR - Неправильно введен номер карты
```

2. #### Функция get_mask_account 
##### Описание:
    Маскирует номер банковского счета.
    Добавлено логирование данной функции.
##### Пример работы функции:
```commandline
python
73654108430135874305 # входной аргумент
**4305 # выход функции

#Пример логов в файле masks.log
2025-01-19 14:03:27,358 - src.masks - INFO - Начало работы функции get_mask_account
2025-01-19 14:03:27,358 - src.masks - INFO - Функция get_mask_card_number успешно завершила работу

2025-01-19 14:12:59,924 - src.masks - INFO - Начало работы функции get_mask_account
2025-01-19 14:12:59,924 - src.masks - ERROR - Неправильно введен номер счёта
```

3. #### Функция mask_account_card 
##### Описание:
    Возвращает строку с замаскированным номером карты или счета.
##### Пример работы функции:

```commandline
python
Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```

4. #### Функция filter_by_state 
##### Описание:
    Возвращает новый список словарей, в которых ключ state
    содержит переданное в функцию значение
##### Пример работы функции:

```commandline
python
Пример входных данных для проверки функции

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},  
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Выход функции со статусом по умолчанию 'EXECUTED'

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},   
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

5. #### Функция sort_by_date 
##### Описание:
    Возвращает новый список, отсортированный по дате в
    зависимости от значения параметра increase
##### Пример работы функции:

```commandline
python
Пример входных данных для проверки функции

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},  
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Выход функции (сортировка по убыванию, т. е. сначала самые последние операции, 
по умолчанию)

[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},  
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

6. #### Функция filter_by_currency 
##### Описание:
    Принимает на вход список словарей, представляющих 
    транзакции, возвращает итератор, который поочередно 
    выдает транзакции с заданной валютой
##### Пример использования функции:

```commandline
python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
7. #### Функция transaction_descriptions   
##### Описание:
    принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди
##### Пример использования функции:

```commandline
python
descriptions = transaction_descriptions(transactions)
for index in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
8. #### Функция card_number_generator 
##### Описание:
    Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, 
    где X — цифра номера карты. Генератор может сгенерировать 
    номера карт в заданном диапазоне от 0000 0000 0000 0001 до 
    9999 9999 9999 9999. Генератор должен принимать начальное и 
    конечное значения для генерации диапазона номеров. 
##### Пример использования функции:

```commandline
python
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
9. #### Декоратор log 
##### Описание:
    автоматически логирует начало и конец выполнения функции, а 
    также ее результаты или возникшие ошибки. Декоратор принимает
    необязательный аргумент filename, который определяет, куда 
    будут записываться логи (в файл или в консоль).
    Логирование должно включает:
    - Имя функции и результат выполнения при успешной операции.
    - Имя функции, тип возникшей ошибки и входные параметры, если
      выполнение функции привело к ошибке. 
##### Пример использования функции:

```commandline
python
@log(filename="function_log")
def summ_two_numbers(x: int | float, y: int | float) -> int | float:
    """
    Складывает два числа
    """
    return x + y
    
summ_two_numbers(1, 2)
summ_two_numbers(1, "2")

#Пример логов в файле function_log.txt

summ_two_numbers ok, result: 3
start - 2025-01-02 14:32:36.649767; stop - 2025-01-02 14:32:36.649771

summ_two_numbers error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}
start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00
```
10. #### Функция read_json_file
##### Описание:
    принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список. Функция 
    находится в модуле utils. Файл с данными о финансовых транзациях 
    operations.json расположен в директории data/ в корне проекта.
    Добавлено логирование данной функции.
##### Пример использования функции:
```commandline
python
print(read_json_file(PATH_TO_FILE))

#Вывод в консоли:
[
{'id': 441945886, 'state': 'EXECUTED', 
'date': '2019-08-26T10:50:58.294041',
 'operationAmount': {'amount': '31957.58', 
 'currency': {'name': 'руб.', 'code': 'RUB'}}, 
 'description': 'Перевод организации', 
 'from': 'Maestro 1596837868705199', 
 'to': 'Счет 64686473678894779589'}, 
 ...
 ]
 
#Пример логов в файле masks.log

2025-01-19 13:51:14,583 - src.utils - INFO - Начало работы функции read_json_file
2025-01-19 13:51:14,584 - src.utils - INFO - Функции read_json_file успешно завершила работу

2025-01-19 14:16:19,590 - src.utils - INFO - Начало работы функции read_json_file
2025-01-19 14:16:19,590 - src.utils - ERROR - JSON-файл не найден
```
11. #### Функция get_amount_of_transaction
##### Описание:
    принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях, тип данных — float. Если транзакция была в USD или EUR, 
    происходит обращение к внешнему API для получения текущего курса валют 
    и конвертации суммы операции в рубли. Для конвертации валюты 
    используется Exchange Rates Data API: 
    https://apilayer.com/exchangerates_data-api. 
    Функцию конвертации расположена в модуле external_api.
##### Пример использования функции:
```commandline
python
bank_operations = read_json_file(PATH_TO_FILE)
print(get_amount_of_transaction(bank_operations[1]))

#Вывод в консоли:
    842698.53

#Данные, полученные из API:
    {            
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 8221.37},          
    "info": {"timestamp": 1737148204, "rate": 102.500986},
    "date": "2025-01-17",
     "result": 842698.531271,
    }
```
12. ### Функция read_csv_file
##### Описание:
    Считывает финансовые операции из CSV-файла.
    Принимает путь к файлу CSV в качестве аргумента,
    выдает список словарей с транзакциями.
    Реализована функция для считывания финансовых операций из Excel.   
    Функция расположена в модуле csv_and_excel_readers.py
##### Пример использования функции:
```commandline
#Пример вызова функции:

pprint.pprint(read_csv_file(PATH_TO_CSV_FILE), width=85, indent=4)

#Пример входных данных:

id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;
Счет 39745660563456619397;Перевод организации

3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;
Discover 0720428384694643;Перевод с карты на карту

...

#Пример выходных данных:
[
    {   'amount': 16210.0,
        'currency_code': 'PEN',
        'currency_name': 'Sol',
        'date': '2023-09-05T11:30:32Z',
        'description': 'Перевод организации',
        'from': 'Счет 58803664561298323391',
        'id': 650703.0,
        'state': 'EXECUTED',
        'to': 'Счет 39745660563456619397'},
    {   'amount': 29740.0,
        'currency_code': 'COP',
        'currency_name': 'Peso',
        'date': '2020-12-06T23:00:58Z',
        'description': 'Перевод с карты на карту',
        'from': 'Discover 3172601889670065',
        'id': 3598919.0,
        'state': 'EXECUTED',
        'to': 'Discover 0720428384694643'},
        ...
]        
        
```

13. ### Функция read_excel_file
##### Описание:
    Считывает финансовые операции из Excel-файла.
    Принимает путь к файлу Excel в качестве аргумента,
    выдает список словарей с транзакциями.    
    Функция расположена в модуле csv_and_excel_readers.py
##### Пример использования функции:
```commandline
#Пример вызова функции:

pprint.pprint(read_excel_file(PATH_TO_EXCEL_FILE), width=85, indent=4)

#Пример входных данных:

|   id	|   state	|   date 	|   ...	|    description	|
|---	|---	|---	|---	|---	|
|650703|EXECUTED|2023-09-05T11:30:32Z;16210 	|  ... 	| 	|Перевод организации
|3598919|EXECUTED|2020-12-06T23:00:58Z;29740 	|  ...	|	Перевод с карты на карту|

...

#Пример выходных данных:
[
{'amount': 16210.0,
        'currency_code': 'PEN',
        'currency_name': 'Sol',
        'date': '2023-09-05T11:30:32Z',
        'description': 'Перевод организации',
        'from': 'Счет 58803664561298323391',
        'id': 650703.0,
        'state': 'EXECUTED',
        'to': 'Счет 39745660563456619397'},
    {   'amount': 29740.0,
        'currency_code': 'COP',
        'currency_name': 'Peso',
        'date': '2020-12-06T23:00:58Z',
        'description': 'Перевод с карты на карту',
        'from': 'Discover 3172601889670065',
        'id': 3598919.0,
        'state': 'EXECUTED',
        'to': 'Discover 0720428384694643'},
        ...
]
```
---

## Тестирование:
Код данного проекта покрыт тестами фреймворка pytest более чем на 80 %. 

Для запуска тестов выполните команду:

'''
python
pytest
'''

Чтобы установить pytest через Poetry, используйте команду:

'''
python
poetry add --group dev pytest
'''

Модули с тестами хранятся в директории tests\. 

---

## Команда проекта:
* Губин Михаил — Back-End Engineer

---

## Источники:
* курс лекций и учебных материалов учебного центра "SkyPro"
