from LibraryData import *
from dataclasses import make_dataclass


class Business:
    def __init__(self) -> None:
        self.data = LibraryData()
        self.loggedOnUser: UserData = None

    def attemptRegister(self, username, password, accType):
        if self.data.getUser(username) != None:
            return None
        else:
            return self.data.createUserAccount(username, password, accType)

    def attemptLogin(self, username, password):
        user: UserData = self.data.getUser(username)
        if user == None:
            return None
        salt = user._passwordSalt
        hash = self.data.hashPassword(password, salt)
        if (hash == user._passwordHash):
            self.loggedOnUser = user
            return user
        else:
            return None

    def getLibraryInfo(self):
        ["username", "usertype", "customerCount", "bookCount", "borrowedCount"]
        username = self.loggedOnUser._username
        usertype = self.loggedOnUser._type
        customerCount = len(self.data.getUsers())
        bookCount = len(self.data.getBooks())
        if self.loggedOnUser._type == 1:
            borrowedCount = len(self.loggedOnUser._customer._booksBorrowed)
        else:
            borrowedCount = 0
        return self.data.LibInfo(username, usertype, customerCount, bookCount, borrowedCount)
