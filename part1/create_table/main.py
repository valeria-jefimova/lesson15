# Создание таблицы
# Дана схема таблицы пациентов ветеринарной клиники:
#
# Id — идентификатор карты
# AnimalType — вид животного
# Sex — пол животного
# Name — кличка
# DateOfBirth — дата рождения
# Age — возраст (полных лет)
# Weight — вес (килограммы + граммы)
#
# Создайте таблицу в БД на основе этой схемы
import sqlite3
from prettytable import prettytable

with sqlite3.connect("animals_db.sqlite") as connection:
    cursor = connection.cursor()
    sqlite_query = """ 
        CREATE TABLE animals_2 (
        id integer, 
        animal_type varchar(50), 
        sex varchar(50), 
        name varchar(50), 
        date_of_birth date,
        age integer,
        weight decimal)"""  # TODO составьте запрос на создание таблицы


# Не удаляйте код ниже, он используется для вывода заголовков созданной таблицы
def print_result(sqlite_query):
    cursor.execute(sqlite_query)
    result_query = 'SELECT * from animals_2'
    table = cursor.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
