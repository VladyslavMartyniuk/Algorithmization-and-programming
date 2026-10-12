# Задача 3.9. На вході — додатні цілі числа a і b.
import math

a, b = map(int, input().split())
gcd_value = math.gcd(a, b)
lcm_value = a * b // gcd_value

print(f"НСД = {gcd_value}, НСК = {lcm_value}")
