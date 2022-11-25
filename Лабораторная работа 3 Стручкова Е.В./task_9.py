salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
month_ = 1
while True:
    delta = spend - salary
    if month_ > months:
        break
    month_ += 1
    money_capital += delta
    spend *= 1 + increase
print(round(money_capital))
