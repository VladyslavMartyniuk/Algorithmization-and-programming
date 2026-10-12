# Вхід: двоцифрове натуральне число.
n = int(input())
tens = n // 10
units = n % 10
reversed_number = units * 10 + tens
print(f"{reversed_number}, сума = {n + reversed_number}")
