import datetime

from src.widget import get_date, mask_account_card

if __name__ == "__main__":

    bank_card_or_account_number = input("Введите номер банковской карты или счета")

    print(mask_account_card(bank_card_or_account_number))
    print(get_date(str(datetime.datetime.now())))
