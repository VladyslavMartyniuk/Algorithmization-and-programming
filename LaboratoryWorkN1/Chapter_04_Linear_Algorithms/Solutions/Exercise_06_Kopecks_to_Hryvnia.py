# Вхід: невід'ємна сума в копійках.
kopecks_total = int(input())
hryvnias = kopecks_total // 100
kopecks = kopecks_total % 100
print(f"{hryvnias} грн {kopecks:02d} коп")
