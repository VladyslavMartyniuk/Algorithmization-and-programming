n = int(input())  # натуральне n > 0
factorial = 1
factorials_sum = 0
for i in range(1, n + 1):
    factorial *= i
    factorials_sum += factorial
print(f"{n}! = {factorial}, сума = {factorials_sum}")
