# Вхід: невід'ємна кількість хвилин.
minutes_total = int(input())
days = minutes_total // (24 * 60)
remaining = minutes_total % (24 * 60)
hours = remaining // 60
minutes = remaining % 60
print(f"{days} діб {hours} год {minutes} хв")
