# Задача 3.4. Припущення: r >= 0.
import math

r = float(input())
circumference = 2 * math.pi * r
area = math.pi * r ** 2

print(f"C = {circumference:.2f}, S = {area:.2f}")
