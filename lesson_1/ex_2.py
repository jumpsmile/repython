# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input('Enter seconds: '))
h = sec // 3600
m = sec % 3600 // 60
s = sec % 3600 % 60

print('%02d:%02d:%02d' % (h, m, s))
