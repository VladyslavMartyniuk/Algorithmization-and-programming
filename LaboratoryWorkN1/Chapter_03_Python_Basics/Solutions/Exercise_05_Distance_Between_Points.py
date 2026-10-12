# Задача 3.5. Координати дійсні.
import math

x1, y1, x2, y2 = map(float, input().split())
distance = math.hypot(x2 - x1, y2 - y1)

print(f"d = {distance:.2f}")
