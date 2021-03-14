import src.utils as utils

from datetime import date
import uuid as uuid_lib
import random
import re


class User:
    def __init__(self, username: str, password: str, name: str, dob: date, address: str, security_questions: dict):
        '''
        Initializes a User object.
        You can assume that this code is correct.
        '''
        self._name = name
        self._dob = dob
        self._address = address
        self._uuid = str(uuid_lib.uuid4())
        self._username = username
        if len(security_questions) != 3:
            raise ValueError('Each user must have three security questions.')
        self._security_questions = {q: utils.hash_str(
            security_questions[q]) for q in security_questions}
        if not User.validate_password_strength(password):
            raise ValueError('A password must be between 8-20 characters and contain at least \
                one uppercase letter, one number, and one special character.')
        self._password = utils.hash_str(password)

    def __str__(self) -> str:
        '''
        This function allows you to print out a user's information or represent a user as a string.
        You can assume that this function is correct. 

        ex: print(<user_object_here>)
        ex: str(<user_object_here>)
        '''
        return '\nUSER OBJECT:\nName:\t\t%s\nUsername:\t%s\nPassword:\t%s\nUUID:\t\t%s\nDOB:\t\t%s\nAddress:\t%s\n' \
            % (self._name, self._username, self._password[0], self._uuid, str(self._dob), self._address)

    def __repr__(self) -> str:
        '''
        This function allows you to view a user's information in a CLI.
        You can assume that this function is correct. 
        '''
        return str(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def dob(self) -> date:
        return self._dob

    @property
    def address(self) -> str:
        return self._address

    @property
    def uuid(self) -> str:
        return self._uuid

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> (str, str):
        return self._password

    @property
    def security_questions(self) -> dict:
        return self._security_questions

    def get_random_question(self) -> str:
        '''
        Selects a random security question from the user's security questions.
        '''
        return random.choice(self.security_questions.keys())

    @classmethod
    def validate_password_strength(cls, password: str) -> bool:
        '''
        Checks if the provided password has:
            - at least one special character: one of !@#$%^&*<>?
            - at least one upper case letter
            - at least one number
            - a length between 8 and 20 characters
        Returns True if the password meets the above requirements. Returns False otherwise.
        '''
        return True

    def reset_password(self, security_question: str, security_answer: str, new_password: str) -> None:
        '''
        Checks whether the answer to the provided security question matches the **HASHED answer** to the same
        security question in the user's stored security questions. If the provided answer matches, this function
        resets the user's password to the provided password **that must now be hashed**.

        If the provided security question is not in the user's configured security questions,
        raise a TypeError

        Then, if the answer to the security question is incorrect, raise a PermissionError

        Then, if the user has answered the security question correctly, BUT the new password is not
        strong enough, raise a RuntimeError.

        Then, if the new password is the same as the old password, raise a ValueError.
        '''

        if security_question in self._security_questions:
            raise ValueError(
                'User has not configured the provided security question')

        security_answer_salt, hashed_answer = self._security_questions[security_answer]
        password_salt, old_password = self._password

        if not utils.check_str(security_answer, hashed_answer, security_answer_salt):
            raise ValueError(
                'The provided answer to the selected security question is incorrect.')
        elif not User.validate_password_strength(new_password):
            raise ValueError('A password must be between 8-20 characters and contain at least \
                one uppercase letter, one number, and one special character.')
        elif utils.check_str(new_password, old_password, password_salt):
            raise ValueError(
                'The new password cannot be the same as the old password.')
        else:
            self._password = utils.hash_str(new_password)
