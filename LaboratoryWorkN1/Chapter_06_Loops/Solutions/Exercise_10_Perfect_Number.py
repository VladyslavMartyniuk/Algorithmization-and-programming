n = int(input())  # натуральне n > 0
proper_divisors_sum = 0
# Будь-який власний дільник n не перевищує n // 2.
for divisor in range(1, n // 2 + 1):
    if n % divisor == 0:
        proper_divisors_sum += divisor
if proper_divisors_sum == n:
    print("досконале")
else:
    print("не досконале")
