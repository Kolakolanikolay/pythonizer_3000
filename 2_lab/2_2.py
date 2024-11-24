salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

time = months
money_capital = 0
while time > 0:
    money_capital -= (salary - spend)
    spend += spend * increase
    time -= 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
