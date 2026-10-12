n = int(input())  # натуральне число
if n == 0:
    digit_sum = digit_product = 0
else:
    digit_sum = 0
    digit_product = 1
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_product *= digit
        n //= 10
print(f"сума = {digit_sum}, добуток = {digit_product}")
