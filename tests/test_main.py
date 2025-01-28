import unittest
from io import StringIO
from unittest.mock import patch

from main import main_functions, get_final_results, main_interface


def test_main_functions_jsn_executed() -> None:
    """
    Проверяет работу функции main_functions, когда выбраны следующие параметры:
    данные читаются из JSON-файла,
    фильтрация выбрана по статусу 'executed',
    остальные фильтры не выбраны.
    Результат сравнивается по двум последним банковским операциям из списка
    """
    args_for_main_functions = {
        'choose_data_format': '1',
        'choose_transactions_state': 'executed',
        'filter_for_date': 'нет',
        'filter_for_currency': 'нет',
        'filter_for_word': 'нет',
        'flag_decrease_bool': True,
        'word_for_searching': ''
    }
    transactions_list = main_functions(args_for_main_functions)
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


def test_main_functions_csv_canceled_filter_data() -> None:
    """
    Проверяет работу функции main_functions, когда выбраны следующие параметры:
    данные читаются из CSV-файла,
    фильтрация выбрана по статусу 'canceled',
    выбрана фильтрация по дате по убыванию,
    остальные фильтры не выбраны.
    Результат сравнивается по трём последним банковским операциям из списка
    """
    args_for_main_functions = {
        'choose_data_format': '2',
        'choose_transactions_state': 'executed',
        'filter_for_date': 'да',
        'filter_for_currency': 'нет',
        'filter_for_word': 'нет',
        'flag_decrease_bool': True,
        'word_for_searching': ''
    }
    transactions_list = main_functions(args_for_main_functions)
    assert transactions_list[-3: ]  == [
        {'amount': 24045.0,
         'currency_code': 'EUR',
         'currency_name': 'Euro',
         'date': '2021-01-01T05:06:24Z',
         'description': 'Перевод с карты на карту',
         'from': 'American Express 3974807204664022',
         'id': 1779770.0,
         'state': 'EXECUTED',
         'to': 'Visa 7286072015230056'},
        {'amount': 12764.0,
         'currency_code': 'AZN',
         'currency_name': 'Manat',
         'date': '2020-01-01T05:03:33Z',
         'description': 'Перевод с карты на карту',
         'from': 'American Express 2957863070974974',
         'id': 3682775.0,
         'state': 'EXECUTED',
         'to': 'American Express 6990780344978331'},
        {'amount': 34119.0,
         'currency_code': 'CNY',
         'currency_name': 'Yuan Renminbi',
         'date': '2020-01-01T14:34:00Z',
         'description': 'Перевод организации',
         'from': 'Visa 4485542637612146',
         'id': 4124955.0,
         'state': 'EXECUTED',
         'to': 'Счет 28542261928514137912'}
    ]


def test_main_functions_xlsx_pending_filter_data_currency() -> None:
    """
    Проверяет работу функции main_functions, когда выбраны следующие параметры:
    данные читаются из XLSX-файла,
    фильтрация выбрана по статусу 'pending',
    выбрана фильтрация по дате по возрастанию,
    выводится должны только рублевые операции,
    остальные фильтрации не выбраны.
    Результат сравнивается по трём последним банковским операциям из списка
    """
    args_for_main_functions = {
        'choose_data_format': '3',
        'choose_transactions_state': 'pending',
        'filter_for_date': 'да',
        'filter_for_currency': 'да',
        'filter_for_word': 'нет',
        'flag_decrease_bool': False,
        'word_for_searching': ''
    }
    transactions_list = main_functions(args_for_main_functions)
    assert transactions_list[-3: ]  == [
   {'amount': 31503.0,
  'currency_code': 'RUB',
  'currency_name': 'Ruble',
  'date': '2020-10-05T10:31:57Z',
  'description': 'Открытие вклада',
  'from': None,
  'id': 1358349.0,
  'state': 'PENDING',
  'to': 'Счет 69086868315648596195'},
 {'amount': 31503.0,
  'currency_code': 'RUB',
  'currency_name': 'Ruble',
  'date': '2020-10-05T10:31:57Z',
  'description': 'Открытие вклада',
  'from': None,
  'id': 1358349.0,
  'state': 'PENDING',
  'to': 'Счет 69086868315648596195'},
 {'amount': 31503.0,
  'currency_code': 'RUB',
  'currency_name': 'Ruble',
  'date': '2020-10-05T10:31:57Z',
  'description': 'Открытие вклада',
  'from': None,
  'id': 1358349.0,
  'state': 'PENDING',
  'to': 'Счет 69086868315648596195'}
    ]


