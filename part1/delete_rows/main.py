# Удаление записи из БД
#
# Собака Алина давно перестала быть пациенткой ветклиники,
# так что нужно удалить запись о ней из базы.
# Реализовать соответствующий запрос.
#
#
import sqlite3

with sqlite3.connect("animals_db.sqlite") as connection:
    cursor = connection.cursor()
    sqlite_query = """ 
            DROP TABLE animals_3;
            CREATE TABLE animals_3 (
            id integer PRIMARY KEY AUTOINCREMENT,
            animal_type varchar(50) NOT NULL,
            sex varchar(50),
            name varchar(50)
            CONSTRAINT df_name DEFAULT 'Noname',
            date_of_birth date,
            age integer,
            weight decimal);
            INSERT INTO animals_3
            (animal_type, sex, name, date_of_birth, age, weight)
            VALUES ('Кошка', 'Ж', 'Соня', '2013-12-02', 7, 2.15),
            ('Кот', 'М', 'Семен', '2017-05-03', 4, 4.5),
            ('Собака', 'Ж', 'Алина', '2018-11-12', 2, 20.8),
            ('Пес', 'М', 'Бобик', '2015-08-25', 6, 5.75);
            DELETE FROM animals_3 WHERE `Name`='Алина'
            """
    cursor.executescript(sqlite_query)
    # cursor.execute(sqlite_query)
    cursor.fetchall()

# Не удаляйте этот код, он используется
# для вывода результата


# def print_result(sqlite_query):
#     cursor.execute(sqlite_query)
#     result_query = 'SELECT * from animals'
#     table = cursor.execute(result_query)
#     mytable = prettytable.from_db_cursor(table)
#     mytable.max_width = 30
#     print(mytable)
#
#
# if __name__ == '__main__':
#     print_result(sqlite_query)
