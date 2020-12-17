# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


my_func(name='Petr', surname='Petrov', year=1993, city='Moscow', email='petrov@petr.ru', phone='8-800-888-88-88')
