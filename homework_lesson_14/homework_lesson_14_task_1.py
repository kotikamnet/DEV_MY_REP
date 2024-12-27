"""
Представим, что у нас есть таблица "Employees" с полями "Name", "Position", "Department", "Salary".
 ● Создайте таблицу "Employees" с указанными полями. +
 ● Вставьте в таблицу несколько записей с информацией о сотрудниках вашей компании. +
 ● Измените данные в таблице для каких-то сотрудников. +
Например, изменим должность одного из сотрудников на более высокую. +
 ● Добавьте новое поле "HireDate" (дата приема на работу) в таблицу "Employees".
 ● Добавьте записи о дате приема на работу для всех сотрудников. +
 ● Найдите всех сотрудников, чья должность "Manager". +
 ● Найдите всех сотрудников, у которых зарплата больше 5000 долларов. +
 ● Найдите всех сотрудников, которые работают в отделе "Sales". +
 ● Найдите среднюю зарплату по всем сотрудникам.
 ● Удалите таблицу "Employees".
"""

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('../lesson_14/employees.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
Name TEXT NOT NULL PRIMARY KEY
Position TEXT NOT NULL
Department TEXT NOT NULL
Salary INTEGER)
""")

connection.commit()

employees = [
    ('Alex Pupkin', 'Engineer', 'It', 5500),
    ('Masha Pupkina', 'Analyst', 'Analytics', 5000),
    ('Sergey Slay', 'Manager', 'Sales', 800)
]

cursor.executemany('INSERT INTO Employees (Name, Position, Department, Salary) '
                   'VALUES (?, ?, ?, ?)', employees)

connection.commit()

cursor.execute('UPDATE Employees SET Position = ? WHERE Name = ?', ('Lead Analyst', 'Masha Pupkina'))

cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')

hire_dates = [
    ('2024-11-22', 'Alex Pupkin'),
    ('2022-11-11', 'Masha Pupkina'),
    ('2020-12-12', 'Sergey Slay')
]
cursor.executemany('UPDATE Employees SET HireDate = ? WHERE Name = ?', hire_dates)

cursor.execute('SELECT Name FROM Employees WHERE Position = ?', ('Manager',))
manager_employees = cursor.fetchall()
print('Менеджеры:', manager_employees)

cursor.execute('SELECT Name FROM Employees WHERE Salary > ?', (5000,))
salary_employees = cursor.fetchall()
for salary_employee in salary_employees:
    print('Зп выше 5000:', salary_employee)

cursor.execute('SELECT Name FROM Employees WHERE Department = ?', ('Sales',))
sales_employees = cursor.fetchall()
for sales_employee in sales_employees:
    print('Работают в sales:', sales_employee)

cursor.execute('SELECT AVG(Salary) from Employees')
average_salary = cursor.fetchone()[0]
print('Средняя зп:', average_salary)

# Удаление таблицы
cursor.execute('DROP TABLE IF EXISTS Employees')

connection.commit()
connection.close()