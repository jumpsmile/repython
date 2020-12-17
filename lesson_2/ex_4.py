# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input("Enter a few words ")
my_words = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_words = my_str.split()
    if len(str(my_words)) <= 10:
        print(f" {num} {my_words[el]}")
        num += 1
    else:
        print(f" {num} {my_words[el][0:10]}")
        num += 1
