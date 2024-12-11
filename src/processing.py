def filter_by_state(operations_info: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, в которых ключ state содержит переданное в функцию значение
    """
    return [operation for operation in operations_info if operation["state"] == state]


def sort_by_date(operations_info: list, increase: bool = True) -> list:
    """
    Возвращает новый список, отсортированный по дате в зависимости от значения параметра increase
    """
    return sorted(operations_info, key=lambda operation: operation["date"], reverse=not increase)
