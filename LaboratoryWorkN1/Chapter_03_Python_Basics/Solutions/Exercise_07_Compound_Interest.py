# Задача 3.7. Нарахування відсотків раз на рік, протягом 3 років.
principal, annual_rate = map(float, input().split())
amount = principal * (1 + annual_rate / 100) ** 3

print(f"{amount:.2f}")
