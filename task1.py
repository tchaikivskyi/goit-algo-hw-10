from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = LpVariable('FruitJuice', lowBound=0, cat='Continuous')

model += 2*lemonade + fruit_juice <= 100, "WaterLimit"
model += lemonade <= 50, "SugarLimit"
model += lemonade <= 30, "LemonJuiceLimit"
model += 2*fruit_juice <= 40, "FruitPureeLimit"

model += lemonade + fruit_juice, "TotalProducts"

model.solve()

print("Оптимальна кількість виробленого Лимонаду:", value(lemonade))
print("Оптимальна кількість виробленого Фруктового соку:", value(fruit_juice))
print("Максимальна загальна кількість продуктів:", value(model.objective))
