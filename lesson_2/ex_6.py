# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]}

products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')

    unit = tmp

    products.append((
        order,
        {
            'Название': title,
            'Стоимость': price,
            'Количество': amount,
            'Ед. изм.': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (д/н)) ')
    if q.lower() == 'д':
        break

analytic = {
    'Название': [],
    'Стоимость': [],
    'Количество': [],
    'Ед. изм.': set()
}

for _, item in products:
    analytic['Название'].append(item['Название'])
    analytic['Стоимость'].append(item['Стоимость'])
    analytic['Количество'].append(item['Количество'])
    analytic['Ед. изм.'].add(item['Ед. изм.'])
print(analytic)
