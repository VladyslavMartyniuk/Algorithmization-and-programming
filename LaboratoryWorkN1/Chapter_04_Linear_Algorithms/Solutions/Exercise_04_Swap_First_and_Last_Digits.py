# Вхід: трицифрове натуральне число.
n = int(input())
first = n // 100
middle = n // 10 % 10
last = n % 10
print(last * 100 + middle * 10 + first)
