money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mes = 0
while True:
    change = salary - spend
    if change + money_capital < 0:
        break
    else:
        money_capital += change
        mes += 1
        spend += (spend* increase)
print("Количество месяцев, которое можно протянуть без долгов:", mes)
