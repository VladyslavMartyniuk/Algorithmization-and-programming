# Вхід: дата у вигляді шестицифрового цілого числа ДДММРР.
n = int(input())
day = n // 10000
month = n // 100 % 100
year = n % 100
print(f"{day:02d}.{month:02d}.20{year:02d}")
