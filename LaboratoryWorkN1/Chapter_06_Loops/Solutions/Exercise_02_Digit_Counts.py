n = int(input())  # n >= 0
if n == 0:
    digits_count = even_count = 1  # число 0 має одну парну цифру
else:
    digits_count = even_count = 0
    while n > 0:
        digit = n % 10
        digits_count += 1
        if digit % 2 == 0:
            even_count += 1
        n //= 10
print(f"цифр = {digits_count}, парних = {even_count}")
