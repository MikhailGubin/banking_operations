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
'''
python
git clone git@github.com:MikhailGubin/banking_operations.git
'''

2. #### Установите зависимости:
'''
python
pip install -r requirements.txt
'''

---

## Использование:
1. #### Функция get_mask_card_number маскирует номер банковской карты
##### Пример работы функции:
7000792289606361  # входной аргумент
7000 79** **** 6361  # выход функции

2. #### Функция get_mask_account маскирует номер банковского счета
##### Пример работы функции:
73654108430135874305 # входной аргумент
**4305 # выход функции

3. #### Функция mask_account_card возвращает строку с замаскированным номером карты и счета
##### Пример работы функции:
Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции

4. #### Функция filter_by_state возвращает новый список словарей, в которых ключ state
содержит переданное в функцию значение
##### Пример работы функции:
Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

5. #### Функция sort_by_date возвращает новый список, отсортированный по дате в
зависимости от значения параметра increase
##### Пример работы функции:
Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции, по умолчанию)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

---

## Тестирование:
Код данного проекта покрыт тестами фреймворка pytest более чем на 90 %. 

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
