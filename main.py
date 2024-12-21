import pprint
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":

    bank_card_or_account_number = "Maestro 1596837868705199"
    banking_operations_info = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:10:00.216451"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T08:55:30.512364"}
    ]

    print(mask_account_card(bank_card_or_account_number))
    print(get_date("2019-07-03T18:35:29.512364"))

    pprint.pprint(filter_by_state(banking_operations_info), width=85, indent=4)
    pprint.pprint(sort_by_date(banking_operations_info, decreasing=False), width=85, indent=4)
