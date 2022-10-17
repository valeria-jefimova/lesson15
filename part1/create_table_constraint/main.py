# Cоздание таблицы со столбцом по умолчанию
#
# Создайте таблицу в БД на основе схемы из
# предыдущей задачи. При создании таблицы
# предусмотрите для поля Name значение по умолчанию "Noname"
#
import sqlite3
from prettytable import prettytable

with sqlite3.connect("animals_db.sqlite") as connection:
    cursor = connection.cursor()
    sqlite_query = """ 
        CREATE TABLE animals_3 (
        id integer PRIMARY KEY AUTOINCREMENT, 
        animal_type varchar(50) NOT NULL, 
        sex varchar(50), 
        name varchar(50) 
        CONSTRAINT df_name DEFAULT 'Noname', 
        date_of_birth date,
        age integer,
        weight decimal)"""  # TODO составьте запрос на создание таблицы

# Не удаляйте этот код, он используется для вывода заголовков созданной таблицы
def print_result(sqlite_query):
    cursor.execute(sqlite_query)
    result_query = 'SELECT * from animals_3'
    table = cursor.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
