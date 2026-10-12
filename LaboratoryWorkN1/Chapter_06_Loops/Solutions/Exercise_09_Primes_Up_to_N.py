n = int(input())
primes_for_output = []  # список використано лише для рядка виводу
for candidate in range(2, n + 1):
    divisor = 2
    is_prime = True
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        primes_for_output.append(str(candidate))
if primes_for_output:
    print(f"{' '.join(primes_for_output)} ({len(primes_for_output)} чисел)")
else:
    print("(0 чисел)")
