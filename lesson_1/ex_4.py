# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
n = int(input('Enter integer number: '))
m = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > m:
        m = n % 10
    if n > 9:
        continue
    else:
        print(str(f'Max number:{m}'))
        break
