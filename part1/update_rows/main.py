# Изменение данных
#
#
# Когда мы начали работать с получившейся таблицей,
# то поняли, что тип животных не стоит разделять по полу.
# Так что теперь нам нужно заменить
# в столбце AnimalType значение Кот на Кошка, Пес на Собака.
# Напишите соответствующий запрос.

import sqlite3

from prettytable import prettytable

with sqlite3.connect("animals_db.sqlite") as connection:
    cursor = connection.cursor()
    sqlite_query = """ 
            DROP TABLE animals_4;
            CREATE TABLE animals_4 (
            id integer PRIMARY KEY AUTOINCREMENT,
            animal_type varchar(50) NOT NULL,
            sex varchar(50),
            name varchar(50)
            CONSTRAINT df_name DEFAULT 'Noname',
            date_of_birth date,
            age integer,
            weight decimal);
            INSERT INTO animals_4
            (animal_type, sex, name, date_of_birth, age, weight)
            VALUES ('Кошка', 'Ж', 'Соня', '2013-12-02', 7, 2.15),
            ('Кот', 'М', 'Семен', '2017-05-03', 4, 4.5),
            ('Собака', 'Ж', 'Алина', '2018-11-12', 2, 20.8),
            ('Пес', 'М', 'Бобик', '2015-08-25', 6, 5.75);
            UPDATE animals_4 SET animal_type = 'Кошка' WHERE animal_type='Кот'
            """
    cursor.executescript(sqlite_query)
    # cursor.execute(sqlite_query)
    cursor.fetchall()


def print_result():
    result_query = ('SELECT * from animals')
    table = cursor.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result()
