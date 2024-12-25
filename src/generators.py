def filter_by_currency(transactions_list: list, currency: str = "USD") -> dict| str:
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











def transaction_descriptions(transactions_dict: list) -> list:
    pass

def card_number_generator(start: int, stop: int) -> str:
    pass
