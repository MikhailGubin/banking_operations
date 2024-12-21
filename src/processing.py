from src.widget import get_date


def filter_by_state(banking_transactions: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, в которых ключ state содержит переданное в функцию значение
    """
    transactions_in_bank = []
    for transaction in banking_transactions:
        if "state" in transaction and transaction["state"] == state:
            transactions_in_bank.append(transaction)

    if transactions_in_bank == []:
        raise ValueError("Отсутствуют словари с указанным статусом state в списке")

    return transactions_in_bank


def sort_by_date(banking_transactions: list, decreasing: bool = True) -> list:
    """
    Возвращает новый список, отсортированный по дате в зависимости от значения параметра increase
    """

    return sorted(banking_transactions, key=lambda transaction: get_date(transaction["date"]), reverse=decreasing)
