# Задача 3.6. Припущення: a > 0 та b > 0.
import math

a, b = map(float, input().split())
c = math.hypot(a, b)
perimeter = a + b + c
area = a * b / 2

print(f"c = {c:.2f}, P = {perimeter:.2f}, S = {area:.2f}")
