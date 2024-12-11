def filter_by_state(operations_info: list, state: str = "EXECUTED") -> list:
    """ "
    Возвращает новый список словарей, в которых ключ state
    содержит переданное в функцию значение
    """
    list_of_operations = []
    for operation in operations_info:
        if operation["state"] == state:
            list_of_operations.append(operation)
    return list_of_operations
