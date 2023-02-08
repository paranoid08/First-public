per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input('Введите сумму вклада:'))
deposit=[]
deposit.append(money/100*per_cent['ТКБ'])
deposit.append(money/100*per_cent['СКБ'])
deposit.append(money/100*per_cent['ВТБ'])
deposit.append(money/100*per_cent['СБЕР'])
max_sum = max(deposit)
bank = max(per_cent, key=per_cent.get) # поиск ключа (названия банка) с максимальным доходом по вкладу
print("Максимальный доход по вкладу составит:", max_sum, "в банке", bank)


# второй способ с использованием цикла
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input('Введите сумму вклада:'))
deposit=[]
for key in per_cent:
    deposit.append(money/100*per_cent[key])
max_sum = max (deposit)
bank=max (per_cent, key=per_cent.get)
print("Максимальный доход по вкладу составит:", max_sum, "в банке", bank)