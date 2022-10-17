# Добавление данных в таблицу
#
# Добавьте в БД следующих животных:
#
# +----+------------+-------+-----+-------------+-----+--------+
# | Id | AnimalType |  Name | Sex | DateOfBirth | Age | Weight |
# +----+------------+-------+-----+-------------+-----+--------+
# | 1  |   Кошка    |  Соня |  Ж  |  2013-12-02 |  7  |  2.15  |
# | 2  |    Кот     | Семен |  М  |  2017-05-03 |  4  |  4.5   |
# | 3  |   Собака   | Алина |  Ж  |  2018-11-12 |  2  |  20.8  |
# | 4  |    Пес     | Бобик |  М  |  2015-08-25 |  6  |  5.75  |
# +----+------------+-------+-----+-------------+-----+--------+
#
#
import sqlite3
from prettytable import prettytable

with sqlite3.connect("animals_db.sqlite") as connection:
    cursor = connection.cursor()
    # sqlite_query = """
    #         CREATE TABLE animals_3 (
    #         id integer PRIMARY KEY AUTOINCREMENT,
    #         animal_type varchar(50) NOT NULL,
    #         sex varchar(50),
    #         name varchar(50)
    #         CONSTRAINT df_name DEFAULT 'Noname',
    #         date_of_birth date,
    #         age integer,
    #         weight decimal)
    #         """
    sqlite_query = """
    INSERT INTO animals_3
    (animal_type, sex, name, date_of_birth, age, weight)
    VALUES ('Кошка', 'Ж', 'Соня', '2013-12-02', 7, 2.15),
    ('Кот', 'М', 'Семен', '2017-05-03', 4, 4.5),
    ('Собака', 'Ж', 'Алина', '2018-11-12', 2, 20.8),
    ('Пес', 'М', 'Бобик', '2015-08-25', 6, 5.75)
    """
    cursor.execute(sqlite_query)
    cursor.fetchall()
    # TODO составьте запрос на добавление данных в таблицу


# Не удаляйте этот код, он используется для вывода результата
# def print_result(sqlite_query):
#     cursor.execute(sqlite_query)
#     result_query = 'SELECT * from animals_3'
#     table = cursor.execute(result_query)
#     mytable = prettytable.from_db_cursor(table)
#     mytable.max_width = 30
#     print(mytable)
#
#
# if __name__ == '__main__':
#     print_result(sqlite_query)
