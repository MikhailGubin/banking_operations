import pprint

from main import main


def test_main_only_executed() -> None:
    """ Проверяет работу всей программы в сборе"""
    args_for_main = {
        'choose_data_format': '1',
        'choose_transactions_state': 'executed',
        'filter_for_date': 'нет',
        'filter_for_currency': 'нет',
        'filter_for_word': 'нет',
        'flag_decrease_bool': True,
        'word_for_searching': ''
    }
    transactions_list = main(args_for_main)
    assert transactions_list[-2: ]  == [
        {   'date': '2019-01-05T00:52:30.108534',
        'description': 'Перевод со счета на счет',
        'from': 'Счет 46363668439560358409',
        'id': 957763565,
        'operationAmount': {   'amount': '87941.37',
                               'currency': {'code': 'RUB', 'name': 'руб.'}},
        'state': 'EXECUTED',
        'to': 'Счет 18889008294666828266'},
    {   'date': '2019-07-13T18:51:29.313309',
        'description': 'Перевод с карты на счет',
        'from': 'Maestro 1308795367077170',
        'id': 667307132,
        'operationAmount': {   'amount': '97853.86',
                               'currency': {'code': 'RUB', 'name': 'руб.'}},
        'state': 'EXECUTED',
        'to': 'Счет 96527012349577388612'}
    ]


def test_main() -> None:
    """ Проверяет работу всей программы в сборе"""
    args_for_main = {
        'choose_data_format': '2',
        'choose_transactions_state': 'canceled',
        'filter_for_date': 'да',
        'filter_for_currency': 'нет',
        'filter_for_word': 'нет',
        'flag_decrease_bool': True,
        'word_for_searching': ''
    }
    transactions_list = main(args_for_main)
    pprint.pprint(transactions_list, width=85, indent=4)
    assert transactions_list[-4: ]  == [
        {   'date': '2019-01-05T00:52:30.108534',
        'description': 'Перевод со счета на счет',
        'from': 'Счет 46363668439560358409',
        'id': 957763565,
        'operationAmount': {   'amount': '87941.37',
                               'currency': {'code': 'RUB', 'name': 'руб.'}},
        'state': 'EXECUTED',
        'to': 'Счет 18889008294666828266'},
    {   'date': '2019-07-13T18:51:29.313309',
        'description': 'Перевод с карты на счет',
        'from': 'Maestro 1308795367077170',
        'id': 667307132,
        'operationAmount': {   'amount': '97853.86',
                               'currency': {'code': 'RUB', 'name': 'руб.'}},
        'state': 'EXECUTED',
        'to': 'Счет 96527012349577388612'}
    ]