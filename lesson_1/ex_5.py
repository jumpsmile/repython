# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
profit = float(input('Enter profit: $'))
cost = float(input('Enter cost: $'))

if profit >= cost:
    if profit == cost:
        print('The firm does not earn')
    else:
        print('The firm earns')
        profitability = profit - cost
        income = (profitability / profit)
        print('Profitability {:.02%}'.format(income))
        employees = int(input('Enter the number of employees: '))
        print(f'Employee income ${profitability / employees:.02}')
else:
    print('The firm loses')
