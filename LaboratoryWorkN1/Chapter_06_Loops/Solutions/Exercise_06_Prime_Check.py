n = int(input())
if n == 1:
    print("ні просте, ні складене")
elif n < 1:
    print("помилка: введіть натуральне число")
else:
    divisor = 2
    is_prime = True
    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1
    print("просте" if is_prime else "складене")
