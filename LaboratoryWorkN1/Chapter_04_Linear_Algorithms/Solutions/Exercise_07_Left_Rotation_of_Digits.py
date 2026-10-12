# Вхід: чотирицифрове натуральне число.
n = int(input())
first = n // 1000
remaining = n % 1000
print(remaining * 10 + first)
