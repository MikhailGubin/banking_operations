def filter_by_state(banking_transactions: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, в которых ключ state содержит переданное в функцию значение
    """
    return [transaction for transaction in banking_transactions if transaction["state"] == state]


def sort_by_date(banking_transactions: list, decreasing: bool = True) -> list:
    """
    Возвращает новый список, отсортированный по дате в зависимости от значения параметра increase
    """
    return sorted(banking_transactions, key=lambda transaction: transaction["date"], reverse=decreasing)
