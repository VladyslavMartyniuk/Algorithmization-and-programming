n = int(input())  # натуральне n > 0
first_digit = n % 10
minimum = maximum = first_digit
while n > 0:
    digit = n % 10
    if digit < minimum:
        minimum = digit
    if digit > maximum:
        maximum = digit
    n //= 10
print(f"max = {maximum}, min = {minimum}")
