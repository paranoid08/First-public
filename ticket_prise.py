n=int(input('Введите количество билетов:'))
sum=0
for i in range(n):
    age=int(input('Введите возраст посетителя:'))
    if age<18:
        sum+=0
    if 18<=age<25:
        sum+=990
    if age>25:
        sum+=1390
if n>3:
        sum*=0.9
print ('Общая сумма к оплате:',sum,'руб.')