def test_main_functions_csv_canceled_filter_data_currency_by_word() -> None:
    """
    Проверяет работу функции main_functions, когда выбраны следующие параметры:
    данные читаются из CSV-файла,
    фильтрация выбрана по статусу 'canceled',
    выбрана фильтрация по дате по возрастанию,
    выводится должны только рублевые операции,
    список транзакций отфильтровывается по слову "открытие".
    Результат сравнивается по трём последним банковским операциям из списка
    """
    args_for_main_functions = {
        'choose_data_format': '2',
        'choose_transactions_state': 'canceled',
        'filter_for_date': 'да',
        'filter_for_currency': 'да',
        'filter_for_word': 'да',
        'flag_decrease_bool': True,
        'word_for_searching': 'открытие'
    }
    transactions_list = main_functions(args_for_main_functions)
    assert transactions_list[-3: ]  == [
        {'amount': 14438.0,
         'currency_code': 'RUB',
         'currency_name': 'Ruble',
         'date': '2020-08-31T00:52:19Z',
         'description': 'Открытие вклада',
         'from': None,
         'id': 4809278.0,
         'state': 'CANCELED',
         'to': 'Счет 75647434231761535859'},
        {'amount': 14438.0,
         'currency_code': 'RUB',
         'currency_name': 'Ruble',
         'date': '2020-08-31T00:52:19Z',
         'description': 'Открытие вклада',
         'from': None,
         'id': 4809278.0,
         'state': 'CANCELED',
         'to': 'Счет 75647434231761535859'},
        {'amount': 14438.0,
         'currency_code': 'RUB',
         'currency_name': 'Ruble',
         'date': '2020-08-31T00:52:19Z',
         'description': 'Открытие вклада',
         'from': None,
         'id': 4809278.0,
         'state': 'CANCELED',
         'to': 'Счет 75647434231761535859'}
    ]


def test_main_functions_no_required_operations() -> None:
    """
    Проверяет работу функции main_functions, когда выбраны отсутствуют транзакции,
    удовлетворяющие заданным условиям.
    Установлены следующие параметры:
    данные читаются из JSON-файла,
    фильтрация выбрана по статусу 'executed',
    выбрана фильтрация по дате по убыванию,
    выводится должны только рублевые операции,
    список транзакций отфильтровывается по слову "карты".
    """
    args_for_main_functions = {
        'choose_data_format': '2',
        'choose_transactions_state': 'pending',
        'filter_for_date': 'да',
        'filter_for_currency': 'да',
        'filter_for_word': 'да',
        'flag_decrease_bool': False,
        'word_for_searching': 'карты'
    }
    transactions_list = main_functions(args_for_main_functions)
    assert transactions_list[-3: ]  == [{}]


@patch('builtins.input', side_effect=['1', 'EXECUTED', 'да', 'по возрастанию', 'да', 'да',
                                      'Перевод'])
def test_main_interface(mock_input) -> None:
    """ Проверяет работу функции main_interface """

    assert main_interface() == {
        'choose_data_format': '1',
        'choose_transactions_state': 'EXECUTED',
        'filter_for_date': 'да',
        'filter_for_currency': 'да',
        'filter_for_word': 'да',
        'flag_decrease_bool': False,
        'word_for_searching': 'Перевод'}


@patch('builtins.input', side_effect=['2', 'CANCELED', '', '', '', '',
                                      '42'])
def test_main_interface_no_filters(mock_input) -> None:
    """
    Проверяет работу функции main_interface,
    если все проверки не выбраны
    """

    assert main_interface() == {
        'choose_data_format': '2',
        'choose_transactions_state': 'CANCELED',
        'filter_for_date': '',
        'filter_for_currency': '',
        'filter_for_word': '',
        'flag_decrease_bool': True,
        'word_for_searching': ''}


@patch('builtins.input', side_effect=['0', '5', '1', 'CAN', '3', 'executed',
                                      '', '', '', '', '23'])
def test_main_interface_test_while_true(mock_input) -> None:
    """
    Проверяет работу функции main_interface,
    если все проверки не выбраны, а на первые
    два вопроса дан нужный ответ только с третьего раза

    """

    assert main_interface() == {
        'choose_data_format': '1',
        'choose_transactions_state': 'EXECUTED',
        'filter_for_date': '',
        'filter_for_currency': '',
        'filter_for_word': '',
        'flag_decrease_bool': True,
        'word_for_searching': ''}


class TestMainFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_final_results(self, transactions_for_generate: list, mock_stdout=None) -> None:
        """ Проверяет работу функции get_final_results"""
        # transactions_for_generate - фикстура из модуля conftest.py
        transactions = transactions_for_generate[-2:]
        get_final_results(transactions)
        self.assertIn("Распечатываю итоговый список транзакций...\n"
                      "Всего банковских операций в выборке: 2", mock_stdout.getvalue())


class TestMainFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_final_results(self, mock_stdout) -> None:
        """ Проверяет работу функции get_final_results"""
        # transactions_for_generate - фикстура из модуля conftest.py
        transactions_list = [{}]
        get_final_results(transactions_list)
        self.assertIn("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
                      mock_stdout.getvalue())
