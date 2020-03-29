# Project 0x0F.

Python - Object-relational mapping


## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

## Read or watch:


    Object-relational mappers
    mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
    MySQLdb tutorial
    SQLAlchemy tutorial
    SQLAlchemy
    mysqlclient/MySQLdb
    Introduction to SQLAlchemy
    Flask SQLAlchemy
    10 common stumbling blocks for SQLAlchemy newbies
    Python SQLAlchemy Cheatsheet
    SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)


## Learning Objectives


At the end of this project, you are expected to be able to explain to anyone, without the help of Google.


### General

Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))

How to connect to a MySQL database from a Python script

How to SELECT rows in a MySQL table from a Python script

How to INSERT rows in a MySQL table from a Python script

    What ORM means

How to map a Python Class to a MySQL table


## Requirements

### General


    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    Your files will be executed with MySQLdb version 1.3.x
    Your files will be executed with SQLAlchemy version 1.2.x
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    You are not allowed to use execute with sqlalchemy



## Tasks

 0. If it's not tested it doesn't work mandatory 
 1. Base class mandatory 
 2. First Rectangle mandatory 
 3. Validate attributes mandatory 
 4. Area first mandatory 
 5. Display #0 mandatory 
 6. __str__ mandatory 
 7. Display #1 mandatory 
 8. Update #0 mandatory 
 9. Update #1 mandatory 
 10. And now, the Square! mandatory 
 11. Square size mandatory
 12. Square update mandatory
 13. Rectangle instance to dictionary representation mandatory
 14. Square instance to dictionary representation mandatory
 15. Dictionary to JSON string mandatory
 16. JSON string to file mandatory
 17. JSON string to dictionary mandatory
 18. Dictionary to Instance mandatory
 19. File to instances mandatory
 20. JSON ok, but CSV? #advanced
 21. Let's draw it #advanced


## More Info
### Install MySQLdb module version 1.3.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```
Install SQLAlchemy module version 1.2.x
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'
```
Also, you can have this warming message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
cursor.execute(statement, parameters)  
```
You can ignore it.


## Coding style tests

PEP 8 style (version 1.7.*)
```
sudo apt-get install python3-pep8
```

## Built With

* Emacs editor.
* gcc 4.8.4 compiler.
* Linux vagrant-ubuntu-trusty-64 3.13.0-170-generic / Ubun 14.04.06

## Author

* **Leonardo Calderon J.** - *Initial work* - [LeoCJJ](https://github.com/leocjj)
01/28/2020
