# import GUI, Business
import sqlite3
from dataclasses import make_dataclass
import string, random, hashlib, json


class LibraryData:
    LibInfo = make_dataclass("LibInfo", ["username", "usertype", "customerCount", "bookCount", "borrowedCount"])
    UserInfo = make_dataclass("UserInfo", ["id", "username", "usertype", "userid", "booksBorrowed"])
    BookInfo = make_dataclass("BookInfo", ["id", "title", "author", "price", "stock"])

    def __init__(self) -> None:
        self._database = sqlite3.connect("main.db")
        self._cur = self._database.cursor()
        self._cur.executescript('''
        CREATE TABLE IF NOT EXISTS book(id INT NOT NULL PRIMARY KEY, title TEXT NOT NULL, author TEXT, price INT NOT NULL, stock INT NOT NULL);
        CREATE TABLE IF NOT EXISTS user(id INT NOT NULL PRIMARY KEY, username TEXT NOT NULL, passwordHash TEXT NOT NULL, passwordSalt TEXT NOT NULL, type INT NOT NULL);
        CREATE TABLE IF NOT EXISTS customer(userid INT NOT NULL PRIMARY KEY, booksBorrowed TEXT NOT NULL);
        ''')
        self._database.commit()
        self.users = []
        self.books = []
        self.admins = []
        self.customers = []

    def getUsers(self):
        self._cur.execute("SELECT * FROM user")
        results = self._cur.fetchall()
        return results

    def getBooks(self):
        self._cur.execute("SELECT * FROM book")
        results = self._cur.fetchall()
        return results

    def getBookByTitle(self, title):
        self._cur.execute("SELECT * FROM book WHERE title = ?", (title,))
        book = self._cur.fetchone()
        return self.BookInfo(*book)

    def getUser(self, username):
        self._cur.execute("SELECT * FROM user WHERE username = ?", (username,))
        results = self._cur.fetchall()
        if len(results) > 0:
            return UserData(results[0][0], self._cur, self._database)
        else:
            return None

    def generateSalt(self):
        return "".join(random.sample(string.ascii_letters, 20))

    def hashPassword(self, password, salt):
        enc: str = password + salt
        hash = hashlib.sha512(enc.encode('latin-1'))
        return hash.digest().decode('latin-1')

    def createUserAccount(self, username, password, accType):
        salt = self.generateSalt()
        hashed = self.hashPassword(password, salt)
        self._cur.execute("SELECT * FROM user")
        users = self._cur.fetchall()
        if len(users) == 0:
            id = 0
        else:
            id = users[-1][0] + 1
        self._cur.execute("INSERT INTO user(id, username, passwordHash, passwordSalt, type) VALUES(?,?,?,?,?)",
                          (id, username, hashed, salt, accType))
        if accType == 1:
            self._cur.execute("INSERT INTO customer VALUES(?, ?)", (id, json.dumps([])))
        self._database.commit()
        return UserData(id, self._cur, self._database)

    def createBook(self, title, author, stock, price):
        self._cur.execute("SELECT * FROM book")
        books = self._cur.fetchall()
        self._cur.connection
        if len(books) == 0:
            id = 0
        else:
            id = books[-1][0] + 1
        self._cur.execute("INSERT INTO book VALUES(?,?,?,?,?)", (id, title, author, stock, price))
        self._database.commit()

    def updateBook(self, id, title, author, stock, price):
        self._cur.execute("UPDATE book SET title = ?, author = ?, stock = ?, price = ? WHERE id = ?",
                          (title, author, stock, price, id))
        self._database.commit()
        if id in BookData.existingObjects:
            BookData.existingObjects[id]._title = title
            BookData.existingObjects[id]._author = author
            BookData.existingObjects[id]._price = price
            BookData.existingObjects[id]._stock = stock


class BookData:
    existingObjects = {}

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            id = args[0]
            if type(id) == int and id in cls.existingObjects:
                return cls.existingObjects[id]
        return super(BookData, cls).__new__(cls)

    def __init__(self, id: int, _cur, _database) -> None:
        if type(id) == int:
            self._database = _database
            self._cur = _cur
            self._cur.execute("SELECT * FROM book WHERE id = ?", (id,))
            results = self._cur.fetchall()
            if len(results) != 1:
                raise ValueError("Invalid book id provided to create BookData object.")
            dbEntry = results[0]
            self._id = dbEntry[0]
            self._title = dbEntry[1]
            self._author = dbEntry[2]
            self._price = dbEntry[3]
            self._stock = dbEntry[4]
            self.existingObjects[id] = self


class UserData:
    existingObjects = {}

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            id = args[0]
            if type(id) == int and id in cls.existingObjects:
                return cls.existingObjects[id]
        return super(UserData, cls).__new__(cls)

    def __init__(self, id: int, _cur, _database) -> None:
        if type(id) == int:
            self._database = _database
            self._cur = _cur
            self._cur.execute("SELECT * FROM user WHERE id = ?", (id,))
            results = self._cur.fetchall()
            if len(results) != 1:
                raise ValueError("Invalid user id provided to create UserData object.")
            dbEntry = results[0]
            self._id = dbEntry[0]
            self._username = dbEntry[1]
            self._passwordHash = dbEntry[2]
            self._passwordSalt = dbEntry[3]
            self._type = dbEntry[4]
            if self._type == 0:
                self._customer = None
            elif self._type == 1:
                self._customer = CustomerData(self._id, _cur, self._database)
            self.existingObjects[id] = self


class CustomerData:
    existingObjects = {}

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            id = args[0]
            if type(id) == int and id in cls.existingObjects:
                return cls.existingObjects[id]
        return super(CustomerData, cls).__new__(cls)

    def __init__(self, id: int, _cur, _database) -> None:
        if type(id) == int:
            self._database = _database
            self._cur = _cur
            self._cur.execute("SELECT * FROM customer WHERE userid = ?", (id,))
            results = self._cur.fetchall()
            if len(results) != 1:
                raise ValueError("Invalid user id provided to create CustomerData object.")
            dbEntry = results[0]
            self._userid = dbEntry[0]
            self._booksBorrowed = json.loads(dbEntry[1])
            self.existingObjects[id] = self

    def addBook(self, book: BookData):
        self._booksBorrowed += [book._id]
        self._cur.execute("UPDATE customer SET booksBorrowed = ? WHERE userid = ?",
                          (json.dumps(self._booksBorrowed), self._userid))
        self._database.commit()

    def addBookById(self, bookid):
        self._booksBorrowed += [bookid]
        self._cur.execute("UPDATE customer SET booksBorrowed = ? WHERE userid = ?",
                          (json.dumps(self._booksBorrowed), self._userid))
        self._database.commit()

    def returnBook(self, book: BookData):
        self._booksBorrowed.remove(book._id)
        self._cur.execute("UPDATE customer SET booksBorrowed = ? WHERE userid = ?",
                          (json.dumps(self._booksBorrowed), self._userid))
        self._database.commit()

    def returnBookById(self, bookid):
        self._booksBorrowed.remove(bookid)
        self._cur.execute("UPDATE customer SET booksBorrowed = ? WHERE userid = ?",
                          (json.dumps(self._booksBorrowed), self._userid))
        self._database.commit()

    @property
    def booksBorrowed(self):
        return [BookData(id, self._cur, self._database) for id in self._booksBorrowed]


dat = LibraryData()
dat.getUsers()