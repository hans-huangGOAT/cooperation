from datetime import datetime
import uuid as uuid_lib
from enum import Enum

class TransactionType(Enum):
    WITHDRAW = "Withdrawal"
    DEPOSIT = "Deposit"

class Transaction:
    '''
    Stores data for a single transaction for a user in an account.
    '''
    def __init__(self, user_uuid: str, account_uuid: str, pin: str, timestamp: datetime, amount: float, transaction_type: TransactionType):
        '''
        Initializes a Transaction object.
        You can assume that this code is correct.
        '''
        self._uuid = uuid_lib.uuid4()
        self._user_uuid = user_uuid
        self._account_uuid = account_uuid
        self._pin = pin
        self._timestamp = timestamp
        self._amount = amount
        self._transaction_type = transaction_type

    def __str__(self) -> str:
        return '\nTRANSACTION [%s]:\nUser UUID:\t%s\nType:\t\t%s\nAmount:\t\t%f\nTimestamp:\t%s\n' \
            % (self.uuid, self.user_uuid, self._transaction_type.name, self._amount, str(self._timestamp))
    
    def __repr__(self) -> str:
        return str(self)

    @property
    def uuid(self):
        return self._uuid

    @property
    def user_uuid(self):
        return self._user_uuid

    @property
    def account_uuid(self):
        return self._account_uuid
    
    @property
    def pin(self):
        return self._pin

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def amount(self):
        return self._amount

    @property
    def transaction_type(self):
        return self._transaction_type