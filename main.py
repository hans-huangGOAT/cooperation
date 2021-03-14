import pandas as pd
from datetime import date
from datetime import datetime

import src.utils as utils
from src.user import User
from src.bank import Bank
from src.account import Account, AccountType
from src.transaction import Transaction, TransactionType

# create a bank with users you can play around with
bank = Bank()
df = pd.read_csv('data/users.csv')

for index, row in df.iterrows():
    sec_qs = {
        row.security_question_1: row.security_answer_1,
        row.security_question_2: row.security_answer_2,
        row.security_question_3: row.security_answer_3

    }
    dt = datetime.combine(pd.Timestamp(row.dob).date(), datetime.min.time())

    bank.add_user(User(row.username, row.password,
                       row['name'], dt, row.address, sec_qs))

# You can assume that the code above is correct.
# Use the space below to test out any functions or pieces of code.

user = User("Huang", "123456", "Zean", datetime.now(), "Qingdao", {
            "favoriteFood": "Apple", "Parent": "Mother", "Sports": "Basketball"})
print(user.__str__())

if type(bank) == Bank:
    print("You can delete this block of code in main.py if you want!")

account = Account(user, AccountType.SAVINGS, "123456", 1000.2)
print(account.__str__())

transaction = Transaction(user._uuid, account._uuid,
                          "123456", datetime.now(), 600, TransactionType.DEPOSIT)
print(transaction.__str__())

print(account.validate_transaction(transaction))
print(account.get_deposit_history())
