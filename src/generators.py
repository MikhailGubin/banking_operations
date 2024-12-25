from src.masks import get_mask_card_number


def filter_by_currency(transactions_list: list, currency: str = "USD") -> dict|str:
    """"
    Принимает на вход список словарей, представляющих транзакции,
    возвращает итератор, который поочередно выдает транзакции
    с заданной валютой SupportsNext[_T]
    """
    amount_transactions = 0

    if not transactions_list:
        yield "Пустой список транзакций"

    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            amount_transactions += 1
            yield transaction

    if amount_transactions == 0:
        yield "Транзакции в заданной валюте отсутствуют"

    while True:
        yield "Генератор закончил работу"


def transaction_descriptions(transactions_dict: list) -> str:
    """"
    Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди
    """
    if not transactions_dict:
        yield "Пустой список транзакций"
    for transaction in transactions_dict:
        yield transaction["description"]
    while True:
        yield "Генератор закончил работу"



def card_number_generator(start: int, stop: int) -> str:
    """
    Выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где
    X — цифра номера карты
    """
    if start > stop:
        start, stop = stop, start
    elif start == stop:
        yield "Начало и конец диапазона совпадают"
    if start < 1:
        yield "Диапазон чисел меньше 0"
    elif stop > 9999999999999999:
        yield "Диапазон чисел вышел верхнюю границу"
    else:
        for number in range(start, stop+1):
            card_number = "0"*(16 - len(str(number))) + str(number)
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[-4:]}"
    while True:
        yield "Генератор закончил работу"
