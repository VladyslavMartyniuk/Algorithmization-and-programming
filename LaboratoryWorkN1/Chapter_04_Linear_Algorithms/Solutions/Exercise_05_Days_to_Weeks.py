# Вхід: невід'ємна кількість днів.
days_total = int(input())
weeks = days_total // 7
days = days_total % 7
print(f"{weeks} тиж {days} дн")
