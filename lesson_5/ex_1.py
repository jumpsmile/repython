# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
my_f = open('file_1.txt', 'w')
line = input('Enter the text \n')
while line:
    my_f.writelines(line)
    line = input('Enter the text \n')
    if not line:
        break

my_f.close()
my_f = open('file_1.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()
