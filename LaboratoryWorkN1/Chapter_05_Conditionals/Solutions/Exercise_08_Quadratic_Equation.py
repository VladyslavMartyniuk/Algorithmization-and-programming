# Вхід: дійсні коефіцієнти a, b, c через пробіл.
import math

a, b, c = map(float, input().split())
if a == 0:
    if b != 0:
        x = -c / b
        print(f"лінійне: x={x:g}")
    elif c == 0:
        print("безліч розв'язків")
    else:
        print("коренів немає")
else:
    b_squared = b * b
    four_ac = 4 * a * c
    discriminant = b_squared - four_ac
    # Відносний допуск допомагає не сплутати похибку float з D ≈ 0.
    tolerance = 1e-12 * max(abs(b_squared), abs(four_ac))
    if abs(discriminant) <= tolerance:
        x = -b / (2 * a)
        print(f"x={x:g}")
    elif discriminant > 0:
        root = math.sqrt(discriminant)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)
        print(f"x1={x1:g}, x2={x2:g}")
    else:
        print("коренів немає")
