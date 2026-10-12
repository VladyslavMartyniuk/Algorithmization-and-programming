n = int(input())  # натуральне n > 0
divisors_for_output = []
count = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        divisors_for_output.append(str(divisor))  # список використано лише для рядка виводу
        count += 1
print(" ".join(divisors_for_output), f"({count} дільників)")
