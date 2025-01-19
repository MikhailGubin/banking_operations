import pprint

from data.data_for_main import bank_card_or_account_number, banking_operations_info, transactions_for_generate
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import PATH_TO_FILE, read_json_file
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    # Visa Platinum 8990922113665229 - пример банковской карты
    print(get_mask_card_number(8990922113665229))
    # Счет 11776614605963066702 - пример банковского счета
    print(get_mask_account(11776614605963066702))
    pprint.pprint(read_json_file(PATH_TO_FILE), width=85, indent=4)

    print(mask_account_card(bank_card_or_account_number))
    print(get_date("2019-07-03T18:35:29.512364"))
    pprint.pprint(filter_by_state(banking_operations_info), width=85, indent=4)
    pprint.pprint(sort_by_date(banking_operations_info, decreasing=False), width=85, indent=4)

    usd_transactions = filter_by_currency(transactions_for_generate, "USD")
    for _ in range(2):
        pprint.pprint(next(usd_transactions), width=85, indent=4)

    descriptions = transaction_descriptions(transactions_for_generate)
    for _ in range(3):
        print(next(descriptions))

    for card_number in card_number_generator(11, 20):
        print(card_number)
