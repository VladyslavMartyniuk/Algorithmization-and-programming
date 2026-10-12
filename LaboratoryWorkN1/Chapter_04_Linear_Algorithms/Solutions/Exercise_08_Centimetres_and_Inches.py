# Вхід: невід'ємна кількість сантиметрів.
# Повні дюйми рахуємо цілими числами: 1 дюйм = 254/100 см.
cm = int(input())
meters = cm // 100
remaining_cm = cm % 100
full_inches = cm * 100 // 254
print(f"{meters} м {remaining_cm} см, {full_inches} дюймів")
