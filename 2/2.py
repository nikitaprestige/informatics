salary = 5000      # ежемесячная зарплата
spend = 6000       # траты за первый месяц
months = 10        # количество месяцев без долгов
increase = 0.03    # ежемесячный рост цен (3%)

money_capital = 0  # подушка безопасности
current_spend = spend  # траты текущего месяца (увеличение)

# дефицит за каждый месяц
for month in range(months):
    # если траты будут превышать зарплату, разница покрывается из подушки
    deficit = max(0, current_spend - salary)
    money_capital += deficit  # + дефицит к подушке
    current_spend *= (1 + increase)  # увеличить траты на следующий месяц

# округление
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))