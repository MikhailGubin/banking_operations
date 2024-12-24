def filter_by_currency(transactions_list: list, currency: str = "USD") -> dict:
    amount_transactions = 0
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction
    if amount_transactions == 0:
        raise ValueError("Транзакции в заданной валюте отсутствуют")




def transaction_descriptions(transactions_dict: list) -> list:
    pass

def card_number_generator(start: int, stop: int) -> str:
    pass
