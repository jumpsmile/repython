# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

NUMS = ('Один', 'Два', 'Три', 'Четыре')

with open('file_4.txt', 'r', encoding='utf-8') as fhs:
    lines = fhs.readlines()

numbers = [int(line[-2]) for line in lines if line != '\n']
content = "\n".join(f'{NUMS[n - 1]} - {n}' for n in numbers)

with open('file_4_new.txt', 'w', encoding='utf-8') as fhd:
    fhd.write(content)
