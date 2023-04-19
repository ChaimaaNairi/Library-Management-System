# Library Management System
The Library Management System is a Python project that keeps track of users who borrow books in a library and their details. The system allows users to log in and create a profile where they can see when they received the book and when they should return it. Students receive a discount on the book price, and they can search for books by title, author, code, and price.</br>

<h2>Design of the System</h2>
The design of the Library Management System includes the problem definition, targets, and actors of the system.</br>

<h3>Problem Definition and Targets </h3>
The library management system aims to provide a platform where users can easily borrow books from the library. The system allows users to create a profile, see their borrowed books, and return them on time. The system also offers a discount to students, making it easier for them to borrow books.</br>

<h3>System Actors </h3>
The Library Management System has three actors: users, system administrators, and the database. Users can log in and create a profile, while system administrators can determine the return and receipt dates, show available books, and tell users how many books they can borrow. The database stores all user information.</br>

<h3>Implementation of Layers</h3>
The Library Management System is divided into three layers: presentation, business, and data.</br></br>

<b>Presentation Layer</b></br>
The presentation layer provides a graphical user interface (GUI) for the Library Management System using the Tkinter library, which is built into Python. The GUI includes a login window where users can enter their username and password and search for books. Users can also sign up for the system, reset their password, and view their borrowed books. System administrators can add or edit book information.</br>

<b>Business Layer</b></br>
The business layer provides all the internal processes for the Library Management System. It contains classes for all the required assets of the project, and the interactions of these classes give way to the operation of the program.</br>
The central class of the business layer is the "Library" class, which holds important information about the library and program and instantiates other classes as needed. The "User" class generates user objects that contain all the information about the users and perform all the actions. The "Book" class holds information about a book, including the title, author, price, and availability.</br>
The business layer also communicates with the data layer to update user and book information.</br>

<b>Data Layer</b></br>
The data layer stores all user information and past sessions of the Library Management System. The system uses SQLite, a database management system, to store all the data in local storage and access it via file access channels.</br>
The data layer uses the sqlite3 library of the Python language to enable communication with the database. When a user updates their information or borrows a book, the corresponding record in the database is updated.</br>

<h2>Conclusion</h2>
The Library Management System provides a user-friendly interface for users to borrow books from the library. The system's layered architecture ensures that it is easy to maintain and update, and its use of a database management system ensures that data is stored securely and easily accessible.</br>


