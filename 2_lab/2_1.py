money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mes = -1 # так как мы знаем (из учловия), что подушка у нас ЕСТЬ и она положительна
        # => хотя бы раз в цикл программа точно зайдет. => хотя бы раз mes++
        # => при изначальном значении mes = -1 программа даст верный ответ
while money_capital>0:
    money_capital += (salary - spend)
    mes+=1
    spend += spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", mes)