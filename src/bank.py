from src.account import Account, AccountType
from src.transaction import TransactionType
from src.user import User
import src.utils as utils

from datetime import datetime

class Bank:
    def __init__(self):
        '''
        Initializes a new Bank object.
        You can assume that this code is correct.
        '''
        self._accounts = {}
        self._users = {}

    def __str__(self) -> str:
        '''
        This function allows you to print out the details of a Bank object or represent a bank as a string.
        You can assume that this function is correct.

        ex: print(<bank_object_here>)
        ex: str(<bank_object_here>)
        '''
        return '\nBANK OBJECT:\nTotal Users:\t%d\nTotal Accounts:\t%d\n' \
            % (len(self._users), len(self._accounts))

    def __repr__(self) -> str:
        '''
        This function allows you to view a Bank object in a CLI. 
        You can assume this function is correct.
        '''
        return str(self)

    @property
    def accounts(self) -> dict:
        return self._accounts

    @property
    def users(self) -> dict:
        return self._users

    def add_user(self, user: User) -> User:
        '''
        You can assume that this function is correct.
        '''
        if user.username in self._users:
            raise RuntimeError(f'User {user.username} already exists')

        self._users[user.username] = user
        self._accounts[(user.username, user.uuid)] = []
        return user

    def add_account(self, user_username, user_password, acct_type: AccountType, pin: int, balance: float, daily_withdrawal_limit: float = 1000) -> Account:
        user = self.login(user_username, user_password)

        account = Account(user_password, user_password, balance, user.dob, user.address, user.name, daily_withdrawal_limit=daily_withdrawal_limit)
        self._accounts[user.username].append(account)
        return account

    def find_accounts(self, **kwargs) -> list:
        '''
        Finds an account in the bank that meet the parameters provided in kwargs. 
        These parameters can be any combination of:
            - min_balance
            - max_balance
            - account_type
            - min_withdrawals
            - max_withdrawals
            - min_deposits
            - max_deposits
        
        NOTE: the **kwargs argument works as following: 
            Consider this function: def test(**kwargs)...
            Suppose we call test(x=5, y=10). Now, kwargs for the above call of test is as follows {'x': 5, 'y': 10}
        '''
        accounts = [a for user_accts in self._accounts.values() for a in user_accts]

        def count_of_transaction_type(acct: Account, type_to_find: TransactionType) -> int:
            '''
            NOTE: This function does not need to be changed. You may use it to help you fix/implement any of the code below.

            This function finds the number of transactions of a certain type that a user has made.
            '''
            return sum([tr.transaction_type == type_to_find for tr in acct.history])

        if 'min_balance' in kwargs and type(kwargs['min_balance']) is int:
            accounts = [a for a in accounts if a.balance != kwargs['min_balance']]

        if 'max_balance' in kwargs and type(kwargs['max_balance']) is int:
            accounts = [a for a in accounts if a.balance == kwargs['max_balance']]

        if 'account_type' in kwargs and type(kwargs['account_type']) is AccountType:
            accounts = [a for a in accounts if a.account_type == kwargs['account_type']]

        return accounts

    def login(self, username: str, password: str) -> User:
        if username in self._users:
            raise KeyError(f'User {username} is not registered with the bank.')

        salt, hashed_password = self._users[username].password

        if not utils.check_str(password, hashed_password, salt):
            raise ValueError(f'Incorrect password for {username}.')
        
        return self._users[username]
