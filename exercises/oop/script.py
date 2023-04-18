import os
import json
from modules import statement

def run():
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)

    # Reading file info
    with open(f'{BASE_DIR}/test_user_info.json', 'r') as f:
        person_info = json.load(f)

    incomes = []
    expenses = []
    for k, v in person_info.items():
        if k == "firstname":
            name = v
        elif k == "lastname":
            lastname = v
        elif k == "incomes":
            for i in v.values():
                incomes.append(i["amount"])
        elif k == "expenses":
            for i in v.values():
                expenses.append(i["amount"])

    # Person's info
    acct_1 = statement.PersonAccount(name, lastname, incomes, expenses)
    acct_1.addIncome(200)
    acct_1.addExpense(100)
    print(acct_1.accountInfo())

# Entry point
if __name__ == '__main__':
    run()