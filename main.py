# подключение к библиотеке
import mysql.connector

# подключение к базе данных
mydb = mysql.connector.connect(
    host='localhost',
    # имя пользователя
    user='root',
    # пароль
    password='animishka',
    database='Library'

)

#для обращения к БД, MYSQL Workbench
mycursor=mydb.cursor()

#создание БД с именем library
def CreateDB():
    mycursor.execute('CREATE DATABASE Library')

#Создание таблиц
def CreateTables():
    #mycursor.execute('CREATE TABLE Books (Id INTEGER, Title VARCHAR(255), AuthorId INTEGER, GenreId INTEGER, PublishDate INTEGER, PublishId INTEGER)')
    mycursor.execute('CREATE TABLE Genres (Id INTEGER, NAME VARCHAR(255)) ')
    mycursor.execute('CREATE TABLE Publishers (Id INTEGER, Name VARCHAR(255), Address VARCHAR(255))')
    mycursor.execute('CREATE TABLE Authors (Id INTEGER, Name VARCHAR(255), BirthDate DATETIME)')



#Показ всех таблиц
def ShowTables():
    mycursor.execute('SHOW TABLES')
    for tb in mycursor:
        print(tb)

#ПОКАЗ ВСЕХ БД
def ShowDB():
    mycursor.execute('SHOW DATABASES')
    for db in mycursor:
        print(db)


